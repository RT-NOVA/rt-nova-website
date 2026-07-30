(() => {
  const root = document.querySelector("[data-schedule-filter]");
  const list = document.querySelector("[data-schedule-list]");
  const sections = Array.from(document.querySelectorAll("[data-schedule-team-section]"));
  const empty = document.querySelector("[data-schedule-empty]");
  if (!root || !list) return;

  const teamSelect = root.querySelector("[data-filter-team]");
  const teamTabs = Array.from(root.querySelectorAll("[data-filter-team-tab]"));
  const searchInput = root.querySelector("[data-filter-search]");
  const resultCount = root.querySelector("[data-schedule-count]");
  const clearButton = root.querySelector("[data-schedule-clear]");
  let expandedTeam = "";

  const pluralize = (count, singular, plural = `${singular}s`) => `${count} ${count === 1 ? singular : plural}`;

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
    return eventDateKey ? eventDateKey < todayKey : false;
  };

  const hasTeam = (slug) => sections.some((section) => section.dataset.teamSlug === slug);

  const teamFromUrl = () => new URL(window.location.href).searchParams.get("team") || "";

  const updateTeamUrl = (slug) => {
    const url = new URL(window.location.href);
    const existing = url.searchParams.get("team") || "";
    if (existing === slug) return;

    if (slug) {
      url.searchParams.set("team", slug);
    } else {
      url.searchParams.delete("team");
    }

    window.history.pushState({ team: slug }, "", url);
  };

  const syncTeamControls = (slug) => {
    teamTabs.forEach((tab) => {
      const isActive = (tab.dataset.teamValue || "") === slug;
      tab.classList.toggle("is-active", isActive);
      tab.setAttribute("aria-pressed", isActive ? "true" : "false");
    });
  };

  const closePastEvents = () => {
    sections.forEach((section) => {
      const pastDetails = section.querySelector("[data-schedule-past]");
      if (pastDetails) pastDetails.open = false;
    });
  };

  const scrollBelowHeader = (target) => {
    if (!target) return;

    window.requestAnimationFrame(() => {
      const header = document.querySelector("[data-rt-header]");
      const headerHeight = header?.getBoundingClientRect().height || 0;
      const top = target.getBoundingClientRect().top + window.scrollY - headerHeight - 24;
      const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      window.scrollTo({
        top: Math.max(0, top),
        behavior: reduceMotion ? "auto" : "smooth"
      });
    });
  };

  sections.forEach((section) => {
    const events = Array.from(section.querySelectorAll("[data-schedule-event]"));
    const pastContainer = section.querySelector("[data-schedule-past-events]");
    const pastDetails = section.querySelector("[data-schedule-past]");
    const pastCount = section.querySelector("[data-schedule-past-count]");
    const upcomingCount = section.querySelector("[data-schedule-upcoming-count]");
    const nextDate = section.querySelector("[data-schedule-next-date]");
    const nextMonth = section.querySelector("[data-schedule-next-month]");
    const nextDay = section.querySelector("[data-schedule-next-day]");
    const nextType = section.querySelector("[data-schedule-next-type]");
    const nextTitle = section.querySelector("[data-schedule-next-title]");
    const nextMeta = section.querySelector("[data-schedule-next-meta]");

    events.forEach((event) => {
      const past = isPastEvent(event);
      event.dataset.eventStatus = past ? "past" : "upcoming";
      event.classList.toggle("is-past-event", past);
      if (past && pastContainer) pastContainer.appendChild(event);
    });

    const upcoming = events.filter((event) => event.dataset.eventStatus === "upcoming");
    const past = events.filter((event) => event.dataset.eventStatus === "past");

    if (upcomingCount) {
      upcomingCount.textContent = upcoming.length
        ? pluralize(upcoming.length, "upcoming event")
        : "No upcoming events";
    }

    const nextEvent = upcoming[0];
    if (nextEvent) {
      const dateKey = normalizeDateKey(nextEvent.dataset.eventDate);
      const date = dateKey ? new Date(`${dateKey}T12:00:00`) : null;
      const time = nextEvent.dataset.eventTime || "TBD";
      const location = nextEvent.dataset.eventLocation || "TBD";
      const eventType = String(nextEvent.dataset.eventType || "").trim();

      if (nextDate) nextDate.hidden = false;
      if (nextMonth) {
        nextMonth.textContent = date
          ? new Intl.DateTimeFormat("en-US", { month: "short" }).format(date).toUpperCase()
          : "NEXT";
      }
      if (nextDay) {
        nextDay.textContent = date
          ? new Intl.DateTimeFormat("en-US", { day: "numeric" }).format(date)
          : "—";
      }
      if (nextType) {
        nextType.hidden = false;
        nextType.textContent = eventType ? `Up Next · ${eventType}` : "Up Next";
      }
      if (nextTitle) nextTitle.textContent = nextEvent.dataset.eventTitle || "Upcoming event";
      if (nextMeta) nextMeta.textContent = `${time} · ${location}`;
    } else {
      if (nextDate) nextDate.hidden = true;
      if (nextType) {
        nextType.hidden = true;
        nextType.textContent = "";
      }
      if (nextTitle) nextTitle.textContent = "Schedule coming soon";
      if (nextMeta) nextMeta.textContent = "Check back for current-season events.";
    }

    if (pastCount) pastCount.textContent = String(past.length);
    if (pastDetails) pastDetails.hidden = past.length === 0;
  });

  if (!sections.length) {
    if (resultCount) resultCount.textContent = "No current teams are posted.";
    if (empty) empty.hidden = false;
    if (clearButton) clearButton.hidden = true;
    return;
  }

  const update = () => {
    const selectedTeam = teamSelect.value;
    const query = searchInput.value.trim().toLowerCase();
    const hasQuery = query.length > 0;
    let visibleSections = 0;
    let matchingEventCount = 0;
    let upcomingEventCount = 0;
    let focusedTeamName = "";

    syncTeamControls(selectedTeam);

    sections.forEach((section) => {
      const slug = section.dataset.teamSlug || "";
      const teamMatches = !selectedTeam || slug === selectedTeam;
      const sectionMatchesQuery = !hasQuery || (section.dataset.search || "").toLowerCase().includes(query);
      const events = Array.from(section.querySelectorAll("[data-schedule-event]"));
      const upcoming = events.filter((event) => event.dataset.eventStatus === "upcoming");
      const past = events.filter((event) => event.dataset.eventStatus === "past");
      const matchingUpcoming = upcoming.filter((event) => sectionMatchesQuery || (event.dataset.search || "").includes(query));
      const matchingPast = past.filter((event) => sectionMatchesQuery || (event.dataset.search || "").includes(query));
      const sectionHasQueryMatch = sectionMatchesQuery || matchingUpcoming.length > 0 || matchingPast.length > 0;
      const shouldShowSection = teamMatches && (!hasQuery || sectionHasQueryMatch);
      const upcomingHead = section.querySelector("[data-schedule-upcoming-head]");
      const noUpcoming = section.querySelector("[data-schedule-no-upcoming]");
      const noEvents = section.querySelector("[data-schedule-no-events]");
      const pastDetails = section.querySelector("[data-schedule-past]");
      const pastCount = section.querySelector("[data-schedule-past-count]");
      const panel = section.querySelector("[data-schedule-panel]");
      const toggle = section.querySelector("[data-schedule-toggle]");
      const toggleLabel = section.querySelector("[data-schedule-toggle-label]");
      const toggleIcon = section.querySelector(".schedules-team-toggle__icon");
      const isExpanded = shouldShowSection && (
        hasQuery ? sectionHasQueryMatch : expandedTeam === slug
      );

      upcoming.forEach((event) => {
        const matches = !hasQuery || sectionMatchesQuery || (event.dataset.search || "").includes(query);
        event.hidden = !(isExpanded && matches);
      });

      past.forEach((event) => {
        const matches = !hasQuery || sectionMatchesQuery || (event.dataset.search || "").includes(query);
        event.hidden = !(isExpanded && matches);
      });

      const visibleUpcomingCount = hasQuery ? matchingUpcoming.length : upcoming.length;
      const visiblePastCount = hasQuery ? matchingPast.length : past.length;
      const totalEvents = events.length;

      if (panel) panel.hidden = !isExpanded;
      if (upcomingHead) upcomingHead.hidden = !isExpanded || visibleUpcomingCount === 0;
      if (noEvents) noEvents.hidden = !(isExpanded && totalEvents === 0);
      if (noUpcoming) {
        noUpcoming.hidden = !(
          isExpanded &&
          totalEvents > 0 &&
          !hasQuery &&
          upcoming.length === 0
        );
      }

      if (pastDetails) {
        pastDetails.hidden = !isExpanded || visiblePastCount === 0;
        if (pastCount) pastCount.textContent = String(visiblePastCount);

        if (hasQuery && visiblePastCount > 0) {
          pastDetails.open = true;
          pastDetails.dataset.openedForSearch = "true";
        } else if (isExpanded && upcoming.length === 0 && past.length > 0) {
          pastDetails.open = true;
          delete pastDetails.dataset.openedForSearch;
        } else if (!hasQuery && pastDetails.dataset.openedForSearch === "true") {
          pastDetails.open = false;
          delete pastDetails.dataset.openedForSearch;
        }
      }

      if (toggle) {
        toggle.hidden = !shouldShowSection || hasQuery;
        toggle.setAttribute("aria-expanded", isExpanded ? "true" : "false");
      }
      if (toggleLabel) toggleLabel.textContent = isExpanded ? "Hide Schedule" : "View Full Schedule";
      if (toggleIcon) toggleIcon.textContent = isExpanded ? "−" : "+";

      section.hidden = !shouldShowSection;
      section.classList.toggle("is-expanded", isExpanded);

      if (shouldShowSection) {
        visibleSections += 1;
        upcomingEventCount += upcoming.length;
        matchingEventCount += hasQuery ? matchingUpcoming.length + matchingPast.length : 0;
        if (selectedTeam === slug) focusedTeamName = section.dataset.team || "Team";
      }
    });

    if (resultCount) {
      if (hasQuery) {
        resultCount.textContent = `${pluralize(matchingEventCount, "matching event")} across ${pluralize(visibleSections, "team")}`;
      } else if (selectedTeam) {
        resultCount.textContent = `${focusedTeamName} · ${pluralize(upcomingEventCount, "upcoming event")}`;
      } else {
        resultCount.textContent = `${pluralize(visibleSections, "current team")} · ${pluralize(upcomingEventCount, "upcoming event")}`;
      }
    }

    if (clearButton) clearButton.hidden = !selectedTeam && !hasQuery;
    if (empty) empty.hidden = visibleSections !== 0;
  };

  teamSelect.addEventListener("change", () => {
    searchInput.value = "";
    closePastEvents();
    expandedTeam = teamSelect.value;
    updateTeamUrl(teamSelect.value);
    update();
  });

  teamTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      teamSelect.value = tab.dataset.teamValue || "";
      searchInput.value = "";
      closePastEvents();
      expandedTeam = teamSelect.value;
      updateTeamUrl(teamSelect.value);
      update();
    });
  });

  searchInput.addEventListener("input", update);

  sections.forEach((section) => {
    const toggle = section.querySelector("[data-schedule-toggle]");
    if (!toggle) return;

    toggle.addEventListener("click", () => {
      const slug = section.dataset.teamSlug || "";
      const willExpand = expandedTeam !== slug;
      closePastEvents();
      expandedTeam = willExpand ? slug : "";
      update();
      if (willExpand) scrollBelowHeader(section);
    });
  });

  clearButton?.addEventListener("click", () => {
    teamSelect.value = "";
    searchInput.value = "";
    expandedTeam = "";
    closePastEvents();
    updateTeamUrl("");
    update();
    if (window.matchMedia("(max-width: 720px)").matches) {
      teamSelect.focus();
    } else {
      teamTabs[0]?.focus();
    }
  });

  window.addEventListener("popstate", () => {
    const requestedTeam = teamFromUrl();
    closePastEvents();
    teamSelect.value = hasTeam(requestedTeam) ? requestedTeam : "";
    expandedTeam = teamSelect.value;
    searchInput.value = "";
    update();
  });

  const requestedTeam = teamFromUrl();
  teamSelect.value = hasTeam(requestedTeam) ? requestedTeam : "";
  expandedTeam = teamSelect.value;
  update();
})();
