(() => {
    const root = document.querySelector("[data-schedule-filter]");
    const sections = Array.from(document.querySelectorAll("[data-schedule-team-section]"));
    const empty = document.querySelector("[data-schedule-empty]");
    if (!root || !sections.length) return;

    const teamSelect = root.querySelector("[data-filter-team]");
    const searchInput = root.querySelector("[data-filter-search]");
    const defaultEventLimit = 3;

    const toDateKey = (date) => {
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");
      return `${year}-${month}-${day}`;
    };

    const todayKey = toDateKey(new Date());

    const normalizeDateKey = (value) => {
      const match = String(value || "").match(/\d{4}-\d{2}-\d{2}/);
      return match ? match[0] : "";
    };

    const isPastEvent = (event) => {
      const eventDateKey = normalizeDateKey(event.dataset.eventDate);
      if (!eventDateKey) return false;
      return eventDateKey < todayKey;
    };

    sections.forEach((section) => {
      Array.from(section.querySelectorAll("[data-schedule-event]")).forEach((event) => {
        event.dataset.eventStatus = isPastEvent(event) ? "past" : "upcoming";
      });
    });

    const teamOrderValue = (team) => {
      const match = String(team || "").match(/^(\d+)/);
      return match ? parseInt(match[1], 10) : -1;
    };

    const sortTeamsOlderFirst = (a, b) => {
      const ageDiff = teamOrderValue(b) - teamOrderValue(a);
      return ageDiff || String(a).localeCompare(String(b), undefined, { numeric: true });
    };

    const currentTeams = Array.from(new Set(sections
      .filter((section) => section.dataset.currentTeam === "true")
      .map((section) => section.dataset.team)
      .filter(Boolean))).sort(sortTeamsOlderFirst);

    currentTeams.forEach((value) => {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = value;
      teamSelect.appendChild(option);
    });

    const list = sections[0].parentElement;
    if (list) {
      sections
        .slice()
        .sort((a, b) => {
          const currentDiff = (b.dataset.currentTeam === "true") - (a.dataset.currentTeam === "true");
          return currentDiff || sortTeamsOlderFirst(a.dataset.team, b.dataset.team);
        })
        .forEach((section) => list.appendChild(section));
    }

    const updateToggle = (section, hiddenCount, expanded, hasQuery) => {
      const toggle = section.querySelector("[data-schedule-toggle]");
      if (!toggle) return;

      if (hasQuery || hiddenCount <= 0) {
        toggle.hidden = true;
        return;
      }

      toggle.hidden = false;
      toggle.setAttribute("aria-expanded", expanded ? "true" : "false");
      toggle.textContent = expanded
        ? "Show fewer events"
        : `Show all ${section.querySelectorAll("[data-schedule-event]").length} events`;
    };

    const update = () => {
      const selectedTeam = teamSelect.value;
      const query = searchInput.value.trim().toLowerCase();
      const hasQuery = query.length > 0;
      let visibleSections = 0;

      sections.forEach((section) => {
        const isCurrent = section.dataset.currentTeam === "true";
        const teamMatches = !selectedTeam || section.dataset.team === selectedTeam;
        const events = Array.from(section.querySelectorAll("[data-schedule-event]"));
        const noUpcoming = section.querySelector("[data-schedule-no-upcoming]");
        const eventSearchText = events.map((event) => event.dataset.search || "").join(" ");
        const sectionSearchText = `${section.dataset.search || ""} ${eventSearchText}`.toLowerCase();
        const sectionMatchesQuery = !hasQuery || sectionSearchText.includes(query);
        const shouldShowSection = teamMatches && (selectedTeam || hasQuery || isCurrent) && sectionMatchesQuery;
        const expanded = section.dataset.expanded === "true";

        let visibleEvents = 0;
        let matchingEvents = 0;
        let matchingUpcomingEvents = 0;
        let hiddenMatchingEvents = 0;

        events.forEach((event) => {
          const eventMatchesQuery = !hasQuery || (event.dataset.search || "").toLowerCase().includes(query);
          const teamNameMatchesQuery = hasQuery && String(section.dataset.team || "").toLowerCase().includes(query);
          const matches = !hasQuery || teamNameMatchesQuery || eventMatchesQuery;
          const isPast = event.dataset.eventStatus === "past";

          event.classList.toggle("is-past-event", isPast);

          if (matches) matchingEvents += 1;
          if (matches && !isPast) matchingUpcomingEvents += 1;

          const upcomingSlot = matches && !isPast && matchingUpcomingEvents <= defaultEventLimit;

          // Default view: show the next 3 upcoming events only.
          // Expanded view: show all matching events, with past events muted.
          // Search view: show all matching events so searches can find history.
          const showEvent = shouldShowSection && matches && (hasQuery || expanded || upcomingSlot);

          event.hidden = !showEvent;
          if (showEvent) visibleEvents += 1;
          if (shouldShowSection && matches && !showEvent) hiddenMatchingEvents += 1;
        });

        const hasEvents = events.length > 0;
        const showNoUpcoming = shouldShowSection && hasEvents && !hasQuery && !expanded && matchingUpcomingEvents === 0;

        if (noUpcoming) noUpcoming.hidden = !showNoUpcoming;

        const showEmptyCurrentTeam = shouldShowSection && !hasEvents;
        const sectionVisible = shouldShowSection && (visibleEvents > 0 || showEmptyCurrentTeam || showNoUpcoming);

        section.hidden = !sectionVisible;
        updateToggle(section, hiddenMatchingEvents, expanded, hasQuery);

        if (sectionVisible) visibleSections += 1;
      });

      if (empty) empty.hidden = visibleSections !== 0;
    };

    sections.forEach((section) => {
      const toggle = section.querySelector("[data-schedule-toggle]");
      if (!toggle) return;

      toggle.addEventListener("click", () => {
        section.dataset.expanded = section.dataset.expanded === "true" ? "false" : "true";
        update();
      });
    });

    teamSelect.addEventListener("change", () => {
      sections.forEach((section) => {
        section.dataset.expanded = "false";
      });
      update();
    });

    searchInput.addEventListener("input", update);
    update();
  })();
