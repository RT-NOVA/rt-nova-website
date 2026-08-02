(() => {
  "use strict";

  document.querySelectorAll("[data-random-achievement]").forEach((gallery) => {
    const items = Array.from(gallery.querySelectorAll("[data-random-achievement-item]"));

    if (!items.length) return;

    const requestedInterval = Number.parseInt(gallery.dataset.randomAchievementInterval, 10);
    const interval = Number.isFinite(requestedInterval) ? Math.max(requestedInterval, 1000) : 0;
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let currentIndex = 0;
    let timer = null;
    let pointerInside = false;

    const showItem = (index) => {
      currentIndex = (index + items.length) % items.length;
      items.forEach((item, itemIndex) => {
        const isCurrent = itemIndex === currentIndex;
        item.classList.toggle("is-primary", isCurrent);
        item.setAttribute("aria-hidden", String(!isCurrent));
        if (isCurrent) {
          item.removeAttribute("tabindex");
        } else {
          item.setAttribute("tabindex", "-1");
        }
      });
    };

    const stopTimer = () => {
      window.clearInterval(timer);
      timer = null;
    };

    const startTimer = () => {
      stopTimer();
      if (items.length < 2 || !interval || reducedMotion || pointerInside || document.hidden) return;
      timer = window.setInterval(() => showItem(currentIndex + 1), interval);
    };

    gallery.addEventListener("mouseenter", () => {
      pointerInside = true;
      stopTimer();
    });

    gallery.addEventListener("mouseleave", () => {
      pointerInside = false;
      startTimer();
    });

    document.addEventListener("visibilitychange", startTimer);

    items.forEach((item) => {
      item.hidden = false;
    });
    showItem(currentIndex);
    startTimer();
  });

  document.querySelectorAll("[data-home-hero]").forEach((hero) => {
    const slides = Array.from(hero.querySelectorAll("[data-home-hero-slide]"));

    if (slides.length < 2) return;

    const requestedInterval = Number.parseInt(hero.dataset.homeHeroInterval, 10);
    const interval = Number.isFinite(requestedInterval) ? Math.max(requestedInterval, 1000) : 6000;
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let currentIndex = Math.max(0, slides.findIndex((slide) => slide.classList.contains("is-active")));
    let timer = null;
    let pointerInside = false;

    const stopTimer = () => {
      window.clearInterval(timer);
      timer = null;
    };

    const showSlide = (index) => {
      currentIndex = (index + slides.length) % slides.length;

      slides.forEach((slide, slideIndex) => {
        slide.classList.toggle("is-active", slideIndex === currentIndex);
      });
    };

    const startTimer = () => {
      stopTimer();
      if (reducedMotion || pointerInside || document.hidden) return;
      timer = window.setInterval(() => showSlide(currentIndex + 1), interval);
    };

    hero.addEventListener("mouseenter", () => {
      pointerInside = true;
      stopTimer();
    });

    hero.addEventListener("mouseleave", () => {
      pointerInside = false;
      startTimer();
    });

    document.addEventListener("visibilitychange", startTimer);

    startTimer();
  });
})();
