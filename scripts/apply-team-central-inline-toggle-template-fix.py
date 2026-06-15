from pathlib import Path

page = Path('layouts/partials/page-teams.html')
css = Path('assets/css/main.css')

page.parent.mkdir(parents=True, exist_ok=True)
css.parent.mkdir(parents=True, exist_ok=True)

if page.exists():
    backup = Path('.backups/page-teams.html.bak-inline-toggle-template-fix')
    backup.parent.mkdir(parents=True, exist_ok=True)
    backup.write_text(page.read_text(), encoding='utf-8')

page.write_text(r'''{{ $data := .Site.Data.teams }}
{{ $seasonScratch := newScratch }}
{{ $seasonScratch.Set "defaultSeason" ($data.default_season | default "2026") }}
{{ range $data.seasons }}
  {{ if eq (lower .status) "current" }}
    {{ $seasonScratch.Set "defaultSeason" .id }}
  {{ end }}
{{ end }}
{{ $defaultSeason := $seasonScratch.Get "defaultSeason" }}

{{ partial "hero.html" (dict "kicker" "Team Central" "title" .Title "intro" $data.intro "actions" (slice (dict "label" "Become A Tiger" "url" "/become-a-tiger/" "class" "rt-btn-primary") (dict "label" "View Coaches" "url" "/coaches/" "class" "rt-btn-outline")) "show_card" false) }}

<section class="rt-section rt-team-central rt-team-central--dashboard rt-team-central--clean-table rt-team-central--final-cleanup rt-team-central--inline-toggle">
  <div class="rt-container">
    <section class="rt-season-dashboard rt-season-dashboard--clean" aria-label="Team Central season dashboard">
      <div class="rt-season-panels" data-team-season-panels>
        {{ range $data.seasons }}
          {{ if or (eq (lower .status) "current") (eq (lower .status) "upcoming") (eq .id $defaultSeason) }}
            <section class="rt-season-panel rt-season-panel--dashboard" data-season-panel="{{ .id }}" {{ if ne .id $defaultSeason }}hidden{{ end }}>
              <div class="rt-season-dashboard__summary rt-season-dashboard__summary--simple rt-season-dashboard__summary--clean">
                <div class="rt-season-dashboard__summary-copy">
                  <h2>{{ .label }}</h2>
                  <p>{{ .cycle }}</p>
                  <p class="rt-season-dashboard__helper">Choose a season to view active and upcoming Rawlings Tigers NOVA teams. Seasons run fall through spring.</p>
                </div>

                <div class="rt-season-toggle" role="tablist" aria-label="Select team season">
                  {{ range $data.seasons }}
                    {{ if or (eq (lower .status) "current") (eq (lower .status) "upcoming") }}
                      <button class="rt-season-toggle__button{{ if eq .id $defaultSeason }} is-active{{ end }}" type="button" role="tab" aria-selected="{{ if eq .id $defaultSeason }}true{{ else }}false{{ end }}" data-season-button="{{ .id }}">
                        <span>{{ .status }}</span>
                        <strong>{{ .label }}</strong>
                      </button>
                    {{ end }}
                  {{ end }}
                </div>
              </div>

              <div class="rt-season-dashboard__terms rt-season-dashboard__terms--clean">
                {{ with .spring }}
                  {{ partial "team-table-term.html" (dict "term" .) }}
                {{ end }}

                {{ with .fall }}
                  {{ partial "team-table-term.html" (dict "term" .) }}
                {{ end }}
              </div>
            </section>
          {{ end }}
        {{ end }}
      </div>
    </section>
  </div>
</section>

<section class="rt-section rt-section--white rt-team-join-band rt-team-join-band--compact">
  <div class="rt-container rt-team-join-band__inner">
    <div>
      <p class="rt-eyebrow rt-eyebrow--dark">Looking for a team?</p>
      <h2>Interested in an upcoming roster?</h2>
      <p>Tell us about your player and a coach will follow up with the best current or upcoming team fit.</p>
    </div>
    <div class="rt-action-row">
      <a class="rt-btn rt-btn--orange" href="{{ partial "url.html" "/become-a-tiger/" }}">Become A Tiger</a>
      <a class="rt-btn rt-btn--ghost-light rt-btn--dark-outline" href="{{ partial "url.html" "/tryouts/" }}">Tryouts</a>
    </div>
  </div>
</section>

<script>
(function () {
  var buttons = document.querySelectorAll('[data-season-button]');
  var panels = document.querySelectorAll('[data-season-panel]');
  if (!buttons.length || !panels.length) return;

  function showSeason(value) {
    panels.forEach(function (panel) {
      panel.hidden = panel.getAttribute('data-season-panel') !== value;
    });
    buttons.forEach(function (button) {
      var active = button.getAttribute('data-season-button') === value;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-selected', active ? 'true' : 'false');
    });
  }

  var activeButton = document.querySelector('[data-season-button].is-active') || buttons[0];
  if (activeButton) showSeason(activeButton.getAttribute('data-season-button'));

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      showSeason(button.getAttribute('data-season-button'));
    });
  });
})();
</script>
''', encoding='utf-8')

append = r'''

/* Team Central: move Current/Upcoming toggle into black season header */
.rt-team-central--inline-toggle .rt-season-dashboard__top,
.rt-team-central--inline-toggle .rt-season-dashboard__selector-copy {
  display: none !important;
}

.rt-team-central--inline-toggle .rt-season-dashboard {
  overflow: hidden;
  border-radius: 24px;
  background: #fff;
  box-shadow: 0 24px 70px rgba(0, 0, 0, 0.12);
}

.rt-team-central--inline-toggle .rt-season-dashboard__summary {
  display: flex !important;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
  background: #07101d;
  color: #fff;
  border-radius: 24px 24px 0 0;
  border-top: 0;
  border-bottom: 4px solid var(--brand, #f15a24);
  padding: clamp(2rem, 4vw, 3.25rem);
}

.rt-team-central--inline-toggle .rt-season-dashboard__summary h2 {
  margin: 0;
  color: #fff;
  font-size: clamp(2.75rem, 6vw, 5rem);
  line-height: 0.95;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.rt-team-central--inline-toggle .rt-season-dashboard__summary p {
  margin: 0.75rem 0 0;
  color: rgba(255, 255, 255, 0.78);
  font-weight: 800;
}

.rt-team-central--inline-toggle .rt-season-dashboard__helper {
  max-width: 52rem;
  color: rgba(255, 255, 255, 0.64) !important;
  font-size: 0.95rem;
  line-height: 1.55;
}

.rt-team-central--inline-toggle .rt-season-dashboard__summary .rt-season-toggle {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.35rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: none;
}

.rt-team-central--inline-toggle .rt-season-dashboard__summary .rt-season-toggle__button {
  border: 0;
  border-radius: 999px;
  padding: 0.75rem 1.25rem;
  background: transparent;
  color: rgba(255, 255, 255, 0.72);
  font-size: 0.72rem;
  font-weight: 900;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.rt-team-central--inline-toggle .rt-season-dashboard__summary .rt-season-toggle__button span,
.rt-team-central--inline-toggle .rt-season-dashboard__summary .rt-season-toggle__button strong {
  display: block;
  color: inherit;
}

.rt-team-central--inline-toggle .rt-season-dashboard__summary .rt-season-toggle__button.is-active {
  background: #fff;
  color: #07101d;
}

.rt-team-central--inline-toggle .rt-season-dashboard__terms {
  padding: clamp(1.75rem, 3vw, 2.5rem);
}

@media (max-width: 760px) {
  .rt-team-central--inline-toggle .rt-season-dashboard__summary {
    align-items: flex-start;
    flex-direction: column;
  }

  .rt-team-central--inline-toggle .rt-season-dashboard__summary .rt-season-toggle {
    width: 100%;
  }

  .rt-team-central--inline-toggle .rt-season-dashboard__summary .rt-season-toggle__button {
    flex: 1;
    text-align: center;
  }
}
'''

current = css.read_text(encoding='utf-8') if css.exists() else ''
marker = '/* Team Central: move Current/Upcoming toggle into black season header */'
if marker not in current:
    css.write_text(current.rstrip() + append + '\n', encoding='utf-8')
else:
    print('CSS marker already present; left assets/css/main.css unchanged.')

print('Applied Team Central inline toggle template fix.')
print('Backup, if any, saved under .backups/ so Hugo will not load it as data.')
