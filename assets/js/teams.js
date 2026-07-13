(function () {
  var root = document.querySelector('[data-team-central]');
  if (!root) return;

  var defaultSeason = root.getAttribute('data-default-season') || '';
  var buttons = root.querySelectorAll('[data-season-button]');
  var panels = root.querySelectorAll('[data-season-panel]');
  if (!buttons.length || !panels.length) return;

  var archiveSeason = root.querySelector('[data-team-archive-season]');
  var archiveTeam = root.querySelector('[data-team-archive-team]');
  var archiveSearch = root.querySelector('[data-team-archive-search]');
  var archiveRows = Array.prototype.slice.call(root.querySelectorAll('[data-team-archive-row]'));
  var archiveEmpty = root.querySelector('[data-team-archive-empty]');
  var archiveCount = root.querySelector('[data-team-archive-count]');

  function showSeason(value) {
    panels.forEach(function (panel) {
      panel.hidden = panel.getAttribute('data-season-panel') !== value;
    });
    buttons.forEach(function (button) {
      var active = button.getAttribute('data-season-button') === value;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
    });

    if (value === 'archive') {
      updateArchiveTeamOptions();
      filterArchiveTeams();
    }
  }

  function optionExists(select, value) {
    return Array.prototype.some.call(select.options, function (option) {
      return option.value === value;
    });
  }

  function updateArchiveTeamOptions() {
    if (!archiveSeason || !archiveTeam) return;

    var selectedSeason = archiveSeason.value || defaultSeason;
    var previousValue = archiveTeam.value || 'all';
    var teams = [];
    var seen = Object.create(null);

    archiveRows.forEach(function (row) {
      var season = row.getAttribute('data-archive-season') || '';
      if (season !== selectedSeason) return;

      var key = row.getAttribute('data-archive-team-key') || '';
      if (!key) return;

      var teamName = row.getAttribute('data-archive-team-name') || 'Team';
      var seasonLabel = row.getAttribute('data-archive-season-label') || season;
      var sortOrder = parseInt(row.getAttribute('data-archive-sort-order') || '9999', 10);

      if (Object.prototype.hasOwnProperty.call(seen, key)) {
        var existingTeam = teams[seen[key]];
        if (sortOrder < existingTeam.sortOrder) existingTeam.sortOrder = sortOrder;
        return;
      }

      seen[key] = teams.length;
      teams.push({
        key: key,
        label: teamName,
        teamName: teamName,
        season: season,
        sortOrder: sortOrder
      });
    });

    teams.sort(function (a, b) {
      if (a.season !== b.season) return b.season.localeCompare(a.season);
      if (a.sortOrder !== b.sortOrder) return a.sortOrder - b.sortOrder;
      return a.teamName.localeCompare(b.teamName, undefined, { numeric: true, sensitivity: 'base' });
    });

    archiveTeam.innerHTML = '';
    var allOption = document.createElement('option');
    allOption.value = 'all';
    allOption.textContent = 'All Teams';
    archiveTeam.appendChild(allOption);

    teams.forEach(function (team) {
      var option = document.createElement('option');
      option.value = team.key;
      option.textContent = team.label;
      archiveTeam.appendChild(option);
    });

    archiveTeam.value = optionExists(archiveTeam, previousValue) ? previousValue : 'all';
  }

  function sortArchiveRows() {
    var results = root.querySelector('[data-team-archive-results]');
    if (!results || !archiveRows.length) return;

    var groupOrders = archiveRows.reduce(function (orders, row) {
      var season = row.getAttribute('data-archive-season') || '';
      var team = (row.getAttribute('data-archive-team-name') || '').toLowerCase();
      var key = season + '::' + team;
      var order = parseInt(row.getAttribute('data-archive-sort-order') || '9999', 10);
      if (!Object.prototype.hasOwnProperty.call(orders, key) || order < orders[key]) {
        orders[key] = order;
      }
      return orders;
    }, {});

    archiveRows.sort(function (a, b) {
      var seasonA = a.getAttribute('data-archive-season') || '';
      var seasonB = b.getAttribute('data-archive-season') || '';
      if (seasonA !== seasonB) return seasonB.localeCompare(seasonA, undefined, { numeric: true });

      var teamA = a.getAttribute('data-archive-team-name') || '';
      var teamB = b.getAttribute('data-archive-team-name') || '';
      var teamKeyA = seasonA + '::' + teamA.toLowerCase();
      var teamKeyB = seasonB + '::' + teamB.toLowerCase();
      var groupOrderA = groupOrders[teamKeyA] || 9999;
      var groupOrderB = groupOrders[teamKeyB] || 9999;
      if (groupOrderA !== groupOrderB) return groupOrderA - groupOrderB;

      var teamSort = teamA.localeCompare(teamB, undefined, { numeric: true, sensitivity: 'base' });
      if (teamSort !== 0) return teamSort;

      var termA = parseInt(a.getAttribute('data-archive-term-order') || '9', 10);
      var termB = parseInt(b.getAttribute('data-archive-term-order') || '9', 10);
      return termA - termB;
    });

    var previousTeamKey = '';
    archiveRows.forEach(function (row) {
      var rowSeason = row.getAttribute('data-archive-season') || '';
      var rowTeam = (row.getAttribute('data-archive-team-name') || '').toLowerCase();
      var teamKey = rowSeason + '::' + rowTeam;
      var isContinuation = teamKey === previousTeamKey;
      row.classList.toggle('is-team-group-start', !isContinuation);
      row.classList.toggle('is-team-group-continuation', isContinuation);
      previousTeamKey = teamKey;
      results.appendChild(row);
    });
  }

  function filterArchiveTeams() {
    if (!archiveRows.length) return;

    var selectedSeason = archiveSeason ? archiveSeason.value : defaultSeason;
    var selectedTeam = archiveTeam ? archiveTeam.value : 'all';
    var query = archiveSearch ? archiveSearch.value.trim().toLowerCase() : '';
    var visibleCount = 0;
    var visibleTeams = Object.create(null);

    archiveRows.forEach(function (row) {
      var rowSeason = row.getAttribute('data-archive-season') || '';
      var rowTeam = row.getAttribute('data-archive-team-key') || '';
      var rowSearch = row.getAttribute('data-archive-search') || '';

      var matchesSeason = rowSeason === selectedSeason;
      var matchesTeam = selectedTeam === 'all' || rowTeam === selectedTeam;
      var matchesSearch = !query || rowSearch.indexOf(query) !== -1;
      var visible = matchesSeason && matchesTeam && matchesSearch;

      row.hidden = !visible;
      if (visible) {
        visibleCount += 1;
        visibleTeams[rowTeam] = true;
      }
    });

    if (archiveEmpty) archiveEmpty.hidden = visibleCount !== 0;
    if (archiveCount) {
      var visibleTeamCount = Object.keys(visibleTeams).length;
      var teamLabel = visibleTeamCount === 1 ? 'team' : 'teams';
      var entryLabel = visibleCount === 1 ? 'season entry' : 'season entries';
      archiveCount.textContent = visibleTeamCount + ' ' + teamLabel + ' · ' + visibleCount + ' ' + entryLabel;
    }
  }

  sortArchiveRows();

  var activeButton = root.querySelector('[data-season-button].is-active') || buttons[0];
  if (activeButton) showSeason(activeButton.getAttribute('data-season-button'));

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      showSeason(button.getAttribute('data-season-button'));
    });
  });

  if (archiveSeason) {
    archiveSeason.addEventListener('change', function () {
      updateArchiveTeamOptions();
      filterArchiveTeams();
    });
  }
  if (archiveTeam) archiveTeam.addEventListener('change', filterArchiveTeams);
  if (archiveSearch) archiveSearch.addEventListener('input', filterArchiveTeams);
})();
