(function () {
  function initRtHeaderNav() {
    var header = document.querySelector('[data-rt-header]');
    if (!header || header.dataset.rtHeaderReady === 'true') return;
    header.dataset.rtHeaderReady = 'true';

    var root = document.documentElement;
    var nav = header.querySelector('[data-rt-nav]');
    var mobileToggle = header.querySelector('[data-rt-nav-toggle]');
    var items = Array.prototype.slice.call(header.querySelectorAll('[data-rt-nav-item]'));
    var hoverQuery = window.matchMedia('(hover: hover) and (pointer: fine)');

    function firstMainElement() {
      var main = document.querySelector('main');
      if (!main) return null;
      for (var i = 0; i < main.children.length; i += 1) {
        var child = main.children[i];
        if (child && child.nodeType === 1) return child;
      }
      return null;
    }

    function normalizedPathname() {
      var path = window.location.pathname || '/';
      path = path.replace(/\/+/g, '/');
      if (path.length > 1 && path.charAt(path.length - 1) !== '/') path += '/';
      return path;
    }

    function pagePathUsesOverlayHeroHeader() {
      var path = normalizedPathname();
      var overlayHeroPaths = [
        '/',
        '/about/',
        '/teams/',
        '/become-a-tiger/',
        '/coaching-opportunities/',
        '/tryouts/',
        '/accolades/',
        '/coaches/',
        '/schedules/',
        '/watch-now/',
        '/training-locations/',
        '/family-hub/',
        '/booster-club/',
        '/sponsors/',
        '/sponsorship-opportunities/'
      ];
      return overlayHeroPaths.indexOf(path) !== -1;
    }

    function pageHasHero() {
      var first = firstMainElement();
      if (pagePathUsesOverlayHeroHeader()) return true;
      if (!first) return false;
      if (first.matches('[data-hero], [data-page-hero], .home-hero, .page-hero, .section-hero, .hero, .inner-hero, .interior-hero, .subpage-hero, .page-header, .page-masthead, .masthead, .cover')) return true;
      var className = String(first.className || '').toLowerCase();
      return className.indexOf('hero') !== -1 || className.indexOf('masthead') !== -1;
    }

    function updateHeaderState() {
      var forcedHeroHeader = pagePathUsesOverlayHeroHeader();
      var hasHero = pageHasHero();
      root.classList.toggle('rt-has-hero', hasHero);
      root.classList.toggle('rt-no-hero', !hasHero);
      root.classList.toggle('rt-force-hero-header', forcedHeroHeader);
      root.classList.toggle('rt-home-page', normalizedPathname() === '/');
      header.classList.toggle('is-scrolled', window.scrollY > 36 || !hasHero);
    }

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
      root.classList.toggle('rt-nav-lock', open);
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

    updateHeaderState();
    window.addEventListener('scroll', updateHeaderState, { passive: true });
    window.addEventListener('resize', updateHeaderState);
    window.addEventListener('load', updateHeaderState);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRtHeaderNav);
  } else {
    initRtHeaderNav();
  }
}());
