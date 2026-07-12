(() => {
    const wall = document.querySelector("[data-banner-wall]");
    const cards = Array.from(document.querySelectorAll("[data-banner-card]"));
    const prev = document.querySelector("[data-banner-prev]");
    const next = document.querySelector("[data-banner-next]");
    const status = document.querySelector("[data-banner-status]");
    const perPage = 3;
    let page = 0;

    if (cards.length && wall) {
      const render = () => {
        const pageCount = Math.max(1, Math.ceil(cards.length / perPage));
        page = ((page % pageCount) + pageCount) % pageCount;
        const start = page * perPage;
        const end = Math.min(start + perPage, cards.length);
        const visibleCount = end - start;

        cards.forEach((card, index) => {
          card.hidden = !(index >= start && index < end);
        });

        wall.setAttribute("data-visible-count", String(visibleCount));
        if (status) status.textContent = `Showing ${start + 1}–${end} of ${cards.length}`;
        if (prev) prev.disabled = cards.length <= perPage;
        if (next) next.disabled = cards.length <= perPage;
      };

      if (prev) prev.addEventListener("click", () => { page -= 1; render(); });
      if (next) next.addEventListener("click", () => { page += 1; render(); });
      render();
    }
  })();

  (() => {
    const perTeamPage = 3;
    const currentSeasonValue = "current";
    const allSeasonsValue = "all";
    const teamOrderValue = (team) => {
      const match = String(team || "").match(/^(\d+)/);
      return match ? parseInt(match[1], 10) : -1;
    };
    const sortTeamsOlderFirst = (a, b) => {
      const aTeam = typeof a === "string" ? a : a.team;
      const bTeam = typeof b === "string" ? b : b.team;
      const ageDiff = teamOrderValue(bTeam) - teamOrderValue(aTeam);
      return ageDiff || String(aTeam).localeCompare(String(bTeam), undefined, { numeric: true });
    };
    const uniqueBy = (items, keyFn) => {
      const seen = new Set();
      return items.filter((item) => {
        const key = keyFn(item);
        if (!key || seen.has(key)) return false;
        seen.add(key);
        return true;
      });
    };
    const matchesSeasonScope = (item, seasonValue) => {
      if (seasonValue === allSeasonsValue) return true;
      if (seasonValue === currentSeasonValue) return item.dataset.currentTeam === "true";
      return item.dataset.season === seasonValue;
    };
    const filterOptionLabel = (seasonValue) => {
      if (seasonValue === allSeasonsValue) return "All Teams";
      if (seasonValue === currentSeasonValue) return "All Current Teams";
      return "All Teams";
    };

    const setupScopedTeamOptions = (root, items, onChange) => {
      const seasonSelect = root.querySelector("[data-filter-season]");
      const teamSelect = root.querySelector("[data-filter-team]");

      const rebuildTeamOptions = () => {
        const seasonValue = seasonSelect ? seasonSelect.value : currentSeasonValue;
        const currentValue = teamSelect.value;
        const useSeasonLabel = seasonValue === allSeasonsValue;
        const options = uniqueBy(
          items
            .filter((item) => matchesSeasonScope(item, seasonValue))
            .map((item) => ({
              key: item.dataset.teamKey,
              team: item.dataset.team,
              season: item.dataset.season,
              seasonLabel: item.dataset.seasonLabel,
              currentTeam: item.dataset.currentTeam === "true"
            }))
            .sort(sortTeamsOlderFirst),
          (item) => item.key
        );

        teamSelect.innerHTML = "";
        const allOption = document.createElement("option");
        allOption.value = "";
        allOption.textContent = filterOptionLabel(seasonValue);
        teamSelect.appendChild(allOption);

        options.forEach((item) => {
          const option = document.createElement("option");
          option.value = item.key;
          option.textContent = useSeasonLabel ? `${item.team} — ${item.seasonLabel}` : item.team;
          teamSelect.appendChild(option);
        });

        if (currentValue && options.some((item) => item.key === currentValue)) {
          teamSelect.value = currentValue;
        }
      };

      if (seasonSelect) {
        seasonSelect.addEventListener("change", () => {
          rebuildTeamOptions();
          onChange();
        });
      }
      teamSelect.addEventListener("change", onChange);
      rebuildTeamOptions();
    };

    const teamRoot = document.querySelector("[data-team-achievement-filter]");
    const teamGroups = Array.from(document.querySelectorAll("[data-team-group]"));
    const teamEmpty = document.querySelector("[data-team-empty]");

    if (teamRoot && teamGroups.length) {
      const seasonSelect = teamRoot.querySelector("[data-filter-season]");
      const teamSelect = teamRoot.querySelector("[data-filter-team]");
      const searchInput = teamRoot.querySelector("[data-filter-search]");
      const teamList = teamGroups[0].parentElement;
      if (teamList) {
        teamGroups
          .slice()
          .sort((a, b) => sortTeamsOlderFirst(a.dataset.team, b.dataset.team))
          .forEach((group) => teamList.appendChild(group));
      }

      const getMatchingItems = (group) => {
        const query = searchInput.value.trim().toLowerCase();
        return Array.from(group.querySelectorAll("[data-team-achievement-item]")).filter((item) => {
          const text = item.dataset.search || "";
          return !query || text.includes(query);
        });
      };

      const renderTeamGroup = (group) => {
        const seasonValue = seasonSelect ? seasonSelect.value : currentSeasonValue;
        const selectedTeamKey = teamSelect.value;
        const seasonMatches = matchesSeasonScope(group, seasonValue);
        const teamMatches = selectedTeamKey ? group.dataset.teamKey === selectedTeamKey : true;
        const allItems = Array.from(group.querySelectorAll("[data-team-achievement-item]"));
        const matchingItems = (seasonMatches && teamMatches) ? getMatchingItems(group) : [];

        allItems.forEach((item) => { item.hidden = true; });

        if (!seasonMatches || !teamMatches || !matchingItems.length) {
          group.hidden = true;
          return 0;
        }

        group.hidden = false;

        const pageCount = Math.max(1, Math.ceil(matchingItems.length / perTeamPage));
        let page = parseInt(group.dataset.teamPage || "0", 10);
        if (Number.isNaN(page)) page = 0;
        page = Math.max(0, Math.min(page, pageCount - 1));
        group.dataset.teamPage = String(page);

        const start = page * perTeamPage;
        const end = Math.min(start + perTeamPage, matchingItems.length);

        matchingItems.forEach((item, index) => {
          item.hidden = !(index >= start && index < end);
        });

        const controls = group.querySelector("[data-team-carousel-controls]");
        const status = group.querySelector("[data-team-carousel-status]");
        const prev = group.querySelector("[data-team-carousel-prev]");
        const next = group.querySelector("[data-team-carousel-next]");

        if (controls) controls.hidden = matchingItems.length <= perTeamPage;
        if (status) status.textContent = `Showing ${start + 1}–${end} of ${matchingItems.length}`;
        if (prev) prev.disabled = page <= 0;
        if (next) next.disabled = page >= pageCount - 1;

        return 1;
      };

      const updateTeams = () => {
        let visibleGroups = 0;
        teamGroups.forEach((group) => {
          visibleGroups += renderTeamGroup(group);
        });
        if (teamEmpty) teamEmpty.hidden = visibleGroups !== 0;
      };

      teamGroups.forEach((group) => {
        const prev = group.querySelector("[data-team-carousel-prev]");
        const next = group.querySelector("[data-team-carousel-next]");

        if (prev) {
          prev.addEventListener("click", () => {
            group.dataset.teamPage = String((parseInt(group.dataset.teamPage || "0", 10) || 0) - 1);
            renderTeamGroup(group);
          });
        }

        if (next) {
          next.addEventListener("click", () => {
            group.dataset.teamPage = String((parseInt(group.dataset.teamPage || "0", 10) || 0) + 1);
            renderTeamGroup(group);
          });
        }
      });

      setupScopedTeamOptions(teamRoot, teamGroups, () => {
        teamGroups.forEach((group) => { group.dataset.teamPage = "0"; });
        updateTeams();
      });

      searchInput.addEventListener("input", () => {
        teamGroups.forEach((group) => { group.dataset.teamPage = "0"; });
        updateTeams();
      });

      updateTeams();
    }

    const playerRoot = document.querySelector("[data-player-achievement-filter]");
    const playerGroups = Array.from(document.querySelectorAll("[data-player-group]"));
    const playerEmpty = document.querySelector("[data-player-empty]");

    if (playerRoot && playerGroups.length) {
      const seasonSelect = playerRoot.querySelector("[data-filter-season]");
      const teamSelect = playerRoot.querySelector("[data-filter-team]");
      const searchInput = playerRoot.querySelector("[data-filter-search]");
      const playerList = playerGroups[0].parentElement;

      if (playerList) {
        playerGroups
          .slice()
          .sort((a, b) => sortTeamsOlderFirst(a.dataset.team, b.dataset.team))
          .forEach((group) => playerList.appendChild(group));
      }

      const getMatchingPlayerItems = (group) => {
        const query = searchInput.value.trim().toLowerCase();
        return Array.from(group.querySelectorAll("[data-player-achievement-item]")).filter((item) => {
          const text = `${group.dataset.search || ""} ${item.dataset.search || ""}`;
          return !query || text.includes(query);
        });
      };

      const renderPlayerGroup = (group) => {
        const seasonValue = seasonSelect ? seasonSelect.value : currentSeasonValue;
        const selectedTeamKey = teamSelect.value;
        const seasonMatches = matchesSeasonScope(group, seasonValue);
        const teamMatches = selectedTeamKey ? group.dataset.teamKey === selectedTeamKey : true;
        const allItems = Array.from(group.querySelectorAll("[data-player-achievement-item]"));
        const matchingItems = (seasonMatches && teamMatches) ? getMatchingPlayerItems(group) : [];

        allItems.forEach((item) => { item.hidden = true; });

        if (!seasonMatches || !teamMatches || !matchingItems.length) {
          group.hidden = true;
          return 0;
        }

        group.hidden = false;

        const pageCount = Math.max(1, Math.ceil(matchingItems.length / perTeamPage));
        let page = parseInt(group.dataset.playerPage || "0", 10);
        if (Number.isNaN(page)) page = 0;
        page = Math.max(0, Math.min(page, pageCount - 1));
        group.dataset.playerPage = String(page);

        const start = page * perTeamPage;
        const end = Math.min(start + perTeamPage, matchingItems.length);

        matchingItems.forEach((item, index) => {
          item.hidden = !(index >= start && index < end);
        });

        const controls = group.querySelector("[data-player-carousel-controls]");
        const status = group.querySelector("[data-player-carousel-status]");
        const prev = group.querySelector("[data-player-carousel-prev]");
        const next = group.querySelector("[data-player-carousel-next]");

        if (controls) controls.hidden = matchingItems.length <= perTeamPage;
        if (status) status.textContent = `Showing ${start + 1}–${end} of ${matchingItems.length}`;
        if (prev) prev.disabled = page <= 0;
        if (next) next.disabled = page >= pageCount - 1;

        return 1;
      };

      const updatePlayers = () => {
        let visibleGroups = 0;
        playerGroups.forEach((group) => {
          visibleGroups += renderPlayerGroup(group);
        });
        if (playerEmpty) playerEmpty.hidden = visibleGroups !== 0;
      };

      playerGroups.forEach((group) => {
        const prev = group.querySelector("[data-player-carousel-prev]");
        const next = group.querySelector("[data-player-carousel-next]");

        if (prev) {
          prev.addEventListener("click", () => {
            group.dataset.playerPage = String((parseInt(group.dataset.playerPage || "0", 10) || 0) - 1);
            renderPlayerGroup(group);
          });
        }

        if (next) {
          next.addEventListener("click", () => {
            group.dataset.playerPage = String((parseInt(group.dataset.playerPage || "0", 10) || 0) + 1);
            renderPlayerGroup(group);
          });
        }
      });

      setupScopedTeamOptions(playerRoot, playerGroups, () => {
        playerGroups.forEach((group) => { group.dataset.playerPage = "0"; });
        updatePlayers();
      });

      searchInput.addEventListener("input", () => {
        playerGroups.forEach((group) => { group.dataset.playerPage = "0"; });
        updatePlayers();
      });

      updatePlayers();
    }
  })();
