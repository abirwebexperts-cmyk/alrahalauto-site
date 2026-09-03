# Al Rahal Auto Maintenance — Website

Pure HTML + modern CSS + vanilla JavaScript. No PHP, no database, no framework.
Hosting: any shared host (built for Namecheap cPanel).

## Folders
- **dist/** → the finished website. Upload the *contents* of this folder to `public_html/`.
- **src/** → the generator and content. Edit here, re-run, re-upload `dist/`.

## Deploy to Namecheap (cPanel)
1. cPanel → File Manager → `public_html` (delete the default files).
2. Upload `dist.zip`, right-click → Extract. Make sure `.htaccess`, `index.html`, `assets/` sit directly inside `public_html`.
   (File Manager → Settings → "Show hidden files" to see `.htaccess`.)
3. Upload your photos following **IMAGE-GUIDE.md**.
4. cPanel → SSL/TLS Status → run AutoSSL so HTTPS works (the .htaccess forces https + www).
5. Google Search Console → add property → submit `https://www.yourdomain.com/sitemap.xml`.
6. Google Business Profile → add the website URL, WhatsApp number 055 747 9292 and the same address.

## Editing content
- Business details (domain, address, hours, email, analytics ID): top of `src/build.py` (CFG).
- Services: `src/data/services.py` — add a dict, get a new service page **plus** 7 model pages automatically.
- Models / brands / blog / FAQ / testimonials / gallery: `src/data/content.py`.
- Design: `src/assets/css/main.css` (colours at the top under `tokens`).
- Rebuild: `cd src && python3 build.py` (Python 3.9+, no packages needed). Then upload `dist/` again.

## SEO built in
Per-page titles & descriptions · canonical · Open Graph / Twitter cards · JSON-LD (AutoRepair LocalBusiness, Service, FAQPage, BlogPosting, BreadcrumbList) · XML sitemap · robots.txt · clean URLs · 229 indexable pages (24 services × 7 models programmatic pages) · lazy-loaded images with alt text · gzip + browser caching + security headers via .htaccess · mobile-first, fast, no heavy libraries.

## Tips for ranking fast
- Upload real photos (Google rewards genuine imagery) and keep them under 400 KB.
- Add one blog post every 1–2 weeks (copy an entry in `content.py`).
- Get 10+ Google reviews mentioning "Range Rover" — then update the rating on the home page.
- Set the real address and city in CFG; the schema and every page description use it.
