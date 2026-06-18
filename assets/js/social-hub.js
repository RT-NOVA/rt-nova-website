(() => {
  function initHomePager(root) {
    const cards = Array.from(root.querySelectorAll('[data-social-card]'));
    const prev = root.querySelector('[data-social-hub-prev]');
    const next = root.querySelector('[data-social-hub-next]');
    const status = root.querySelector('[data-social-hub-status]');
    const pageSize = Number.parseInt(root.getAttribute('data-social-feed-page-size') || '3', 10) || 3;
    if (!cards.length) return;

    let page = 0;
    const pageCount = Math.ceil(cards.length / pageSize);

    function render() {
      const start = page * pageSize;
      const end = start + pageSize;
      cards.forEach((card, index) => {
        card.hidden = index < start || index >= end;
      });

      if (prev) prev.disabled = page === 0;
      if (next) next.disabled = page >= pageCount - 1;
      if (status) {
        const visibleEnd = Math.min(end, cards.length);
        status.textContent = `Showing ${start + 1}-${visibleEnd} of ${cards.length}`;
      }
    }

    if (prev) {
      prev.addEventListener('click', () => {
        if (page > 0) {
          page -= 1;
          render();
        }
      });
    }

    if (next) {
      next.addEventListener('click', () => {
        if (page < pageCount - 1) {
          page += 1;
          render();
        }
      });
    }

    render();
  }

  function initArchiveTabs(root) {
    const buttons = Array.from(root.querySelectorAll('[data-social-filter]'));
    const cards = Array.from(root.querySelectorAll('[data-social-card]'));
    const empty = root.querySelector('[data-social-empty]');
    if (!buttons.length || !cards.length) return;

    function applyFilter(filter) {
      let visible = 0;
      cards.forEach((card) => {
        const type = card.getAttribute('data-social-type') || 'team-news';
        const show = filter === 'all' || type === filter;
        card.hidden = !show;
        if (show) visible += 1;
      });

      buttons.forEach((button) => {
        const active = button.getAttribute('data-social-filter') === filter;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-selected', active ? 'true' : 'false');
      });

      if (empty) empty.hidden = visible !== 0;
    }

    buttons.forEach((button) => {
      button.addEventListener('click', () => {
        applyFilter(button.getAttribute('data-social-filter') || 'all');
      });
    });

    applyFilter('all');
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-social-hub-pager]').forEach(initHomePager);
    document.querySelectorAll('[data-social-hub-tabs]').forEach(initArchiveTabs);
  });
})();
