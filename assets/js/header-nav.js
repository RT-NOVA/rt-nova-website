(function () {
  function initRtHeaderNav() {
    var header = document.querySelector('[data-rt-header]');
    if (!header || header.dataset.rtHeaderReady === 'true') return;
    header.dataset.rtHeaderReady = 'true';

    var nav = header.querySelector('[data-rt-nav]');
    var mobileToggle = header.querySelector('[data-rt-nav-toggle]');
    var items = Array.prototype.slice.call(header.querySelectorAll('[data-rt-nav-item]'));
    var hoverQuery = window.matchMedia('(hover: hover) and (pointer: fine)');

    function triggerFor(item) {
      return item ? item.querySelector('[data-rt-nav-trigger]') : null;
    }

    function panelFor(item) {
      return item ? item.querySelector('[data-rt-nav-panel]') : null;
    }

    function closeItem(item) {
      var trigger = triggerFor(item);
      var panel = panelFor(item);
      if (!trigger || !panel) return;
      trigger.setAttribute('aria-expanded', 'false');
      panel.hidden = true;
      item.classList.remove('is-open');
    }

    function closeAll(exceptItem) {
      items.forEach(function (item) {
        if (item !== exceptItem) closeItem(item);
      });
    }

    function openItem(item) {
      var trigger = triggerFor(item);
      var panel = panelFor(item);
      if (!trigger || !panel) return;
      closeAll(item);
      trigger.setAttribute('aria-expanded', 'true');
      panel.hidden = false;
      item.classList.add('is-open');
    }

    function toggleItem(item) {
      var trigger = triggerFor(item);
      if (!trigger) return;
      if (trigger.getAttribute('aria-expanded') === 'true') closeItem(item);
      else openItem(item);
    }

    function setMobileNav(open) {
      if (!nav || !mobileToggle) return;
      mobileToggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
      document.documentElement.classList.toggle('rt-nav-lock', open);
      if (!open) closeAll();
    }

    items.forEach(function (item) {
      var trigger = triggerFor(item);
      if (!trigger) return;

      item.addEventListener('mouseenter', function () {
        if (hoverQuery.matches) openItem(item);
      });

      item.addEventListener('mouseleave', function () {
        if (hoverQuery.matches) closeItem(item);
      });

      item.addEventListener('focusin', function () {
        if (hoverQuery.matches) openItem(item);
      });

      trigger.addEventListener('click', function (event) {
        event.preventDefault();
        toggleItem(item);
      });
    });

    if (mobileToggle) {
      mobileToggle.addEventListener('click', function () {
        setMobileNav(mobileToggle.getAttribute('aria-expanded') !== 'true');
      });
    }

    document.addEventListener('click', function (event) {
      if (!header.contains(event.target)) {
        closeAll();
        setMobileNav(false);
      }
    });

    document.addEventListener('focusin', function (event) {
      if (!header.contains(event.target)) closeAll();
    });

    document.addEventListener('keydown', function (event) {
      if (event.key !== 'Escape') return;
      closeAll();
      setMobileNav(false);
      if (mobileToggle && header.contains(document.activeElement)) mobileToggle.focus();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRtHeaderNav);
  } else {
    initRtHeaderNav();
  }
}());
