#!/usr/bin/env python3
"""
Al Rahal Auto Maintenance — static site generator.
Run:  python3 build.py      →  writes plain HTML into ../dist/
Edit  data/*.py and config below, then re-run. Upload /dist to public_html.
"""
import os, re, shutil, html, json, datetime
from data.services import SERVICES
from data.content import MODELS, BRANDS, POSTS, TESTIMONIALS, GENERAL_FAQ, GALLERY

# ------------------------------------------------------------------ CONFIG
CFG = dict(
  name="Al Rahal Auto Maintenance", short="Al Rahal",
  tagline="Range Rover & Land Rover Specialists",
  url="https://www.alrahalauto.ae",           # <-- your live domain, no trailing slash
  phone="055 747 9292", phone_intl="971557479292",
  email="alrahal8881@gmail.com",
  landline="06 558 3559", landline_intl="97165583559",
  city="Sharjah", country="United Arab Emirates",
  address="Jabel Tarek Street, opposite Sharjah Cricket Stadium",
  map_embed="https://www.google.com/maps?q=Al+Rahal+Auto+Maintenance+Workshop+Jabel+Tarek+Street+Sharjah&output=embed",
  lat="25.3308", lng="55.4197",
  hours="Saturday – Thursday · 8:00 AM – 1:00 PM & 4:00 PM – 9:00 PM · Friday closed",
  hours_lines=[("Saturday – Thursday","8:00 AM – 1:00 PM"),("Break","1:00 PM – 4:00 PM"),("Reopen","4:00 PM – 9:00 PM"),("Friday","Closed")],
  experience="25+", ga_id="",                    # GA4 id e.g. G-XXXXXXX, blank = off
  instagram="https://instagram.com/alrahal_auto_maintenance/",
)
WA = f"https://wa.me/{CFG['phone_intl']}"
OUT = os.path.join(os.path.dirname(__file__), "..", "dist")
TODAY = datetime.date.today().isoformat()
BUILD_STAMP = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
ASSET_VER = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M')  # cache-busting query string for CSS/JS
SITEMAP = []

def e(s): return html.escape(str(s), quote=True)
def wa(msg): 
    from urllib.parse import quote
    return f"{WA}?text={quote(msg)}"

# ------------------------------------------------------------------ ICONS (inline SVG, stroke-based, 24px grid)
def I(name, cls=""):
    p = ICONS[name]
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
ICONS = {
 "wa": '<path fill="currentColor" stroke="none" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91C21.95 6.45 17.5 2 12.04 2m.01 1.67c4.55 0 8.24 3.7 8.24 8.24 0 4.55-3.7 8.24-8.24 8.24-1.48 0-2.93-.39-4.19-1.15l-.3-.17-3.12.82.83-3.04-.2-.32a8.2 8.2 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.24-8.24M8.53 7.33c-.16 0-.43.06-.66.31-.22.25-.87.86-.87 2.07 0 1.22.89 2.39 1 2.56.14.17 1.76 2.67 4.25 3.73.59.27 1.05.42 1.41.53.59.19 1.13.16 1.56.1.48-.07 1.46-.6 1.67-1.18.21-.58.21-1.07.15-1.18-.07-.1-.23-.16-.48-.27-.25-.14-1.47-.74-1.69-.82-.23-.08-.37-.12-.56.12-.16.25-.64.81-.78.97-.15.17-.29.19-.53.07-.26-.13-1.06-.39-2-1.23-.74-.66-1.23-1.47-1.38-1.72-.12-.24-.01-.39.11-.5.11-.11.27-.29.37-.44.13-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.11-.56-1.35-.77-1.84-.2-.48-.4-.42-.56-.43-.14 0-.3-.01-.47-.01"/>',
 "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "check": '<path d="m5 12 4.5 4.5L19 7"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "close": '<path d="M6 6l12 12M18 6 6 18"/>',
 "shield": '<path d="M12 3 4 6v6c0 5 3.4 8.4 8 9 4.6-.6 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 "star": '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9z"/>',
 "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3 17.8 6.2 21l6.3-6.3a4 4 0 0 0 5.2-5.4l-2.5 2.5-2.1-2.1z"/>',
 "engine": '<path d="M7 8V6h4v2h4l2 3h3v6h-3l-2 3H7l-2-3H3v-6h2z"/><path d="M12 11v4"/>',
 "gearbox": '<circle cx="6" cy="6" r="2"/><circle cx="12" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><path d="M6 8v10M12 8v6h6M18 8v6"/><circle cx="6" cy="18" r="1.5"/>',
 "suspension": '<path d="M12 3v3M8 6h8M9 6l6 2-6 2 6 2-6 2 6 2-6 2h6M12 18v3"/>',
 "brake": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2"/>',
 "oil": '<path d="M12 3s-6 7-6 11a6 6 0 0 0 12 0c0-4-6-11-6-11z"/><path d="M9 15a3 3 0 0 0 3 3"/>',
 "diagnostics": '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M6 11h3l2-4 2 7 2-3h3M9 21h6"/>',
 "ac": '<path d="M12 3v18M3 12h18M6.5 6.5l11 11M17.5 6.5l-11 11"/><path d="M12 3l-2 2M12 3l2 2M12 21l-2-2M12 21l2-2"/>',
 "electrical": '<path d="M13 2 4 14h6l-1 8 9-12h-6z"/>',
 "cooling": '<path d="M12 3v18M12 3l-2.5 2.5M12 3l2.5 2.5M12 21l-2.5-2.5M12 21l2.5-2.5M4.2 7.5l15.6 9M4.2 7.5l3.4-.7M4.2 7.5l.7 3.4M19.8 16.5l-3.4.7M19.8 16.5l-.7-3.4M19.8 7.5 4.2 16.5"/>',
 "turbo": '<circle cx="12" cy="12" r="3"/><path d="M12 3a9 9 0 0 1 9 9h-3M12 3v3M3 12a9 9 0 0 0 9 9v-3"/>',
 "steering": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.5"/><path d="M3.5 10.5c3-1 14-1 17 0M12 14.5V21"/>',
 "tyre": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v5M12 16v5M3 12h5M16 12h5"/>',
 "battery": '<rect x="3" y="7" width="16" height="10" rx="2"/><path d="M21 10v4M7 12h4M9 10v4"/>',
 "drivetrain": '<circle cx="5" cy="12" r="2"/><circle cx="19" cy="12" r="2"/><path d="M7 12h10M12 12v-5M12 7h-3M12 7h3"/>',
 "exhaust": '<path d="M3 10h9l3-3h6v10h-6l-3-3H3z"/><path d="M21 7v10"/>',
 "screen": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "inspection": '<circle cx="10" cy="10" r="6"/><path d="m14.5 14.5 6 6M8 10h4M10 8v4"/>',
 "chain": '<rect x="3" y="9" width="8" height="6" rx="3"/><rect x="13" y="9" width="8" height="6" rx="3"/><path d="M11 12h2"/>',
 "mount": '<path d="M4 18h16M6 18v-4a6 6 0 0 1 12 0v4M12 8V4"/>',
 "drop": '<path d="M12 3s-7 8-7 12.5a7 7 0 0 0 14 0C19 11 12 3 12 3z"/>',
 "fuel": '<path d="M5 21V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v16M3 21h14M15 9h2a2 2 0 0 1 2 2v6a1.5 1.5 0 0 0 3 0V9l-2-2"/><rect x="8" y="6" width="4" height="4"/>',
 "paint": '<path d="M18 3 21 6l-9 9-4 1 1-4z"/><path d="M4 21c3-1 3-4 6-4"/>',
 "shine": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2 2M16 16l2 2M6 18l2-2M16 8l2-2"/><circle cx="12" cy="12" r="3"/>',
 "terrain": '<path d="M3 18 9 8l4 6 3-4 5 8z"/><circle cx="17" cy="6" r="2"/>',
 "car": '<path d="M5 13 7 7h10l2 6M3 13h18v5H3z"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/>',
 "award": '<circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 7 5-3 5 3-1.5-7"/>',
 "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/>',
 "facebook": '<path d="M14 9h3V5h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V9z"/>',
 "tiktok": '<path d="M14 3v11a3.5 3.5 0 1 1-3.5-3.5M14 3c.5 3 2.5 5 5 5"/>',
}

# ------------------------------------------------------------------ LAYOUT
LOGO = '''<a class="logo" href="/" aria-label="{name} home">
  <picture>
    <source media="(max-width:480px)" type="image/webp" srcset="/assets/brand/logo-compact.webp 1x, /assets/brand/logo-compact@2x.webp 2x">
    <source media="(max-width:480px)" srcset="/assets/brand/logo-compact.png 1x, /assets/brand/logo-compact@2x.png 2x">
    <source type="image/webp" srcset="/assets/brand/logo.webp 1x, /assets/brand/logo@2x.webp 2x">
    <img src="/assets/brand/logo.png" srcset="/assets/brand/logo.png 1x, /assets/brand/logo@2x.png 2x" alt="{name}" width="{w}" height="48" decoding="async">
  </picture></a>'''.format(name=CFG['name'], w=round(2106*48/254))

NAV = [("Range Rover","/brands/range-rover/"),("Land Rover","/brands/land-rover/"),("Services","/services/"),("Models","/models/"),("About","/about/"),("Blog","/blog/"),("Contact","/contact/")]

def header(current):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if current.startswith(h) and h!="/" else ""}>{t}</a>' for t,h in NAV)
    return f'''
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <div class="hours" aria-label="Opening hours">
    <span class="hours__status" data-hours-status aria-live="polite"><i></i><b>Checking hours…</b></span>
    <span class="hours__days">{I("clock")} Sat – Thu</span>
    <span class="hours__slot">8:00 AM – 1:00 PM</span><span class="hours__amp">&amp;</span><span class="hours__slot">4:00 PM – 9:00 PM</span>
    <span class="hours__closed">Friday closed</span>
  </div>
  <a data-bk-open href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener">{I("wa")} <span>WhatsApp</span> {CFG['phone']}</a>
</div></div>
<header class="header"><div class="wrap">
  {LOGO}
  <nav class="nav" aria-label="Main">{links}</nav>
  <a data-bk-open class="btn btn--wa header__cta" href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener">{I("wa")} <span>Book on</span> WhatsApp</a>
  <button class="burger" data-open-drawer aria-label="Open menu">{I("menu")}</button>
</div></header>
<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer__head">{LOGO}<button class="burger" data-close-drawer aria-label="Close menu">{I("close")}</button></div>
  <nav aria-label="Mobile">{"".join(f'<a href="{h}" data-close-drawer>{t}</a>' for t,h in NAV)}</nav>
  <div class="drawer__foot"><a data-bk-open class="btn btn--wa btn--lg" href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener">{I("wa")} WhatsApp {CFG['phone']}</a><a class="btn btn--ghost" href="tel:+{CFG['phone_intl']}">{I("phone")} Call now</a></div>
</div>'''


def booking_dialog():
    models_by_brand = [("Range Rover",["Range Rover (Vogue)","Range Rover Sport","Range Rover Velar","Range Rover Evoque"]),
                       ("Land Rover",["Defender","Discovery","Discovery Sport","Freelander"]),
                       ("Other brands",["BMW","Mercedes-Benz","Audi","Porsche","Jaguar","Bentley","Rolls-Royce","Other"])]
    vehicle_opts = "".join(f'<optgroup label="{e(b)}">'+"".join(f'<option>{e(m)}</option>' for m in ms)+'</optgroup>' for b,ms in models_by_brand)
    years = "".join(f'<option>{y}</option>' for y in range(datetime.date.today().year+1, 1999, -1))
    svc_groups = [("Servicing & diagnostics",["Periodic Service & Oil Change","Computer Diagnostics","Pre-Purchase Inspection","Battery Replacement"]),
                  ("Engine & drivetrain",["Engine Repair & Rebuild","Timing Chain Replacement","Turbocharger Repair","Gearbox & Transmission","Transfer Case & Differentials","Engine & Gearbox Mounts","Oil Leak Repair","Fuel System & Injectors","Cooling System & Overheating","Exhaust & DPF Cleaning"]),
                  ("Chassis & comfort",["Air Suspension Repair","Brake Service & Repair","Steering & Rack Repair","Wheel Alignment & Tyres","Air Conditioning Service","Electrical & Wiring Repair","Infotainment & Electronics"]),
                  ("Body & appearance",["Body Repair & Paint","Detailing & Ceramic Coating","Off-Road Preparation"]),
                  ("Not sure",["I'm not sure — please advise"])]
    svc_opts = "".join(f'<optgroup label="{e(g)}">'+"".join(f'<option>{e(x)}</option>' for x in xs)+'</optgroup>' for g,xs in svc_groups)
    slots = "".join(f'<label class="bk-chip bk-chip--slot"><input type="radio" name="Time" value="{t}"><span>{t}</span></label>' for t in ["8:00 AM","9:00 AM","10:00 AM","11:00 AM","12:00 PM","4:00 PM","5:00 PM","6:00 PM","7:00 PM","8:00 PM"])
    return f'''
<dialog class="bk" id="bookDialog" aria-labelledby="bkTitle">
 <form class="bk__form" data-booking novalidate>
  <header class="bk__head">
   <div><p class="bk__kicker">{I("wa")} Book on WhatsApp</p><h2 id="bkTitle">Book your service</h2></div>
   <button type="button" class="bk__close" data-bk-close aria-label="Close">{I("close")}</button>
  </header>
  <ol class="bk__steps" role="list"><li data-step-dot="1" class="is-active">Vehicle</li><li data-step-dot="2">Service &amp; time</li><li data-step-dot="3">Your details</li></ol>

  <section class="bk__step is-active" data-step="1">
   <div class="form__row">
    <label class="field">Vehicle<select name="Vehicle" required><option value="" selected disabled>Select your vehicle</option>{vehicle_opts}</select></label>
    <label class="field">Model year<select name="Year" required><option value="" selected disabled>Year</option>{years}</select></label>
   </div>
   <label class="field">Service required<select name="Service" required><option value="" selected disabled>Choose a service</option>{svc_opts}</select></label>
   <label class="field">Plate number (optional)<input name="Plate" type="text" placeholder="e.g. Sharjah 2 12345"></label>
  </section>

  <section class="bk__step" data-step="2">
   <label class="field">Describe the issue or request (optional)<textarea name="Details" placeholder="e.g. rattle on cold start, sinks on the rear left overnight, AC not cold in traffic"></textarea></label>
   <div class="form__row">
    <label class="field">Preferred date<input name="Date" type="date" required></label>
    <div class="field"><span>Preferred time</span><div class="bk__slots">{slots}</div><p class="form__hint" data-hint="time">Please choose a time slot.</p></div>
   </div>
   <p class="bk__hours">{I("clock")} Saturday – Thursday · 8:00 AM – 1:00 PM &amp; 4:00 PM – 9:00 PM · Friday closed</p>
  </section>

  <section class="bk__step" data-step="3">
   <div class="form__row">
    <label class="field">Your name<input name="Name" type="text" required autocomplete="name"></label>
    <label class="field">Mobile number<input name="Phone" type="tel" required autocomplete="tel" placeholder="05x xxx xxxx"></label>
   </div>
   <p class="bk__label">How would you like to bring the car?</p>
   <div class="bk__slots">
    <label class="bk-chip bk-chip--slot"><input type="radio" name="Drop-off" value="I will drive in" checked><span>I will drive in</span></label>
    <label class="bk-chip bk-chip--slot"><input type="radio" name="Drop-off" value="Please collect from me"><span>Collection & delivery</span></label>
    <label class="bk-chip bk-chip--slot"><input type="radio" name="Drop-off" value="Recovery truck needed (car not drivable)"><span>Recovery needed</span></label>
   </div>
   <label class="field" data-address hidden>Collection address<input name="Address" type="text" placeholder="Area, building, landmark"></label>
   <label class="bk-check"><input type="checkbox" name="Waiting" value="Yes"><span>I would like to wait at the workshop while the work is done</span></label>
   <div class="bk__summary" data-summary aria-live="polite"></div>
  </section>

  <footer class="bk__foot">
   <button type="button" class="btn btn--ghost" data-bk-prev hidden>Back</button>
   <span class="bk__spacer"></span>
   <button type="button" class="btn btn--dark" data-bk-next>Continue {I("arrow")}</button>
   <button type="submit" class="btn btn--wa btn--lg" data-bk-send hidden>{I("wa")} Send booking on WhatsApp</button>
  </footer>
  <p class="form__note bk__privacy">Tapping send opens WhatsApp with your booking pre-filled. Nothing is stored on this website.</p>
 </form>
</dialog>'''

def footer():
    svc = "".join(f'<li><a href="/services/{x["slug"]}/">{e(x["name"])}</a></li>' for x in SERVICES[:10])
    mdl = "".join(f'<li><a href="/models/{m["slug"]}/">{e(m["name"])}</a></li>' for m in MODELS)
    brd = "".join(f'<li><a href="/brands/{b["slug"]}/">{e(b["name"])}</a></li>' for b in BRANDS)
    hrs = "".join(f'<div class="ft-hours__row"><span>{e(d.replace("Saturday – Thursday","Sat – Thu"))}</span><span>{e(t)}</span></div>' for d,t in CFG['hours_lines'])
    maps = "https://www.google.com/maps/search/?api=1&query=" + "Al+Rahal+Auto+Maintenance+Workshop+Jabel+Tarek+Street+Sharjah"
    return f'''
<footer class="ft">
 <div class="ft__glow" aria-hidden="true"></div>
 <div class="wrap">
  <div class="ft__top">
   <div class="ft__brand">
    {LOGO}
    <p class="ft__tag">Independent Range Rover &amp; Land Rover specialists in {e(CFG['city'])}. More than 25 years of experience, dealer-level diagnostics and genuine parts, without dealer pricing.</p>
    <span class="hours__status" data-hours-status><i></i><b>Checking hours…</b></span>
    <div class="ft__contact">
     <a data-bk-open href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener" class="ft__contact-row">{I("wa")}<span><small>WhatsApp</small>{e(CFG['phone'])}</span></a>
     <a href="tel:+{CFG['landline_intl']}" class="ft__contact-row">{I("phone")}<span><small>Workshop</small>{e(CFG['landline'])}</span></a>
     <a href="mailto:{CFG['email']}" class="ft__contact-row">{I("mail")}<span><small>Email</small>{CFG['email']}</span></a>
    </div>
   </div>
   <nav class="ft__col" aria-label="Services"><h4>Services</h4><ul role="list">{svc}<li><a class="ft__more" href="/services/">All {len(SERVICES)} services {I("arrow")}</a></li></ul></nav>
   <nav class="ft__col" aria-label="Models and brands"><h4>Models</h4><ul role="list">{mdl}</ul><h4 class="ft__h4-gap">Also serviced</h4><ul role="list" class="ft__inline">{brd}</ul></nav>
   <div class="ft__col ft__visit">
    <h4>Visit the workshop</h4>
    <address class="ft__addr">{I("pin")}<span>{e(CFG['address'])},<br>{e(CFG['city'])}, {e(CFG['country'])}</span></address>
    <a class="btn btn--ghost btn--sm" href="{maps}" target="_blank" rel="noopener">Get directions {I("arrow")}</a>
    <h4 class="ft__h4-gap">Opening hours</h4>
    <div class="ft-hours">{hrs}</div>
   </div>
  </div>
  <div class="ft__cta">
   <div><strong>Ready to book?</strong><span>Three quick steps, straight to our WhatsApp.</span></div>
   <a data-bk-open class="btn btn--wa" href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener">{I("wa")} Book on WhatsApp</a>
  </div>
  <div class="ft__bottom">
   <p>© {TODAY[:4]} {e(CFG['name'])} Workshop. All rights reserved.</p>
   <p class="ft__legal">Independent specialist workshop. Not affiliated with Jaguar Land Rover Limited; vehicle names are used for identification only.</p>
   <ul class="ft__links" role="list"><li><a href="/about/">About</a></li><li><a href="/blog/">Blog</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/gallery/">Gallery</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul>
   <div class="ft__social"><a href="{CFG['instagram']}" aria-label="Instagram" rel="noopener" target="_blank">{I("instagram")}<span>@alrahal_auto_maintenance</span></a></div>
  </div>
 </div>
 <a class="ft__top-link" href="#top" aria-label="Back to top">{I("arrow")}</a>
</footer>
<button class="wa-float" type="button" data-bk-open aria-haspopup="dialog" aria-controls="bookDialog">{I("wa")}<span>Book on WhatsApp</span></button>
{booking_dialog()}
<script src="/assets/js/main.js?v={ASSET_VER}" defer></script>'''

def local_business_schema():
    return {"@context":"https://schema.org","@type":"AutoRepair","@id":CFG['url']+"/#business","name":CFG['name'],"url":CFG['url'],
      "image":CFG['url']+"/assets/brand/hero-home-1870.jpg","logo":CFG['url']+"/assets/brand/logo.png","telephone":["+"+CFG['phone_intl'],"+"+CFG['landline_intl']],"email":CFG['email'],
      "priceRange":"$$",
      "address":{"@type":"PostalAddress","streetAddress":CFG['address'],"addressLocality":CFG['city'],"addressCountry":"AE"},
      "geo":{"@type":"GeoCoordinates","latitude":CFG['lat'],"longitude":CFG['lng']},
      "openingHoursSpecification":[
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"],"opens":"08:00","closes":"13:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"],"opens":"16:00","closes":"21:00"}],"sameAs":[CFG['instagram']],
      "areaServed":CFG['city'],"knowsAbout":["Range Rover repair","Land Rover repair","BMW repair","Mercedes-Benz repair","Audi repair"],
      "makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Service","name":s['name'],"url":f"{CFG['url']}/services/{s['slug']}/"}} for s in SERVICES]}

def page(path, title, desc, body, current="/", schema=None, image="assets/brand/hero-home-1870.jpg", breadcrumbs=None, kind="website"):
    """Write one HTML page. path like 'services/x/' → dist/services/x/index.html"""
    canonical = CFG['url'] + "/" + path
    schemas = [local_business_schema()]
    if breadcrumbs:
        schemas.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":CFG['url']+u} for i,(n,u) in enumerate(breadcrumbs)]})
    if schema: schemas += schema if isinstance(schema, list) else [schema]
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    ga = f'<script async src="https://www.googletagmanager.com/gtag/js?id={CFG["ga_id"]}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{CFG["ga_id"]}");</script>' if CFG['ga_id'] else ""
    stamp = BUILD_STAMP
    doc = f'''<!DOCTYPE html>
<html lang="en" data-wa="{CFG['phone_intl']}">
<head>
<meta charset="utf-8">
<!-- build {stamp} -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#1B1F23">
<meta property="og:type" content="{kind}"><meta property="og:site_name" content="{e(CFG['name'])}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{CFG['url']}/{image}"><meta property="og:locale" content="en_AE">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{CFG['url']}/{image}">
<meta name="geo.region" content="AE"><meta name="geo.placename" content="{e(CFG['city'])}">
<link rel="icon" href="/assets/brand/favicon.ico" sizes="any"><link rel="icon" href="/assets/brand/favicon.svg" type="image/svg+xml"><link rel="icon" href="/assets/brand/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=Manrope:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/css/main.css?v={ASSET_VER}">
{ld}{ga}
</head>
<body id="top">
{header(current)}
<main id="main">
{body}
</main>
{footer()}
</body></html>'''
    d = os.path.join(OUT, path)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f: f.write(doc)
    SITEMAP.append((canonical, "1.0" if path=="" else "0.8"))

# ------------------------------------------------------------------ PARTIALS
def img(src, alt, cls="", loading="lazy"):
    return f'<img src="/{src}" alt="{e(alt)}" class="{cls}" loading="{loading}" decoding="async" data-fallback>'

def crumbs(items):
    return '<ol class="crumbs" role="list">' + "".join(f'<li><a href="{u}">{e(n)}</a></li>' if i < len(items)-1 else f'<li aria-current="page">{e(n)}</li>' for i,(n,u) in enumerate(items)) + '</ol>'

def page_hero(title, lede, bcs, bg):
    return f'''<section class="page-hero"><div class="page-hero__bg">{img(bg, "", loading="eager")}</div><div class="wrap">{crumbs(bcs)}<h1>{title}</h1><p class="lede">{lede}</p>
    <div class="cta-inline"><a data-bk-open class="btn btn--wa btn--lg" href="{wa(f"Hello Al Rahal, I would like to enquire about {re.sub('<[^>]+>','',title)}.")}" target="_blank" rel="noopener">{I("wa")} Book on WhatsApp</a><a class="btn btn--ghost" href="tel:+{CFG['phone_intl']}">{I("phone")} {CFG['phone']}</a></div></div></section>'''

def book_band(h="Book your Range Rover service on WhatsApp", p="Send your model, year, and the issue. An expert will reply within minutes with a clear price and the next available slot."):
    return f'''<section class="book" id="book"><div class="wrap">
  <p class="kicker">Ready when you are</p><h2>{h}</h2><p class="lede">{p}</p>
  <a data-bk-open class="btn btn--wa btn--xl" href="{wa("Hello Al Rahal, I would like to book a service. My car is: ")}" target="_blank" rel="noopener">{I("wa")} Book Now · {CFG['phone']}</a>
  <div class="book__note"><span>{I("check")} Reply within minutes</span><span>{I("check")} Fixed price before work starts</span><span>{I("check")} Collection & delivery available</span></div>
</div></section>'''

def service_card(s):
    return f'''<a class="card" href="/services/{s['slug']}/"><div class="card__media">{img(f"assets/img/services/{s['slug']}.jpg", s['name'] + " for Range Rover")}</div>
    <div class="card__body"><h3>{e(s['name'])}</h3><p>{e(s['short'])}</p><span class="card__link">View service {I("arrow")}</span></div></a>'''

def post_card(p):
    d = datetime.date.fromisoformat(p['date']).strftime("%d %b %Y")
    return f'''<a class="card" href="/blog/{p['slug']}/"><div class="card__media card__media--wide"><span class="card__tag">{e(p['cat'])}</span>{img(f"assets/img/blog/{p['slug']}.jpg", p['title'])}</div>
    <div class="card__body"><span class="meta"><time datetime="{p['date']}">{d}</time><span>{p['read']} min read</span></span><h3>{e(p['title'])}</h3><p>{e(p['excerpt'])}</p><span class="card__link">Read article {I("arrow")}</span></div></a>'''

def faq_block(items, title="Frequently asked questions"):
    det = "".join(f'<details><summary>{e(q)}</summary><div><p>{e(a)}</p></div></details>' for q,a in items)
    schema = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}
    return f'<h2 class="mt-7">{title}</h2><div class="faq mt-6">{det}</div>', schema

def checks(items):
    return '<ul class="checks" role="list">' + "".join(f'<li>{I("check")}<span>{e(i)}</span></li>' for i in items) + '</ul>'

def wa_form(title, fields, service_default=""):
    """fields: list of (label, name, type, options)"""
    out = []
    for label,name,typ,opts in fields:
        if typ == "select":
            o = "".join(f'<option{" selected" if v==service_default else ""}>{e(v)}</option>' for v in opts)
            out.append(f'<label class="field">{label}<select name="{name}" required>{o}</select></label>')
        elif typ == "textarea":
            out.append(f'<label class="field">{label}<textarea name="{name}" placeholder=" "></textarea></label>')
        else:
            out.append(f'<label class="field">{label}<input name="{name}" type="{typ}" placeholder=" " {"required" if typ!="date" else ""}></label>')
    rows = "".join(out)
    return f'''<form class="form" data-wa-form data-wa-title="{e(title)}" novalidate>
 <input type="text" name="website" class="vh" tabindex="-1" autocomplete="off">
 <div class="form__row">{rows}</div>
 <p class="form__hint">Please complete the highlighted fields.</p>
 <button class="btn btn--wa btn--lg" type="submit">{I("wa")} Send via WhatsApp</button>
 <p class="form__note">Tapping the button opens WhatsApp with your details pre-filled. Nothing is stored on this website.</p>
 <p data-sent hidden><strong>Opened WhatsApp.</strong> If it did not open, message us directly on {e(CFG['phone'])}.</p>
</form>'''

SERVICE_NAMES = [s['name'] for s in SERVICES]
MODEL_NAMES = [m['name'] for m in MODELS] + ["BMW","Mercedes-Benz","Audi","Porsche","Jaguar","Other"]
BOOK_FIELDS = [("Your name","Name","text",None),("Phone number","Phone","tel",None),("Vehicle","Vehicle","select",MODEL_NAMES),("Model year","Year","text",None),("Service needed","Service","select",SERVICE_NAMES),("Preferred date","Preferred date","date",None),("Describe the issue","Message","textarea",None)]

# ------------------------------------------------------------------ PAGES
def build_home():
    feat = [s for s in SERVICES if s.get('featured')]
    svc_cards = "".join(service_card(s) for s in feat[:6])
    models = "".join(f'<a class="model" href="/models/{m["slug"]}/">{img(f"assets/img/models/{m["slug"]}.jpg", m["name"])}<h3>{e(m["name"])}</h3><span>{e(m["short"])} · {e(m["years"])}</span><em>View specialist services</em></a>' for m in MODELS[:4])
    brands = "".join(f'<a href="/brands/{b["slug"]}/">{I("car")}<span>{e(b["name"])}</span><small>{"Specialist" if b["primary"] else "Serviced & repaired"}</small></a>' for b in BRANDS)
    _unused = "".join(f'<blockquote class="quote"><span class="stars" aria-label="5 stars">★★★★★</span><p>{e(t)}</p><footer><span>{e(n)}</span><span>{e(c)}</span></footer></blockquote>' for t,n,c in TESTIMONIALS)
    posts = "".join(post_card(p) for p in POSTS[:3])
    faq_html, faq_schema = faq_block(GENERAL_FAQ[:5])
    marquee = "".join(f'<span>{e(s["name"])}<i></i></span>' for s in SERVICES[:12])
    body = f'''
<section class="hero">
 <div class="hero__media">
  <picture>
   <source type="image/webp" srcset="/assets/brand/hero-home-900.webp 900w, /assets/brand/hero-home-1400.webp 1400w, /assets/brand/hero-home-1870.webp 1870w" sizes="100vw">
   <img src="/assets/brand/hero-home-1400.jpg" srcset="/assets/brand/hero-home-900.jpg 900w, /assets/brand/hero-home-1400.jpg 1400w, /assets/brand/hero-home-1870.jpg 1870w" sizes="100vw" alt="Al Rahal Auto Maintenance Workshop in Sharjah at dusk, with Range Rovers parked outside" width="1870" height="841" loading="eager" fetchpriority="high" decoding="async">
  </picture>
 </div>
 <div class="wrap hero__inner">
  <p class="hero__eyebrow"><span class="hero__rule"></span>Independent Range Rover &amp; Land Rover specialists<span class="hero__dot"></span>{e(CFG['city'])}</p>
  <h1 class="hero__title">Your Range Rover, <br><em>cared for</em> by people <br>who know it best.</h1>
  <p class="hero__lede">Dealer-level diagnostics, genuine parts and technicians who have spent their careers inside Land Rover engine bays. Fixed prices, honest advice and every job documented on WhatsApp.</p>
  <div class="hero__actions"><a data-bk-open class="btn btn--wa btn--lg" href="{wa("Hello Al Rahal, I would like to book a service for my Range Rover.")}" target="_blank" rel="noopener">{I("wa")} Book on WhatsApp</a><a class="btn btn--ghost btn--lg" href="/services/">Explore services {I("arrow")}</a></div>
  <a class="hero__scroll" href="#services" aria-label="Scroll to services"><span>Scroll</span><i></i></a>
 </div>
 <div class="hero__marquee"><div class="marquee__track">{marquee}{marquee}</div></div>
</section>

<section class="trust"><div class="wrap">
 <div class="trust__item">{I("award")}<div><strong>25+ years</strong><span>Land Rover experience</span></div></div>
 <div class="trust__item">{I("diagnostics")}<div><strong>Dealer-level</strong><span>Diagnostic equipment</span></div></div>
 <div class="trust__item">{I("shield")}<div><strong>Genuine parts</strong><span>With written warranty</span></div></div>
 <div class="trust__item">{I("wa")}<div><strong>WhatsApp</strong><span>Booking, reports & photos</span></div></div>
</div></section>

<section class="section" id="services"><div class="wrap">
 <div class="section-head reveal"><p class="kicker">Range Rover & Land Rover services</p><h2>Everything a Range Rover needs, under one roof.</h2><p class="lede">From a scheduled service to a full engine rebuild. Tap a service to see what is included, the symptoms to watch for, and the answers owners ask us most.</p></div>
 <div class="grid grid--3 reveal">{svc_cards}</div>
 <div class="cta-inline"><a class="btn btn--dark" href="/services/">View all {len(SERVICES)} services {I("arrow")}</a></div>
</div></section>

{book_band()}

<section class="section section--dark"><div class="wrap">
 <div class="section-head reveal"><p class="kicker">Every generation, every model</p><h2>Vogue, Sport, Velar, Evoque, Defender, Discovery.</h2><p class="lede">Each model has its own known weaknesses. We have dedicated pages for every one, with the faults we see most and how we fix them permanently.</p></div>
 <div class="models reveal">{models}</div>
 <div class="cta-inline"><a class="btn btn--ghost" href="/models/">All models {I("arrow")}</a></div>
</div></section>

<section class="section"><div class="wrap">
 <div class="section-head reveal"><p class="kicker">Why Al Rahal</p><h2>The dealer's tools. A specialist's attention. A neighbour's prices.</h2></div>
 <div class="features reveal">
  <div class="feature">{I("diagnostics")}<h3>Dealer-level diagnostics</h3><p>We run Land Rover's own Pathfinder and SDD platforms, so software updates, coding and guided tests are done exactly as the factory intends.</p></div>
  <div class="feature">{I("wrench")}<h3>Rebuilt in-house</h3><p>Engines, gearboxes, air suspension and transfer cases are rebuilt on our own benches, not sent away. Faster, cheaper and fully accountable.</p></div>
  <div class="feature">{I("shield")}<h3>Genuine parts, written warranty</h3><p>Genuine Land Rover parts by default, high-quality OE alternatives where they make sense, and a warranty term printed on every invoice.</p></div>
  <div class="feature">{I("wa")}<h3>Everything on WhatsApp</h3><p>Booking, diagnostic reports, photos of worn parts and approval for every item of work. You are never surprised by the invoice.</p></div>
  <div class="feature">{I("clock")}<h3>Same-day for common jobs</h3><p>Air struts, brakes, batteries, servicing and diagnostics are usually completed the same day. Collection and delivery available.</p></div>
  <div class="feature">{I("award")}<h3>Trained on Land Rover</h3><p>Our senior technicians are former main-dealer master technicians. They chose to specialise because they love these cars.</p></div>
 </div>
</div></section>

<section class="section section--bone"><div class="wrap">
 <div class="section-head reveal"><p class="kicker">How it works</p><h2>Four steps from message to handover.</h2></div>
 <div class="steps reveal">
  <div class="step"><h3>Message us</h3><p>Send your model, year and symptoms on WhatsApp. We reply within minutes with an initial view and a booking time.</p></div>
  <div class="step"><h3>Diagnose properly</h3><p>Your car goes on the lift and the diagnostic platform. You receive a written report with photos and a fixed price.</p></div>
  <div class="step"><h3>Approve each item</h3><p>Nothing is done without your approval. We show you the worn parts and explain what can wait.</p></div>
  <div class="step"><h3>Collect with confidence</h3><p>Road tested, cleaned, service record updated and warranty documented. Or we deliver it to your door.</p></div>
 </div>
</div></section>

<section class="section"><div class="wrap">
 <div class="section-head reveal"><p class="kicker">Also welcome here</p><h2>Specialists in Land Rover. Experts in the rest.</h2></div>
 <div class="brands reveal">{brands}</div>
</div></section>



<section class="section"><div class="wrap">
 <div class="section-head reveal"><p class="kicker">From the workshop</p><h2>Knowledge that keeps your Range Rover out of the workshop.</h2></div>
 <div class="grid grid--3 reveal">{posts}</div>
 <div class="cta-inline"><a class="btn btn--dark" href="/blog/">Read the blog {I("arrow")}</a></div>
</div></section>

<section class="section section--bone"><div class="wrap"><div class="section-head"><p class="kicker">Good to know</p></div>{faq_html.replace('class="mt-7"','')}<div class="cta-inline"><a class="btn btn--ghost" href="/faq/">More questions answered {I("arrow")}</a></div></div></section>

{book_band("Get a fixed price for your Range Rover today", "One message on WhatsApp is all it takes.")}
'''
    page("", f"Range Rover & Land Rover Specialist in {CFG['city']} | {CFG['name']}",
         f"Independent Range Rover and Land Rover specialists in {CFG['city']}. Dealer-level diagnostics, air suspension, engine, gearbox and servicing with genuine parts. Book on WhatsApp {CFG['phone']}.",
         body, "/", schema=faq_schema)

def build_services_index():
    cards = "".join(service_card(s) for s in SERVICES)
    body = page_hero("Range Rover & Land Rover services", f"{len(SERVICES)} specialist services, each with a dedicated page explaining what is included, the symptoms to watch for and honest answers to the questions owners ask.", [("Home","/"),("Services","/services/")], "assets/img/hero/services-hero.jpg")
    body += f'<section class="section"><div class="wrap"><div class="grid grid--3">{cards}</div></div></section>' + book_band()
    page("services/", f"Range Rover Repair & Service Menu | {CFG['name']} {CFG['city']}", f"All {len(SERVICES)} Range Rover and Land Rover services at Al Rahal: engine, gearbox, air suspension, brakes, diagnostics, AC and more. Fixed prices on WhatsApp.", body, "/services/", breadcrumbs=[("Home","/"),("Services","/services/")], image="assets/img/hero/services-hero.jpg")

VEHICLE_MAP={"range-rover-vogue":"Range Rover (Vogue)","range-rover-sport":"Range Rover Sport","range-rover-velar":"Range Rover Velar","range-rover-evoque":"Range Rover Evoque","land-rover-defender":"Defender","land-rover-discovery":"Discovery","discovery-sport":"Discovery Sport"}
def ctx_tags(service=None, model=None):
    t=""
    if service: t+=f'<span hidden data-page-service="{e(service)}"></span>'
    if model and model['slug'] in VEHICLE_MAP: t+=f'<span hidden data-page-vehicle="{e(VEHICLE_MAP[model["slug"]])}"></span>'
    return t

def service_page(s, m=None):
    """Service page, optionally specialised for a model (programmatic SEO)."""
    slug = f"services/{s['slug']}/" + (f"{m['slug']}/" if m else "")
    car = m['name'] if m else "Range Rover & Land Rover"
    title_h = f"{e(s['name'])} <br>for {e(car)}" if m else f"{e(s['name'])} <br>for Range Rover & Land Rover"
    bcs = [("Home","/"),("Services","/services/"),(s['name'], f"/services/{s['slug']}/")] + ([(m['name'], f"/{slug}")] if m else [])
    intro = "".join(f"<p>{e(p)}</p>" for p in s['intro'])
    model_note = ""
    if m:
        model_note = f'''<h2>{e(s['name'])} on the {e(m['name'])}</h2><p>{e(m['intro'])}</p><p>Engines we cover on this model: {e(m['engines'])}. Production {e(m['years'])} ({e(m['short'])}). Faults we see most often on the {e(m['name'])} include {", ".join(e(x.lower()) for x in m['issues'][:3])}, and each is diagnosed with the model-specific procedure before any parts are recommended.</p>'''
    faq_html, faq_schema = faq_block(s['faqs'])
    related = "".join(f'<li><a href="/services/{x["slug"]}/{m["slug"]+"/" if m else ""}">{e(x["name"])} {I("arrow")}</a></li>' for x in SERVICES if x is not s)[:0] or "".join(f'<li><a href="/services/{x["slug"]}/{(m["slug"]+"/") if m else ""}">{e(x["name"])}<span>›</span></a></li>' for x in SERVICES[:12] if x is not s)
    models_list = "".join(f'<a href="/services/{s["slug"]}/{x["slug"]}/">{e(x["name"])}</a>' for x in MODELS if x is not m)
    body = page_hero(title_h, e(s['short']), bcs, f"assets/img/services/{s['slug']}.jpg")
    body += ctx_tags(s['name'], m) + f'''
<section class="section"><div class="wrap with-aside">
 <article class="prose">
  {intro}
  {model_note}
  <h2>What the service includes</h2>{checks(s['includes'])}
  <h2>Signs you need it</h2>{checks(s['signs'])}
  <h2>How we work</h2>
  <p>Every job begins with a proper diagnosis on the lift and on Land Rover's diagnostic platform. You receive a written report, photos and a fixed price on WhatsApp before any work begins. Genuine or OE-equivalent parts are used, every repair carries a written warranty, and the vehicle is road tested before handover.</p>
  {faq_html}
  <div class="cta-inline"><a data-bk-open class="btn btn--wa btn--lg" href="{wa(f"Hello Al Rahal, I need {s['name']} for my {car}. ")}" target="_blank" rel="noopener">{I("wa")} Get a fixed price on WhatsApp</a></div>
  <h2>This service by model</h2><div class="tags">{models_list}</div>
 </article>
 <aside class="aside">
  <div class="aside__box aside__box--dark"><h3>Book {e(s['name'].lower())}</h3><p>Message us with your model and year. We reply within minutes during working hours.</p><a data-bk-open class="btn btn--wa" href="{wa(f"Hello Al Rahal, I need {s['name']} for my {car}. ")}" target="_blank" rel="noopener">{I("wa")} {CFG['phone']}</a><a class="btn btn--ghost" href="tel:+{CFG['phone_intl']}">{I("phone")} Call</a></div>
  <div class="aside__box"><h3>Other services</h3><ul role="list">{related}</ul><a class="card__link" href="/services/">All services {I("arrow")}</a></div>
 </aside>
</div></section>''' + book_band(f"Book {e(s['name'].lower())} on WhatsApp")
    svc_schema = {"@context":"https://schema.org","@type":"Service","name":f"{s['name']} for {car}","serviceType":s['name'],"provider":{"@id":CFG['url']+"/#business"},"areaServed":CFG['city'],"url":CFG['url']+"/"+slug,"description":s['short']}
    t = f"{s['name']} for {car} in {CFG['city']} | {CFG['name']}"
    page(slug, t[:70] if len(t)<=70 else f"{s['name']} · {car} | {CFG['short']}", f"{s['short']} Specialist {s['name'].lower()} for {car} in {CFG['city']}. Fixed price on WhatsApp {CFG['phone']}.", body, "/services/", schema=[svc_schema, faq_schema], image=f"assets/img/services/{s['slug']}.jpg", breadcrumbs=bcs)

def build_models():
    cards = "".join(f'<a class="model" href="/models/{m["slug"]}/">{img(f"assets/img/models/{m["slug"]}.jpg", m["name"])}<h3>{e(m["name"])}</h3><span>{e(m["short"])} · {e(m["years"])}</span><em>Known issues & services</em></a>' for m in MODELS)
    body = page_hero("Range Rover & Land Rover models we specialise in", "Every model has its own personality and its own weak points. Choose yours for the faults we see most, the engines we cover and the services built around it.", [("Home","/"),("Models","/models/")], "assets/img/hero/models-hero.jpg")
    body += f'<section class="section"><div class="wrap"><div class="models">{cards}</div></div></section>' + book_band()
    page("models/", f"Range Rover & Land Rover Models Serviced | {CFG['name']}", "Specialist servicing and repair for Range Rover Vogue, Sport, Velar, Evoque, Defender, Discovery and Discovery Sport in "+CFG['city']+".", body, "/models/", breadcrumbs=[("Home","/"),("Models","/models/")], image="assets/img/hero/models-hero.jpg")
    for m in MODELS:
        svcs = "".join(f'<a class="card" href="/services/{s["slug"]}/{m["slug"]}/"><div class="card__body"><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="card__link">{e(m["name"])} {e(s["name"].lower())} {I("arrow")}</span></div></a>' for s in SERVICES)
        issues = "".join(f'<li>{I("check")}<span>{e(i)}</span></li>' for i in m['issues'])
        faqs = [(f"How often should a {m['name']} be serviced?", f"Every 16,000 km or 12 months, with an interim oil change at 8,000 km recommended in Gulf conditions for the {m['engines'].split(',')[0]} and other engines fitted to the {m['name']}."),
                (f"What are the most common {m['name']} problems?", f"On the {m['name']} we most often see {', '.join(x.lower() for x in m['issues'][:3])}. All are diagnosed and repaired in-house."),
                (f"Do you use genuine parts on the {m['name']}?", "Yes. Genuine Land Rover parts by default, with high-quality OE-equivalent options offered where they provide better value.")]
        faq_html, faq_schema = faq_block(faqs)
        body = ctx_tags(None, m) + page_hero(f"{e(m['name'])} <br>specialist service & repair", e(m['intro']), [("Home","/"),("Models","/models/"),(m['name'], f"/models/{m['slug']}/")], f"assets/img/models/{m['slug']}.jpg")
        body += f'''<section class="section"><div class="wrap split">
  <div class="prose"><h2>Known issues on the {e(m['name'])}</h2><p>These are the faults that bring {e(m['name'])} owners to us most often. Each has a proven, permanent repair.</p><ul class="checks" role="list">{issues}</ul>
   <p class="mt-6"><strong>Generations:</strong> {e(m['short'])} · <strong>Years:</strong> {e(m['years'])}<br><strong>Engines covered:</strong> {e(m['engines'])}</p>
   <div class="cta-inline"><a data-bk-open class="btn btn--wa btn--lg" href="{wa(f"Hello Al Rahal, I have a {m['name']} and need help with: ")}" target="_blank" rel="noopener">{I("wa")} Book {e(m['name'].split('(')[0].strip())} service</a></div></div>
  <div class="card__media" style="border-radius:var(--radius-lg);aspect-ratio:4/5">{img(f"assets/img/models/{m['slug']}-detail.jpg", m['name']+" in the workshop")}</div>
 </div></section>
 <section class="section section--bone"><div class="wrap"><div class="section-head"><h2>Every service for the {e(m['name'])}</h2></div><div class="grid grid--3">{svcs}</div></div></section>
 <section class="section"><div class="wrap">{faq_html.replace('class="mt-7"','')}</div></section>''' + book_band(f"Book your {e(m['name'].split('(')[0].strip())} on WhatsApp")
        page(f"models/{m['slug']}/", f"{m['name']} Specialist Repair & Service {CFG['city']} | {CFG['short']}", f"{m['name']} servicing, repair and known-issue fixes in {CFG['city']}: {', '.join(m['issues'][:3]).lower()}. Genuine parts, dealer diagnostics. WhatsApp {CFG['phone']}.", body, "/models/", schema=faq_schema, image=f"assets/img/models/{m['slug']}.jpg", breadcrumbs=[("Home","/"),("Models","/models/"),(m['name'], f"/models/{m['slug']}/")])

def build_brands():
    for b in BRANDS:
        models = "".join(f'<a class="model" href="/models/{m["slug"]}/">{img(f"assets/img/models/{m["slug"]}.jpg", m["name"])}<h3>{e(m["name"])}</h3><span>{e(m["short"])}</span><em>Known issues & services</em></a>' for m in MODELS if m['slug'] in b['models'])
        svcs = "".join(f'<a href="/services/{s["slug"]}/">{I(s["icon"])}<div><strong>{e(s["name"])}</strong><span>{e(s["short"][:60])}…</span></div></a>' for s in SERVICES)
        extra = f'<section class="section section--dark"><div class="wrap"><div class="section-head"><h2>{e(b["name"])} models we specialise in</h2></div><div class="models">{models}</div></div></section>' if models else ""
        body = page_hero(f"{e(b['name'])} <br>specialist service & repair in {e(CFG['city'])}", e(b['intro']), [("Home","/"),("Brands","/services/"),(b['name'], f"/brands/{b['slug']}/")], f"assets/img/brands/{b['slug']}.jpg")
        body += extra + f'<section class="section"><div class="wrap cq"><div class="section-head"><h2>Services for {e(b["name"])}</h2></div><div class="service-row">{svcs}</div></div></section>' + book_band(f"Book your {e(b['name'])} on WhatsApp")
        page(f"brands/{b['slug']}/", f"{b['name']} Specialist Garage {CFG['city']} | {CFG['name']}", f"{b['name']} servicing, diagnostics and repair in {CFG['city']} with genuine parts and dealer-level equipment. Fixed prices on WhatsApp {CFG['phone']}.", body, f"/brands/{b['slug']}/", image=f"assets/img/brands/{b['slug']}.jpg", breadcrumbs=[("Home","/"),(b['name'], f"/brands/{b['slug']}/")])

def build_blog():
    cards = "".join(post_card(p) for p in sorted(POSTS, key=lambda p: p['date'], reverse=True))
    body = page_hero("The Al Rahal workshop journal", "Plain-English guides written by our technicians: what fails on Range Rovers, why, and how to prevent it. No jargon, no sales pitch.", [("Home","/"),("Blog","/blog/")], "assets/img/hero/blog-hero.jpg")
    body += f'<section class="section"><div class="wrap"><div class="grid grid--3">{cards}</div></div></section>' + book_band()
    page("blog/", f"Range Rover Maintenance Guides & Advice | {CFG['name']} Blog", "Expert Range Rover and Land Rover maintenance guides from Al Rahal's technicians: air suspension, timing chains, gearboxes, buying advice and summer preparation.", body, "/blog/", image="assets/img/hero/blog-hero.jpg", breadcrumbs=[("Home","/"),("Blog","/blog/")])
    for i,p in enumerate(POSTS):
        d = datetime.date.fromisoformat(p['date']).strftime("%d %B %Y")
        others = [x for x in POSTS if x is not p][:3]
        rel = "".join(post_card(x) for x in others)
        body = f'''<section class="page-hero"><div class="wrap">{crumbs([("Home","/"),("Blog","/blog/"),(p['title'], f"/blog/{p['slug']}/")])}<p class="kicker">{e(p['cat'])}</p><h1>{e(p['title'])}</h1><p class="meta"><time datetime="{p['date']}">{d}</time><span>{p['read']} min read</span><span>By the Al Rahal technical team</span></p></div></section>
<section class="section"><div class="wrap with-aside">
 <article class="prose"><div class="post-hero">{img(f"assets/img/blog/{p['slug']}.jpg", p['title'], loading="eager")}</div>{p['body']}
  <div class="cta-inline"><a class="btn btn--wa btn--lg" href="{wa("Hello Al Rahal, I read your article \"" + p['title'] + "\" and would like advice about my car.")}" target="_blank" rel="noopener">{I("wa")} Ask a technician on WhatsApp</a></div></article>
 <aside class="aside"><div class="aside__box aside__box--dark"><h3>Worried about this on your car?</h3><p>Send a message or a short video of the symptom. We will tell you what to expect before you drive in.</p><a class="btn btn--wa" href="{wa("Hello Al Rahal, I would like advice about my Range Rover.")}" target="_blank" rel="noopener">{I("wa")} {CFG['phone']}</a></div>
  <div class="aside__box"><h3>Related services</h3><ul role="list">{"".join(f'<li><a href="/services/{s["slug"]}/">{e(s["name"])}<span>›</span></a></li>' for s in SERVICES[:8])}</ul></div></aside>
</div></section>
<section class="section section--bone related"><div class="wrap"><h2>Keep reading</h2><div class="grid grid--3 mt-6">{rel}</div></div></section>''' + book_band()
        schema = {"@context":"https://schema.org","@type":"BlogPosting","headline":p['title'],"description":p['excerpt'],"datePublished":p['date'],"dateModified":p['date'],"image":f"{CFG['url']}/assets/img/blog/{p['slug']}.jpg","author":{"@type":"Organization","name":CFG['name']},"publisher":{"@id":CFG['url']+"/#business"},"mainEntityOfPage":f"{CFG['url']}/blog/{p['slug']}/"}
        page(f"blog/{p['slug']}/", f"{p['title']} | {CFG['short']}", p['excerpt'], body, "/blog/", schema=schema, image=f"assets/img/blog/{p['slug']}.jpg", breadcrumbs=[("Home","/"),("Blog","/blog/"),(p['title'], f"/blog/{p['slug']}/")], kind="article")

def build_about():
    body = page_hero("Built by Land Rover technicians, for Land Rover owners", f"For more than {CFG['experience']} years Al Rahal Auto Maintenance Workshop has done one thing exceptionally well: keep Range Rovers and Land Rovers running as their designers intended.", [("Home","/"),("About","/about/")], "assets/img/about/about-hero.jpg")
    body += f'''<section class="section"><div class="wrap split">
 <div class="prose"><p class="kicker">Our story</p><h2>A workshop that grew out of a frustration.</h2>
  <p>Al Rahal Auto Maintenance Workshop was established to serve Land Rover owners to a higher standard of repair than the dealership provides, and at more competitive prices. We carry out all the same repairs and services as the dealer-owned workshops, with the benefits only an independent specialist can offer: honest advice, fair pricing and convenient scheduling.</p>
  <p>Located on Jabel Tarek Street in {e(CFG['city'])}, opposite the Cricket Stadium, our workshop is equipped with dealer-level diagnostic equipment, touchless wheel alignment and camera and radar calibration systems, alongside dedicated bays for engine, gearbox, air suspension, electrical and air-conditioning work.</p>
  <p>Our technicians have spent their careers inside Land Rover engine bays. We are not just the alternative to the dealer; we aim to be the workshop of choice for every Land Rover in the UAE.</p></div>
 <div class="card__media" style="border-radius:var(--radius-lg)">{img("assets/img/about/workshop.jpg", "Al Rahal workshop floor")}</div>
</div></section>
<section class="section section--dark"><div class="wrap"><div class="stats">
 <div class="stat"><strong>{CFG['experience']}</strong><span>Years of Land Rover experience</span></div>
 <div class="stat"><strong>Dealer-level</strong><span>Diagnostics, alignment & ADAS calibration</span></div>
 <div class="stat"><strong>Genuine</strong><span>Parts with written warranty</span></div>
 <div class="stat"><strong>Sat – Thu</strong><span>8 AM – 1 PM & 4 PM – 9 PM</span></div>
</div></div></section>
<section class="section"><div class="wrap split split--rev">
 <div class="prose"><p class="kicker">What we stand for</p><h2>The dealer's tools. A specialist's attention. Fair prices.</h2>
  <ul class="checks" role="list"><li>{I("check")}<span>Every fault diagnosed properly before any part is recommended</span></li><li>{I("check")}<span>A fixed price on WhatsApp before work begins</span></li><li>{I("check")}<span>Genuine Land Rover parts, or high-quality OE alternatives explained and agreed with you</span></li><li>{I("check")}<span>Photos of worn parts and every stage of the repair</span></li><li>{I("check")}<span>Road test and quality check before handover</span></li><li>{I("check")}<span>Written warranty on parts and labour</span></li></ul>
  <div class="cta-inline"><a data-bk-open class="btn btn--wa btn--lg" href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener">{I("wa")} Book on WhatsApp</a></div></div>
 <div class="card__media" style="border-radius:var(--radius-lg);aspect-ratio:4/5">{img("assets/img/about/founders.jpg", "Al Rahal technicians at work")}</div>
</div></section>''' + book_band()
    page("about/", f"About Al Rahal | Range Rover Specialists in {CFG['city']}, {CFG['experience']} Years", f"Al Rahal Auto Maintenance Workshop, {CFG['city']}: more than {CFG['experience']} years of Range Rover and Land Rover service and repair with dealer-level diagnostics and genuine parts.", body, "/about/", image="assets/img/about/about-hero.jpg", breadcrumbs=[("Home","/"),("About","/about/")])

def build_contact():
    card = f'''<div class="bk-card">
  <p class="kicker">Three quick steps</p><h2>Book your service on WhatsApp</h2>
  <p class="lede">Choose your vehicle and service, pick a date and time within our opening hours, add your details, and the booking arrives on our WhatsApp ready to confirm.</p>
  <ol class="bk-card__steps" role="list"><li><strong>Vehicle</strong><span>Model, year & service</span></li><li><strong>Date & time</strong><span>Slots within opening hours</span></li><li><strong>Your details</strong><span>Name, mobile, drop-off</span></li></ol>
  <div class="cta-inline"><a data-bk-open class="btn btn--wa btn--xl" href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener">{I("wa")} Start booking</a><a class="btn btn--ghost" href="{wa("Hello Al Rahal, I have a quick question.")}" target="_blank" rel="noopener">Quick question instead {I("arrow")}</a></div>
  <p class="form__note">Nothing is stored on this website. Your booking is sent directly to {e(CFG['phone'])}.</p>
 </div>'''
    body = page_hero("Contact & book", "Every enquiry goes straight to a technician on WhatsApp. Book in three steps, or call and visit us in Sharjah.", [("Home","/"),("Contact","/contact/")], "assets/img/hero/contact-hero.jpg")
    body += f'''<section class="section"><div class="wrap split">
 {card}
 <div class="contact-info">
  <div>{I("wa")}<div><strong>WhatsApp</strong><a href="{wa("Hello Al Rahal, I would like to book a service.")}" target="_blank" rel="noopener"><span>{e(CFG['phone'])} · tap to chat</span></a></div></div>
  <div>{I("phone")}<div><strong>Phone</strong><a href="tel:+{CFG['phone_intl']}"><span>Mobile +971 55 747 9292</span></a><br><a href="tel:+{CFG['landline_intl']}"><span>Tel +971 6 558 3559</span></a></div></div>
  <div>{I("mail")}<div><strong>Email</strong><a href="mailto:{CFG['email']}"><span>{CFG['email']}</span></a></div></div>
  <div>{I("pin")}<div><strong>Workshop</strong><span>{e(CFG['address'])}, {e(CFG['city'])}, {e(CFG['country'])}</span></div></div>
  <div>{I("clock")}<div><strong>Opening hours</strong><span class="hours-table">{"".join(f'<span class="hours-row"><span>{e(d)}</span><span>{e(t)}</span></span>' for d,t in CFG['hours_lines'])}</span><span class="hours__status hours__status--inline mt-6" data-hours-status><i></i><b>Checking hours…</b></span></div></div>
  <div class="map" style="display:block"><iframe src="{CFG['map_embed']}" title="Map to Al Rahal Auto Maintenance" loading="lazy" allowfullscreen></iframe></div>
 </div>
</div></section>'''
    page("contact/", f"Contact & Book | {CFG['name']} {CFG['city']} · WhatsApp {CFG['phone']}", f"Book your Range Rover or Land Rover service on WhatsApp {CFG['phone']}. Address, hours and map for Al Rahal Auto Maintenance in {CFG['city']}.", body, "/contact/", image="assets/img/hero/contact-hero.jpg", breadcrumbs=[("Home","/"),("Contact","/contact/")])
    body = '<span hidden data-bk-autoopen></span>' + page_hero("Book a service", "Choose your model and the service you need. We confirm a time and a fixed price on WhatsApp.", [("Home","/"),("Book","/book/")], "assets/img/hero/contact-hero.jpg") + f'<section class="section"><div class="wrap" style="max-inline-size:820px">{card}</div></section>'
    page("book/", f"Book a Range Rover Service on WhatsApp | {CFG['short']}", f"Book your Range Rover or Land Rover service in {CFG['city']} in under a minute. Fixed price confirmed on WhatsApp {CFG['phone']}.", body, "/contact/", breadcrumbs=[("Home","/"),("Book","/book/")])

def build_misc():
    faq_html, faq_schema = faq_block(GENERAL_FAQ + [(q,a) for s in SERVICES[:6] for q,a in s['faqs'][:1]], "Everything owners ask us")
    body = page_hero("Frequently asked questions", "Honest answers about servicing, warranty, parts, pricing and booking.", [("Home","/"),("FAQ","/faq/")], "assets/img/hero/services-hero.jpg") + f'<section class="section"><div class="wrap">{faq_html.replace("class=\"mt-7\"","")}</div></section>' + book_band()
    page("faq/", f"Range Rover Servicing FAQ | {CFG['name']}", "Answers to the questions Range Rover and Land Rover owners ask most about servicing, warranty, genuine parts, pricing and booking at Al Rahal.", body, "/faq/", schema=faq_schema, breadcrumbs=[("Home","/"),("FAQ","/faq/")])
    figs = "".join(f'<figure>{img(f"assets/img/gallery/{f}", c)}<figcaption>{e(c)}</figcaption></figure>' for f,c in GALLERY)
    body = page_hero("Inside the workshop", "A look at the facility, the equipment and the work.", [("Home","/"),("Gallery","/gallery/")], "assets/img/hero/models-hero.jpg") + f'<section class="section"><div class="wrap"><div class="gallery">{figs}</div></div></section>' + book_band()
    page("gallery/", f"Workshop Gallery | {CFG['name']}", "Photos from inside Al Rahal Auto Maintenance: Range Rover engine rebuilds, air suspension, diagnostics, detailing and the customer lounge.", body, "/gallery/", breadcrumbs=[("Home","/"),("Gallery","/gallery/")])
    body = page_hero("Privacy policy", "How this website handles your information.", [("Home","/"),("Privacy","/privacy/")], "assets/img/hero/contact-hero.jpg") + f'''<section class="section"><div class="wrap prose"><p>This website does not store personal information. Contact and booking forms open WhatsApp on your device with the details you entered; nothing is saved on our servers. We may use Google Analytics to understand which pages are visited. You can contact us at {CFG['email']} to ask any question about your data.</p><p>Last updated {TODAY}.</p></div></section>'''
    page("privacy/", f"Privacy Policy | {CFG['name']}", "Privacy policy for the Al Rahal Auto Maintenance website.", body, "/privacy/", breadcrumbs=[("Home","/"),("Privacy","/privacy/")])
    # 404
    body = f'<section class="section" style="min-block-size:60dvh;display:grid;place-items:center;text-align:center"><div><p class="kicker">Page not found</p><h1>That page has gone off-road.</h1><p class="lede mt-6">Try the services menu, or message us on WhatsApp and we will point you the right way.</p><div class="cta-inline" style="justify-content:center"><a class="btn btn--dark" href="/services/">All services</a><a class="btn btn--wa" href="{wa("Hello Al Rahal")}" target="_blank" rel="noopener">{I("wa")} WhatsApp</a></div></div></section>'
    page("404/", f"Page not found | {CFG['short']}", "Page not found.", body)
    SITEMAP.pop()  # do not list 404
    shutil.move(os.path.join(OUT,"404","index.html"), os.path.join(OUT,"404.html")); os.rmdir(os.path.join(OUT,"404"))

def build_static():
    assets_src = os.path.join(os.path.dirname(__file__), "assets")
    shutil.copytree(assets_src, os.path.join(OUT, "assets"), dirs_exist_ok=True)
    # favicon / logo svg
    fav = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#1B1F23"/><path d="M14 33 24 11l10 22h-5l-5-11-5 11z" fill="#B59255"/><path d="M17 36h14" stroke="#B59255" stroke-width="3" stroke-linecap="round"/></svg>'
    # robots + sitemap + htaccess
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {CFG['url']}/sitemap.xml\n")
    urls = "".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{p}</priority></url>" for u,p in SITEMAP)
    open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(OUT,".htaccess"),"w").write(HTACCESS)

HTACCESS = r"""# Al Rahal Auto Maintenance — Apache config for Namecheap shared hosting
ErrorDocument 404 /404.html
# Redirects for renamed pages
Redirect 301 /blog/range-rover-service-cost-dubai/ /blog/range-rover-service-cost-sharjah/
Options -Indexes
DirectoryIndex index.html

<IfModule mod_rewrite.c>
RewriteEngine On
# Force HTTPS + www (edit if you use a non-www domain)
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteCond %{HTTP_HOST} ^(?:www\.)?(.+)$ [NC]
RewriteRule ^ https://www.%1%{REQUEST_URI} [R=301,L]
# Add trailing slash to directory URLs
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^(.*[^/])$ /$1/ [R=301,L]
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json image/svg+xml text/xml application/xml
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 1 month"
ExpiresByType application/javascript "access plus 1 month"
ExpiresByType image/jpeg "access plus 1 year"
ExpiresByType image/png "access plus 1 year"
ExpiresByType image/webp "access plus 1 year"
ExpiresByType image/svg+xml "access plus 1 year"
ExpiresByType text/html "access plus 0 seconds"
</IfModule>

<IfModule mod_headers.c>
<FilesMatch "\.(html)$">
Header set Cache-Control "no-cache, must-revalidate"
</FilesMatch>
Header set X-Content-Type-Options "nosniff"
Header set X-Frame-Options "SAMEORIGIN"
Header set Referrer-Policy "strict-origin-when-cross-origin"
Header set Permissions-Policy "geolocation=(), microphone=(), camera=()"
</IfModule>
"""

# ------------------------------------------------------------------ RUN
if __name__ == "__main__":
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_home(); build_services_index()
    for s in SERVICES:
        service_page(s)
        for m in MODELS: service_page(s, m)
    build_models(); build_brands(); build_blog(); build_about(); build_contact(); build_misc()
    build_static()
    n = sum(len(f) for _,_,f in os.walk(OUT) if True)
    print(f"Built {len(SITEMAP)} pages → {OUT}")
