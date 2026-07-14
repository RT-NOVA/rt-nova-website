(() => {
  const perTeamPage = 3;
  const playerPageSize = 6;
  const currentSeasonValue = "current";
  const allSeasonsValue = "all";

  const teamAge = (team) => {
    const match = String(team || "").match(/^(\d+)/);
    return match ? parseInt(match[1], 10) : -1;
  };

  const teamColorOrder = (team) => {
    const value = String(team || "").toLowerCase();
    if (value.includes("black")) return 0;
    if (value.includes("orange")) return 1;
    return 2;
  };

  const sortTeamsOlderFirst = (a, b) => {
    const aTeam = typeof a === "string" ? a : a.team;
    const bTeam = typeof b === "string" ? b : b.team;
    const ageDifference = teamAge(bTeam) - teamAge(aTeam);
    if (ageDifference) return ageDifference;

    const colorDifference = teamColorOrder(aTeam) - teamColorOrder(bTeam);
    if (colorDifference) return colorDifference;

    return String(aTeam).localeCompare(String(bTeam), undefined, {
      numeric: true,
      sensitivity: "base"
    });
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

  const allTeamsLabel = (seasonValue) => {
    if (seasonValue === currentSeasonValue) return "All Current Teams";
    return "All Teams";
  };

  const setupTeamOptions = (root, groups) => {
    const seasonSelect = root.querySelector("[data-filter-season]");
    const teamSelect = root.querySelector("[data-filter-team]");

    const rebuild = () => {
      const seasonValue = seasonSelect ? seasonSelect.value : currentSeasonValue;
      const currentValue = teamSelect.value;
      const includeSeason = seasonValue === allSeasonsValue;
      const options = uniqueBy(
        groups
          .filter((group) => matchesSeasonScope(group, seasonValue))
          .map((group) => ({
            key: group.dataset.teamKey,
            team: group.dataset.team,
            seasonLabel: group.dataset.seasonLabel
          }))
          .sort(sortTeamsOlderFirst),
        (item) => item.key
      );

      teamSelect.innerHTML = "";
      const allOption = document.createElement("option");
      allOption.value = "";
      allOption.textContent = allTeamsLabel(seasonValue);
      teamSelect.appendChild(allOption);

      options.forEach((item) => {
        const option = document.createElement("option");
        option.value = item.key;
        option.textContent = includeSeason ? `${item.team} — ${item.seasonLabel}` : item.team;
        teamSelect.appendChild(option);
      });

      teamSelect.value = options.some((item) => item.key === currentValue) ? currentValue : "";
    };

    return rebuild;
  };

  const setupBannerArchive = () => {
    const defaultSeasonValue = allSeasonsValue;
    const root = document.querySelector("[data-team-achievement-filter]");
    const gallery = document.querySelector("[data-team-banner-results]");
    const items = Array.from(document.querySelectorAll("[data-team-banner-result]"));
    const empty = document.querySelector("[data-team-empty]");
    if (!root || !gallery || !items.length) return;

    const seasonSelect = root.querySelector("[data-filter-season]");
    const teamSelect = root.querySelector("[data-filter-team]");
    const searchInput = root.querySelector("[data-filter-search]");
    const count = root.querySelector("[data-filter-count]");
    const clear = root.querySelector("[data-filter-clear]");
    const controls = document.querySelector("[data-team-banner-results-controls]");
    const status = document.querySelector("[data-team-banner-results-status]");
    const previous = document.querySelector("[data-team-banner-results-prev]");
    const following = document.querySelector("[data-team-banner-results-next]");
    const rebuildTeamOptions = setupTeamOptions(root, items);
    let page = 0;

    const matchingItems = () => {
      const seasonValue = seasonSelect.value;
      const selectedTeam = teamSelect.value;
      const query = searchInput.value.trim().toLowerCase();

      return items.filter((item) => {
        const seasonMatches = matchesSeasonScope(item, seasonValue);
        const teamMatches = !selectedTeam || item.dataset.teamKey === selectedTeam;
        const searchMatches = !query || (item.dataset.search || "").includes(query);
        return seasonMatches && teamMatches && searchMatches;
      });
    };

    const update = () => {
      const matches = matchingItems();
      const pageCount = Math.max(1, Math.ceil(matches.length / perTeamPage));
      page = Math.max(0, Math.min(page, pageCount - 1));
      const start = page * perTeamPage;
      const end = Math.min(start + perTeamPage, matches.length);
      const visible = new Set(matches.slice(start, end));

      items.forEach((item) => { item.hidden = !visible.has(item); });
      gallery.setAttribute("data-visible-count", String(end - start));

      if (empty) empty.hidden = matches.length !== 0;
      if (controls) controls.hidden = matches.length <= perTeamPage;
      if (status) status.textContent = matches.length ? `${start + 1}–${end} of ${matches.length}` : "0 of 0";
      if (previous) previous.disabled = page <= 0;
      if (following) following.disabled = page >= pageCount - 1;

      if (count) {
        const teamCount = new Set(matches.map((item) => item.dataset.teamKey)).size;
        const teamWord = teamCount === 1 ? "team" : "teams";
        const bannerWord = matches.length === 1 ? "banner" : "banners";
        count.textContent = `${teamCount} ${teamWord} · ${matches.length} ${bannerWord}`;
      }

      if (clear) {
        const isDefault = seasonSelect.value === defaultSeasonValue && !teamSelect.value && !searchInput.value.trim();
        clear.hidden = isDefault;
      }
    };

    seasonSelect.addEventListener("change", () => {
      rebuildTeamOptions();
      page = 0;
      update();
    });
    teamSelect.addEventListener("change", () => {
      page = 0;
      update();
    });
    searchInput.addEventListener("input", () => {
      page = 0;
      update();
    });

    if (previous) {
      previous.addEventListener("click", () => {
        page -= 1;
        update();
      });
    }
    if (following) {
      following.addEventListener("click", () => {
        page += 1;
        update();
      });
    }

    if (clear) {
      clear.addEventListener("click", () => {
        seasonSelect.value = defaultSeasonValue;
        searchInput.value = "";
        rebuildTeamOptions();
        teamSelect.value = "";
        page = 0;
        update();
        seasonSelect.focus();
      });
    }

    rebuildTeamOptions();
    update();
  };

  const setupPlayerGallery = () => {
    const defaultSeasonValue = allSeasonsValue;
    const root = document.querySelector("[data-player-achievement-filter]");
    const gallery = document.querySelector("[data-player-results]");
    const items = Array.from(document.querySelectorAll("[data-player-result]"));
    const empty = document.querySelector("[data-player-empty]");
    if (!root || !gallery) return;

    const seasonSelect = root.querySelector("[data-filter-season]");
    const teamSelect = root.querySelector("[data-filter-team]");
    const searchInput = root.querySelector("[data-filter-search]");
    const count = root.querySelector("[data-filter-count]");
    const clear = root.querySelector("[data-filter-clear]");
    const controls = document.querySelector("[data-player-results-controls]");
    const status = document.querySelector("[data-player-results-status]");
    const previous = document.querySelector("[data-player-results-prev]");
    const following = document.querySelector("[data-player-results-next]");

    if (!items.length) {
      if (empty) empty.hidden = false;
      if (count) count.textContent = "0 teams · 0 honors";
      return;
    }

    const rebuildTeamOptions = setupTeamOptions(root, items);
    const randomRank = new Map(items.map((item) => [item, Math.random()]));
    let page = 0;

    const termOrder = (term) => {
      if (term === "spring") return 2;
      if (term === "fall") return 1;
      return 0;
    };

    const comparePeriodsNewestFirst = (a, b) => {
      const seasonDifference = String(b.season).localeCompare(String(a.season), undefined, { numeric: true });
      if (seasonDifference) return seasonDifference;
      return termOrder(b.term) - termOrder(a.term);
    };

    const balanceTeams = (periodItems) => {
      const buckets = new Map();
      periodItems.forEach((item) => {
        const team = item.dataset.team || "";
        if (!buckets.has(team)) buckets.set(team, []);
        buckets.get(team).push(item);
      });

      buckets.forEach((bucket) => {
        bucket.sort((a, b) => randomRank.get(a) - randomRank.get(b));
      });

      const teams = Array.from(buckets.keys()).sort(sortTeamsOlderFirst);
      const balanced = [];
      let added = true;
      while (added) {
        added = false;
        teams.forEach((team) => {
          const next = buckets.get(team).shift();
          if (next) {
            balanced.push(next);
            added = true;
          }
        });
      }
      return balanced;
    };

    const balancedRecentOrder = (matches) => {
      const periods = new Map();
      matches.forEach((item) => {
        const period = {
          season: item.dataset.season || "",
          term: item.dataset.term || ""
        };
        const key = `${period.season}|${period.term}`;
        if (!periods.has(key)) periods.set(key, { ...period, items: [] });
        periods.get(key).items.push(item);
      });

      return Array.from(periods.values())
        .sort(comparePeriodsNewestFirst)
        .flatMap((period) => balanceTeams(period.items));
    };

    const orderedMatches = () => {
      const seasonValue = seasonSelect.value;
      const selectedTeam = teamSelect.value;
      const query = searchInput.value.trim().toLowerCase();
      const matches = items.filter((item) => {
        const seasonMatches = matchesSeasonScope(item, seasonValue);
        const teamMatches = !selectedTeam || item.dataset.teamKey === selectedTeam;
        const searchMatches = !query || (item.dataset.search || "").includes(query);
        return seasonMatches && teamMatches && searchMatches;
      });

      return !selectedTeam && !query ? balancedRecentOrder(matches) : matches;
    };

    const update = () => {
      const matches = orderedMatches();
      const pageCount = Math.max(1, Math.ceil(matches.length / playerPageSize));
      page = Math.max(0, Math.min(page, pageCount - 1));
      const start = page * playerPageSize;
      const end = Math.min(start + playerPageSize, matches.length);
      const visible = new Set(matches.slice(start, end));

      matches.forEach((item) => gallery.appendChild(item));
      items.forEach((item) => { item.hidden = !visible.has(item); });
      gallery.setAttribute("data-visible-count", String(end - start));

      if (empty) empty.hidden = matches.length !== 0;
      if (controls) controls.hidden = matches.length <= playerPageSize;
      if (status) status.textContent = matches.length ? `${start + 1}–${end} of ${matches.length}` : "0 of 0";
      if (previous) previous.disabled = page <= 0;
      if (following) following.disabled = page >= pageCount - 1;

      if (count) {
        const teamCount = new Set(matches.map((item) => item.dataset.team)).size;
        const teamWord = teamCount === 1 ? "team" : "teams";
        const honorWord = matches.length === 1 ? "honor" : "honors";
        count.textContent = `${teamCount} ${teamWord} · ${matches.length} ${honorWord}`;
      }

      if (clear) {
        const isDefault = seasonSelect.value === defaultSeasonValue && !teamSelect.value && !searchInput.value.trim();
        clear.hidden = isDefault;
      }
    };

    seasonSelect.addEventListener("change", () => {
      rebuildTeamOptions();
      page = 0;
      update();
    });
    teamSelect.addEventListener("change", () => {
      page = 0;
      update();
    });
    searchInput.addEventListener("input", () => {
      page = 0;
      update();
    });

    if (previous) {
      previous.addEventListener("click", () => {
        page -= 1;
        update();
      });
    }
    if (following) {
      following.addEventListener("click", () => {
        page += 1;
        update();
      });
    }

    if (clear) {
      clear.addEventListener("click", () => {
        seasonSelect.value = defaultSeasonValue;
        searchInput.value = "";
        rebuildTeamOptions();
        teamSelect.value = "";
        page = 0;
        update();
        seasonSelect.focus();
      });
    }

    rebuildTeamOptions();
    update();
  };

  setupBannerArchive();
  setupPlayerGallery();
})();

(() => {
  const modal = document.querySelector("[data-player-photo-modal]");
  if (!modal) return;

  const image = modal.querySelector("[data-player-photo-modal-image]");
  const name = modal.querySelector("[data-player-photo-modal-name]");
  const honor = modal.querySelector("[data-player-photo-modal-honor]");
  const closeButtons = modal.querySelectorAll("[data-player-photo-close]");
  let lastTrigger = null;

  const openModal = (trigger) => {
    const src = trigger.dataset.playerPhoto;
    if (!src) return;

    lastTrigger = trigger;
    image.src = src;
    image.alt = trigger.dataset.playerName || "Player honor";
    name.textContent = trigger.dataset.playerName || "Player honor";
    honor.textContent = trigger.dataset.playerHonor || "";
    modal.hidden = false;
    document.documentElement.classList.add("accolades-photo-modal-open");

    const closeButton = modal.querySelector(".accolades-photo-modal__close");
    if (closeButton) closeButton.focus();
  };

  const closeModal = () => {
    if (modal.hidden) return;
    modal.hidden = true;
    image.removeAttribute("src");
    document.documentElement.classList.remove("accolades-photo-modal-open");
    if (lastTrigger) lastTrigger.focus();
  };

  document.querySelectorAll("[data-player-photo]").forEach((trigger) => {
    trigger.addEventListener("click", () => openModal(trigger));
  });

  closeButtons.forEach((button) => button.addEventListener("click", closeModal));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !modal.hidden) closeModal();
  });
})();
