document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#site-nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('is-open', !open);
  });
});


// RT NOVA Team Central: move season toggle into black header
(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    var page = document.querySelector('.rt-team-central, .team-central, [data-page="teams"]');
    if (!page && !/\/teams\/?$/.test(window.location.pathname)) return;

    var toggle = document.querySelector(
      '.rt-season-toggle, .team-season-toggle, .team-central-season-toggle, .rt-team-season-switch, .team-season-switch, [data-team-season-toggle]'
    );

    var header = document.querySelector(
      '.rt-team-season-summary, .rt-team-season-hero, .rt-team-selected-season, .rt-team-dashboard__season, .rt-team-season-dashboard__summary, .team-season-summary, .team-season-hero, .team-selected-season, .team-dashboard__season, .team-season-dashboard__summary'
    );

    if (!toggle || !header || header.contains(toggle)) return;
    header.appendChild(toggle);
    header.classList.add('rt-season-toggle-inline-ready');
  });
}());

