(() => {
  const root = document.querySelector("[data-schedule-filter]");
  const list = document.querySelector("[data-schedule-list]");
  const sections = Array.from(document.querySelectorAll("[data-schedule-team-section]"));
  const empty = document.querySelector("[data-schedule-empty]");
  const spotlight = document.querySelector("[data-schedule-spotlight]");
  const spotlightList = document.querySelector("[data-schedule-spotlight-list]");
  if (!root || !list) return;

  const teamSelect = root.querySelector("[data-filter-team]");
  const teamTabs = Array.from(root.querySelectorAll("[data-filter-team-tab]"));
  const teamCardLinks = Array.from(document.querySelectorAll("[data-filter-team-card]"));
  const viewButtons = Array.from(root.querySelectorAll("[data-filter-view]"));
  const searchInput = root.querySelector("[data-filter-search]");
  const resultCount = root.querySelector("[data-schedule-count]");
  const clearButton = root.querySelector("[data-schedule-clear]");
  let expandedTeam = "";
  let selectedView = "all";

  const pluralize = (count, singular, plural = `${singular}s`) => `${count} ${count === 1 ? singular : plural}`;

  const toDateKey = (date) => {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    return `${year}-${month}-${day}`;
  };

  const normalizeDateKey = (value) => {
    const match = String(value || "").match(/\d{4}-\d{2}-\d{2}/);
    return match ? match[0] : "";
  };

  const dateFromKey = (value) => {
    const key = normalizeDateKey(value);
    return key ? new Date(`${key}T12:00:00`) : null;
  };

  const today = new Date();
  const todayKey = toDateKey(today);
  const daysUntilSaturday = (6 - today.getDay() + 7) % 7;
  const weekendOffset = today.getDay() === 0 ? -1 : daysUntilSaturday;
  const weekendStart = new Date(today.getFullYear(), today.getMonth(), today.getDate() + weekendOffset, 12);
  const weekendEnd = new Date(weekendStart);
  weekendEnd.setDate(weekendStart.getDate() + 1);
  const weekendStartKey = toDateKey(weekendStart);
  const weekendEndKey = toDateKey(weekendEnd);

  const eventRange = (event) => {
    const start = normalizeDateKey(event.dataset.eventDate);
    const rawEnd = normalizeDateKey(event.dataset.eventEndDate) || start;
    return { start, end: rawEnd < start ? start : rawEnd };
  };

  const isCurrentEvent = (event) => {
    const { start, end } = eventRange(event);
    return Boolean(start && start <= todayKey && end >= todayKey);
  };

  const isPastEvent = (event) => {
    const { end } = eventRange(event);
    return Boolean(end && end < todayKey);
  };

  const isWeekendEvent = (event) => {
    const { start, end } = eventRange(event);
    return Boolean(start && start <= weekendEndKey && end >= weekendStartKey);
  };

  const eventStatus = (event) => {
    const { start, end } = eventRange(event);
    const multiDay = start && end && start !== end;

    if (isPastEvent(event)) return { key: "completed", label: "Completed" };
    if (isCurrentEvent(event)) {
      if (multiDay && end === todayKey) return { key: "final-day", label: "Final Day" };
      if (multiDay) return { key: "in-progress", label: "In Progress" };
      return { key: "today", label: "Today" };
    }
    if (isWeekendEvent(event)) return { key: "this-weekend", label: "This Weekend" };
    return { key: "upcoming", label: "Upcoming" };
  };

  const eventMatchesView = (event, view) => {
    if (view === "now") return isCurrentEvent(event);
    if (view === "weekend") return !isPastEvent(event) && isWeekendEvent(event);

    const type = String(event.dataset.eventType || "").toLowerCase();
    if (view === "tournament") return type.includes("tournament");
    if (view === "game") return type.includes("game");
    return true;
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

  const syncViewControls = () => {
    viewButtons.forEach((button) => {
      const isActive = (button.dataset.viewValue || "all") === selectedView;
      button.classList.toggle("is-active", isActive);
      button.setAttribute("aria-pressed", isActive ? "true" : "false");
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

  const selectTeam = (slug, shouldScroll = false) => {
    if (!hasTeam(slug)) return;
    teamSelect.value = slug;
    searchInput.value = "";
    closePastEvents();
    expandedTeam = slug;
    updateTeamUrl(slug);
    update();
    if (shouldScroll) {
      scrollBelowHeader(sections.find((section) => section.dataset.teamSlug === slug));
    }
  };

  const createSpotlightCard = (event) => {
    const card = document.createElement("article");
    const status = eventStatus(event);
    card.className = `schedules-spotlight-card is-${status.key}`;

    const topline = document.createElement("div");
    topline.className = "schedules-spotlight-card__topline";
    const slug = event.dataset.eventTeamSlug || "";
    const team = document.createElement("a");
    team.href = `?team=${encodeURIComponent(slug)}#team-${slug}`;
    team.textContent = event.dataset.eventTeam || "Team";
    team.addEventListener("click", (clickEvent) => {
      clickEvent.preventDefault();
      selectTeam(slug, true);
    });
    const badge = document.createElement("strong");
    badge.className = "schedules-event-status";
    badge.textContent = status.label;
    topline.append(team, badge);

    const title = document.createElement("h3");
    title.textContent = event.dataset.eventTitle || "Schedule Event";
    const date = document.createElement("p");
    date.textContent = event.dataset.eventDateLabel || "Date TBD";
    const meta = document.createElement("p");
    meta.className = "schedules-spotlight-card__meta";
    meta.textContent = `${event.dataset.eventTime || "TBD"} · ${event.dataset.eventLocation || "TBD"}`;

    const links = document.createElement("div");
    links.className = "schedules-spotlight-card__links";
    event
      .querySelectorAll("[data-event-resource-links] a:not([data-event-team-link])")
      .forEach((link) => links.appendChild(link.cloneNode(true)));

    card.append(topline, title, date, meta);
    if (links.childElementCount) card.append(links);
    return card;
  };

  const renderSpotlight = () => {
    if (!spotlight || !spotlightList) return;

    const events = Array.from(document.querySelectorAll("[data-schedule-event]"))
      .filter((event) => !isPastEvent(event) && (isCurrentEvent(event) || isWeekendEvent(event)))
      .sort((left, right) => {
        const currentDifference = Number(isCurrentEvent(right)) - Number(isCurrentEvent(left));
        return currentDifference || eventRange(left).start.localeCompare(eventRange(right).start);
      });

    spotlightList.replaceChildren(...events.map(createSpotlightCard));
    spotlight.dataset.eventCount = String(events.length);
    spotlight.hidden = events.length === 0;
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
      const status = eventStatus(event);
      const past = status.key === "completed";
      event.dataset.eventStatus = past ? "past" : "upcoming";
      event.dataset.eventState = status.key;
      event.classList.toggle("is-past-event", past);
      event.classList.toggle("is-current-event", isCurrentEvent(event));
      const statusLabel = event.querySelector("[data-event-status-label]");
      if (statusLabel) statusLabel.textContent = status.label;
      if (past && pastContainer) pastContainer.appendChild(event);
    });

    const upcoming = events.filter((event) => event.dataset.eventStatus === "upcoming");
    const past = events.filter((event) => event.dataset.eventStatus === "past");

    if (upcomingCount) {
      upcomingCount.textContent = upcoming.length
        ? pluralize(upcoming.length, "current / upcoming event")
        : "No current events";
    }

    const nextEvent = upcoming[0];
    if (nextEvent) {
      const date = dateFromKey(nextEvent.dataset.eventDate);
      const time = nextEvent.dataset.eventTime || "TBD";
      const location = nextEvent.dataset.eventLocation || "TBD";
      const eventType = String(nextEvent.dataset.eventType || "").trim();
      const status = eventStatus(nextEvent);

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
        nextType.textContent = `${status.label}${eventType ? ` · ${eventType}` : ""}`;
      }
      if (nextTitle) nextTitle.textContent = nextEvent.dataset.eventTitle || "Upcoming event";
      if (nextMeta) nextMeta.textContent = `${nextEvent.dataset.eventDateLabel || "Date TBD"} · ${time} · ${location}`;
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

  renderSpotlight();

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
    const hasViewFilter = selectedView !== "all";
    let visibleSections = 0;
    let matchingEventCount = 0;
    let currentEventCount = 0;
    let focusedTeamName = "";

    syncTeamControls(selectedTeam);
    syncViewControls();

    sections.forEach((section) => {
      const slug = section.dataset.teamSlug || "";
      const teamMatches = !selectedTeam || slug === selectedTeam;
      const sectionMatchesQuery = !hasQuery || (section.dataset.search || "").toLowerCase().includes(query);
      const events = Array.from(section.querySelectorAll("[data-schedule-event]"));
      const upcoming = events.filter((event) => event.dataset.eventStatus === "upcoming");
      const past = events.filter((event) => event.dataset.eventStatus === "past");
      const matches = (event) => {
        const queryMatches = !hasQuery || sectionMatchesQuery || (event.dataset.search || "").includes(query);
        return queryMatches && eventMatchesView(event, selectedView);
      };
      const matchingUpcoming = upcoming.filter(matches);
      const matchingPast = past.filter(matches);
      const sectionHasMatch = matchingUpcoming.length > 0 || matchingPast.length > 0 || (hasQuery && sectionMatchesQuery && !hasViewFilter);
      const preserveSelectedTeam = Boolean(selectedTeam && teamMatches);
      const shouldShowSection = teamMatches && ((!hasQuery && !hasViewFilter) || sectionHasMatch || preserveSelectedTeam);
      const upcomingHead = section.querySelector("[data-schedule-upcoming-head]");
      const noUpcoming = section.querySelector("[data-schedule-no-upcoming]");
      const noEvents = section.querySelector("[data-schedule-no-events]");
      const pastDetails = section.querySelector("[data-schedule-past]");
      const pastCount = section.querySelector("[data-schedule-past-count]");
      const panel = section.querySelector("[data-schedule-panel]");
      const toggle = section.querySelector("[data-schedule-toggle]");
      const toggleLabel = section.querySelector("[data-schedule-toggle-label]");
      const toggleIcon = section.querySelector(".schedules-team-toggle__icon");
      const filteredView = hasQuery || hasViewFilter;
      const isExpanded = shouldShowSection && (filteredView || expandedTeam === slug);

      upcoming.forEach((event) => {
        event.hidden = !(isExpanded && (!filteredView || matches(event)));
      });

      past.forEach((event) => {
        event.hidden = !(isExpanded && (!filteredView || matches(event)));
      });

      const visibleUpcomingCount = filteredView ? matchingUpcoming.length : upcoming.length;
      const visiblePastCount = filteredView ? matchingPast.length : past.length;
      const totalEvents = events.length;

      if (panel) panel.hidden = !isExpanded;
      if (upcomingHead) upcomingHead.hidden = !isExpanded || visibleUpcomingCount === 0;
      if (noEvents) noEvents.hidden = !(isExpanded && totalEvents === 0);
      if (noUpcoming) {
        noUpcoming.hidden = !(isExpanded && totalEvents > 0 && visibleUpcomingCount === 0);
        noUpcoming.textContent = filteredView ? "No current events match this view." : "No upcoming events currently posted.";
      }

      if (pastDetails) {
        pastDetails.hidden = !isExpanded || visiblePastCount === 0;
        if (pastCount) pastCount.textContent = String(visiblePastCount);

        if (hasQuery && visiblePastCount > 0) {
          pastDetails.open = true;
          pastDetails.dataset.openedForSearch = "true";
        } else if (!filteredView && isExpanded && upcoming.length === 0 && past.length > 0) {
          pastDetails.open = true;
          delete pastDetails.dataset.openedForSearch;
        } else if (!hasQuery && pastDetails.dataset.openedForSearch === "true") {
          pastDetails.open = false;
          delete pastDetails.dataset.openedForSearch;
        }
      }

      if (toggle) {
        toggle.hidden = !shouldShowSection || filteredView;
        toggle.setAttribute("aria-expanded", isExpanded ? "true" : "false");
      }
      if (toggleLabel) toggleLabel.textContent = isExpanded ? "Hide Schedule" : "View Full Schedule";
      if (toggleIcon) toggleIcon.textContent = isExpanded ? "−" : "+";

      section.hidden = !shouldShowSection;
      section.classList.toggle("is-expanded", isExpanded);

      if (shouldShowSection) {
        visibleSections += 1;
        currentEventCount += visibleUpcomingCount;
        matchingEventCount += visibleUpcomingCount + visiblePastCount;
        if (selectedTeam === slug) focusedTeamName = section.dataset.team || "Team";
      }
    });

    if (resultCount) {
      if (hasQuery || hasViewFilter) {
        resultCount.textContent = `${pluralize(matchingEventCount, "matching event")} across ${pluralize(visibleSections, "team")}`;
      } else if (selectedTeam) {
        resultCount.textContent = `${focusedTeamName} · ${pluralize(currentEventCount, "current / upcoming event")}`;
      } else {
        resultCount.textContent = `${pluralize(visibleSections, "current team")} · ${pluralize(currentEventCount, "current / upcoming event")}`;
      }
    }

    if (clearButton) clearButton.hidden = !selectedTeam && !hasQuery && !hasViewFilter;
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
      const slug = tab.dataset.teamValue || "";
      if (slug) {
        selectTeam(slug);
      } else {
        teamSelect.value = "";
        searchInput.value = "";
        closePastEvents();
        expandedTeam = "";
        updateTeamUrl("");
        update();
      }
    });
  });

  teamCardLinks.forEach((link) => {
    link.addEventListener("click", (clickEvent) => {
      clickEvent.preventDefault();
      selectTeam(link.dataset.teamValue || "", true);
    });
  });

  viewButtons.forEach((button) => {
    button.addEventListener("click", () => {
      selectedView = button.dataset.viewValue || "all";
      closePastEvents();
      expandedTeam = selectedView === "all" ? teamSelect.value : "";
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
    selectedView = "all";
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
    selectedView = "all";
    update();
  });

  const requestedTeam = teamFromUrl();
  teamSelect.value = hasTeam(requestedTeam) ? requestedTeam : "";
  expandedTeam = teamSelect.value;
  update();
})();
