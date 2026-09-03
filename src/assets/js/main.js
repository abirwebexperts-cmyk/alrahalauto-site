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

  /* Sticky header shadow */
  const header = document.querySelector('.header');
  const onScroll = () => header?.classList.toggle('is-stuck', scrollY > 10);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
})();
