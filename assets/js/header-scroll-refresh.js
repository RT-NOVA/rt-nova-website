(function () {
  function initScrollHeader() {
    var header = document.querySelector('[data-rt-scroll-header]');
    if (!header || header.dataset.rtScrollReady === 'true') return;
    header.dataset.rtScrollReady = 'true';

    var nav = header.querySelector('[data-rt-nav]');
    var toggle = header.querySelector('[data-rt-nav-toggle]');
    var scrolledAt = 14;

    function syncScrolledState() {
      header.classList.toggle('is-scrolled', window.scrollY > scrolledAt);
      header.classList.toggle('is-nav-open', !!(nav && nav.classList.contains('is-open')));
    }

    syncScrolledState();
    window.addEventListener('scroll', syncScrolledState, { passive: true });
    window.addEventListener('resize', syncScrolledState);

    if (toggle) {
      toggle.addEventListener('click', function () {
        window.setTimeout(syncScrolledState, 0);
      });
    }

    document.addEventListener('click', function () {
      window.setTimeout(syncScrolledState, 0);
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') window.setTimeout(syncScrolledState, 0);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollHeader);
  } else {
    initScrollHeader();
  }
}());
