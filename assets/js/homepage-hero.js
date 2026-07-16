(() => {
  "use strict";

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
