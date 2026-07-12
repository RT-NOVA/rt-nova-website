(() => {
    const buttons = Array.from(document.querySelectorAll("[data-coaches-season-button]"));
    const panels = Array.from(document.querySelectorAll("[data-coaches-season-panel]"));
    if (!buttons.length || !panels.length) return;

    const showSeason = (season) => {
      buttons.forEach((button) => {
        const active = button.dataset.coachesSeasonButton === season;
        button.classList.toggle("is-active", active);
        button.setAttribute("aria-pressed", active ? "true" : "false");
      });

      panels.forEach((panel) => {
        panel.hidden = panel.dataset.coachesSeasonPanel !== season;
      });
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => showSeason(button.dataset.coachesSeasonButton));
    });
  })();

(() => {
    const modal = document.querySelector("[data-coach-photo-modal]");
    if (!modal) return;

    const image = modal.querySelector("[data-coach-photo-modal-image]");
    const name = modal.querySelector("[data-coach-photo-modal-name]");
    const role = modal.querySelector("[data-coach-photo-modal-role]");
    const closeButtons = modal.querySelectorAll("[data-coach-photo-close]");
    let lastTrigger = null;

    const openModal = (trigger) => {
      const src = trigger.getAttribute("data-coach-photo");
      const coachName = trigger.getAttribute("data-coach-name") || "Coach";
      const coachRole = trigger.getAttribute("data-coach-role") || "";
      if (!src) return;

      lastTrigger = trigger;
      image.src = src;
      image.alt = coachName;
      name.textContent = coachName;
      role.textContent = coachRole;
      modal.hidden = false;
      document.documentElement.classList.add("rt-coach-photo-modal-open");

      const closeButton = modal.querySelector(".rt-coach-photo-modal__close");
      if (closeButton) closeButton.focus({ preventScroll: true });
    };

    const closeModal = () => {
      if (modal.hidden) return;
      modal.hidden = true;
      image.removeAttribute("src");
      image.alt = "";
      document.documentElement.classList.remove("rt-coach-photo-modal-open");
      if (lastTrigger) lastTrigger.focus({ preventScroll: true });
    };

    document.addEventListener("click", (event) => {
      const trigger = event.target.closest("[data-coach-photo]");
      if (!trigger) return;
      event.preventDefault();
      event.stopPropagation();
      openModal(trigger);
    });

    closeButtons.forEach((button) => {
      button.addEventListener("click", closeModal);
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeModal();
    });
  })();
