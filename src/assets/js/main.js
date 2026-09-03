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

  /* Sticky header shadow */
  const header = document.querySelector('.header');
  const onScroll = () => header?.classList.toggle('is-stuck', scrollY > 10);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
})();
