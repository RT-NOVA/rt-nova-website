(() => {
    const root = document.querySelector("[data-tryout-filter]");
    const groups = Array.from(document.querySelectorAll("[data-tryout-group]"));
    const empty = document.querySelector("[data-tryout-empty]");
    const globalPrivateCallout = document.querySelector("[data-private-tryout-global]");
    if (!root || !groups.length) return;

    const ageSelect = root.querySelector("[data-filter-age]");
    const searchInput = root.querySelector("[data-filter-search]");

    const update = () => {
      const selectedAge = ageSelect.value;
      const query = searchInput.value.trim().toLowerCase();
      const isDefaultView = !selectedAge && !query;
      let visibleGroups = 0;
      let privateOnlyCount = 0;
      let postedCount = 0;

      groups.forEach((group) => {
        const hasPosted = group.dataset.hasPosted === "true";
        if (hasPosted) postedCount += 1;
        if (!hasPosted) privateOnlyCount += 1;

        const sessions = Array.from(group.querySelectorAll("[data-tryout-session]"));
        const groupSearch = `${group.dataset.search || ""} ${sessions.map((session) => session.dataset.search || "").join(" ")}`.toLowerCase();
        const ageMatches = !selectedAge || group.dataset.ageGroup === selectedAge;
        const searchMatches = !query || groupSearch.includes(query);

        // Default view: only show age groups with real posted sessions.
        // Filtered view: show the selected/searched age group, including private fallback-only groups.
        const groupVisible = ageMatches && searchMatches && (!isDefaultView || hasPosted);
        group.hidden = !groupVisible;

        sessions.forEach((session) => {
          const kind = session.dataset.sessionKind || "posted";
          session.hidden = !groupVisible || (isDefaultView && kind !== "posted");
        });

        if (groupVisible) visibleGroups += 1;
      });

      if (globalPrivateCallout) {
        // If there are no posted dates at all, the global private notice becomes the main schedule message.
        // If some posted dates exist, it explains that non-listed age groups can request private tryouts.
        globalPrivateCallout.hidden = !isDefaultView || privateOnlyCount === 0;
      }

      if (empty) {
        empty.hidden = visibleGroups !== 0 || (isDefaultView && privateOnlyCount > 0);
      }
    };

    ageSelect.addEventListener("change", update);
    searchInput.addEventListener("input", update);
    update();
  })();
