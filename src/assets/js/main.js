/* Al Rahal Auto Maintenance — main.js (no dependencies) */
(() => {
  const WA = document.documentElement.dataset.wa; // set in <html data-wa="971557479292">

  /* Mobile drawer */
  const drawer = document.getElementById('drawer');
  const open = () => { drawer.setAttribute('data-open', ''); document.body.style.overflow = 'hidden'; };
  const close = () => { drawer.removeAttribute('data-open'); document.body.style.overflow = ''; };
  document.querySelectorAll('[data-open-drawer]').forEach(b => b.addEventListener('click', open));
  document.querySelectorAll('[data-close-drawer]').forEach(b => b.addEventListener('click', close));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });

  /* Image fallback: if an image is missing, show a labelled placeholder so the layout never breaks */
  document.querySelectorAll('img[data-fallback]').forEach(img => {
    const show = () => {
      if (img.dataset.done) return; img.dataset.done = 1;
      const box = document.createElement('div');
      box.className = 'img-fallback';
      box.textContent = 'Upload: ' + img.getAttribute('src');
      img.replaceWith(box);
    };
    img.addEventListener('error', show);
    if (img.complete && img.naturalWidth === 0) show();
  });

  /* Reveal (one entrance per section) */
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .12 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  } else document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-in'));

  /* Counters */
  const animate = el => {
    const end = parseFloat(el.dataset.count), suffix = el.dataset.suffix || '', dur = 1400, t0 = performance.now();
    const step = t => { const p = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - p, 3))); el.textContent = v.toLocaleString() + suffix; if (p < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window) {
    const io2 = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { animate(e.target); io2.unobserve(e.target); } }), { threshold: .5 });
    document.querySelectorAll('[data-count]').forEach(el => io2.observe(el));
  }

  /* WhatsApp forms: build a formatted message and open WhatsApp */
  document.querySelectorAll('form[data-wa-form]').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const f = new FormData(form);
      const title = form.dataset.waTitle || 'Enquiry';
      const lines = [`*${title} — Al Rahal Auto Maintenance*`, ''];
      for (const [k, v] of f.entries()) if (v && k !== 'website') lines.push(`*${k}:* ${v}`);
      lines.push('', `Sent from ${location.href}`);
      const url = `https://wa.me/${WA}?text=${encodeURIComponent(lines.join('\n'))}`;
      window.open(url, '_blank', 'noopener');
      form.querySelector('[data-sent]')?.removeAttribute('hidden');
    });
  });

  /* Live opening-hours status (Asia/Dubai). Sat–Thu 08:00–13:00 & 16:00–21:00, Friday closed */
  const statusEls = document.querySelectorAll('[data-hours-status]');
  if (statusEls.length) {
    const fmt = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Dubai', weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: false });
    const update = () => {
      const p = Object.fromEntries(fmt.formatToParts(new Date()).map(x => [x.type, x.value]));
      const day = p.weekday, mins = (+p.hour % 24) * 60 + +p.minute;
      let state, text;
      if (day === 'Fri') { state = 'closed'; text = 'Closed today · Opens Saturday 8:00 AM'; }
      else if (mins < 480) { state = 'closed'; text = 'Closed · Opens today 8:00 AM'; }
      else if (mins < 780) { state = 'open'; text = 'Open now · Until 1:00 PM'; }
      else if (mins < 960) { state = 'break'; text = 'On break · Reopens 4:00 PM'; }
      else if (mins < 1260) { state = 'open'; text = 'Open now · Until 9:00 PM'; }
      else { state = 'closed'; text = day === 'Thu' ? 'Closed · Opens Saturday 8:00 AM' : 'Closed · Opens tomorrow 8:00 AM'; }
      statusEls.forEach(el => { el.dataset.state = state; el.querySelector('b').textContent = text; });
    };
    update(); setInterval(update, 60000);
  }

  /* Booking dialog (3-step) */
  const dlg = document.getElementById('bookDialog');
  if (dlg) {
    const form = dlg.querySelector('[data-booking]');
    const steps = [...form.querySelectorAll('.bk__step')], dots = [...form.querySelectorAll('[data-step-dot]')];
    const prev = form.querySelector('[data-bk-prev]'), next = form.querySelector('[data-bk-next]'), send = form.querySelector('[data-bk-send]');
    const summary = form.querySelector('[data-summary]'), addr = form.querySelector('[data-address]');
    let cur = 0;
    const dateEl = form.querySelector('[name=Date]');
    const today = new Date(); dateEl.min = today.toISOString().slice(0, 10);
    const show = i => {
      cur = i;
      steps.forEach((s, k) => s.classList.toggle('is-active', k === i));
      dots.forEach((d, k) => { d.classList.toggle('is-active', k === i); d.classList.toggle('is-done', k < i); });
      prev.hidden = i === 0; next.hidden = i === steps.length - 1; send.hidden = i !== steps.length - 1;
      if (i === steps.length - 1) renderSummary();
      steps[i].querySelector('input,select,textarea')?.focus({ preventScroll: true });
      dlg.querySelector('.bk__form').scrollTo({ top: 0 });
    };
    const validate = i => {
      let ok = true;
      steps[i].querySelectorAll('[required]').forEach(el => {
        const bad = !el.value || (el.type === 'tel' && !/^\+?[\d\s-]{8,}$/.test(el.value));
        el.closest('.field')?.classList.toggle('is-invalid', bad); if (bad) ok = false;
      });
      if (i === 1) {
        const anySvc = form.querySelectorAll('[name=Service]:checked').length > 0;
        form.querySelector('.bk__services').style.outline = anySvc ? '' : '2px solid var(--danger)';
        const t = form.querySelector('[name=Time]:checked'); form.querySelector('[data-hint=time]').classList.toggle('is-on', !t);
        if (dateEl.value) { const d = new Date(dateEl.value + 'T12:00:00'); if (d.getDay() === 5) { dateEl.closest('.field').classList.add('is-invalid'); dateEl.setCustomValidity('Closed on Friday'); ok = false; } else dateEl.setCustomValidity(''); }
        ok = ok && anySvc && !!t;
      }
      return ok;
    };
    const buildLines = () => {
      const f = new FormData(form), g = k => f.get(k)?.toString().trim() || '';
      const svcs = f.getAll('Service').join(', ');
      const dt = g('Date') ? new Date(g('Date') + 'T12:00:00').toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' }) : '';
      const L = ['*New booking request — Al Rahal Auto Maintenance*', ''];
      L.push(`*Vehicle:* ${g('Vehicle')} ${g('Year')}`.trim());
      if (g('Engine')) L.push(`*Engine:* ${g('Engine')}`);
      if (g('Mileage')) L.push(`*Mileage:* ${g('Mileage')}`);
      if (g('Plate')) L.push(`*Plate:* ${g('Plate')}`);
      L.push(`*Service:* ${svcs}`);
      if (g('Symptoms')) L.push(`*Symptoms:* ${g('Symptoms')}`);
      L.push(`*Preferred:* ${dt} at ${g('Time')}`);
      L.push(`*Name:* ${g('Name')}`, `*Mobile:* ${g('Phone')}`, `*Drop-off:* ${g('Drop-off')}`);
      if (g('Address')) L.push(`*Address:* ${g('Address')}`);
      if (g('Waiting')) L.push('*Waiting at workshop:* Yes');
      L.push('', `Sent from ${location.href}`);
      return L;
    };
    const renderSummary = () => {
      const rows = buildLines().slice(2, -2).map(l => { const m = l.match(/^\*(.+?):\*\s*(.*)$/); return m ? `<b>${m[1]}</b><span>${m[2].replace(/</g,'&lt;') || '—'}</span>` : ''; }).join('');
      summary.innerHTML = `<div>${rows}</div>`;
    };
    form.addEventListener('input', () => { if (cur === steps.length - 1) renderSummary(); });
    document.querySelectorAll('[data-bk-open]').forEach(b => b.addEventListener('click', () => { dlg.showModal(); show(0); }));
    dlg.querySelectorAll('[data-bk-close]').forEach(b => b.addEventListener('click', () => dlg.close()));
    dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
    next.addEventListener('click', () => { if (validate(cur)) show(cur + 1); });
    prev.addEventListener('click', () => show(cur - 1));
    form.querySelectorAll('[name=Drop-off]').forEach(r => r.addEventListener('change', () => { addr.hidden = !/collect/i.test(r.value) && !/Recovery/.test(r.value) ? true : !r.checked; }));
    form.addEventListener('change', e => { if (e.target.name === 'Drop-off') { const v = form.querySelector('[name=Drop-off]:checked').value; addr.hidden = !(/collect|Recovery/.test(v)); } });
    form.addEventListener('submit', e => {
      e.preventDefault(); if (!validate(2)) return;
      window.open(`https://wa.me/${WA}?text=${encodeURIComponent(buildLines().join('\n'))}`, '_blank', 'noopener');
      dlg.close();
    });
    // pre-select service from page context
    const ctx = document.querySelector('[data-page-service]')?.dataset.pageService;
    if (ctx) form.querySelectorAll('[name=Service]').forEach(cb => { if (cb.value === ctx) cb.checked = true; });
  }

  /* Sticky header shadow */
  const header = document.querySelector('.header');
  const onScroll = () => header?.classList.toggle('is-stuck', scrollY > 10);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
})();
