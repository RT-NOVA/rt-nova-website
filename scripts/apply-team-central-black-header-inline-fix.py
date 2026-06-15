from pathlib import Path

css_path = Path('assets/css/main.css')
js_path = Path('assets/js/main.js')

css_marker = '/* RT NOVA Team Central: black inline season toggle fix */'
css = r'''
/* RT NOVA Team Central: black inline season toggle fix */
/* Goal: remove the white selector cap and place Current/Upcoming inside the black season header. */

/* Collapse the old white selector area if it still exists. Keep it visible only as a tiny structural wrapper. */
.rt-team-season-selector,
.rt-team-season-picker,
.rt-team-dashboard-selector,
.rt-team-season-dashboard__selector,
.team-season-selector,
.team-central-season-selector,
.team-dashboard-selector,
.team-central-dashboard__selector {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
  margin: 0 !important;
  padding: 0 !important;
  min-height: 0 !important;
  height: 0 !important;
  overflow: visible !important;
}

/* Hide redundant selector text/labels from the collapsed white area. */
.rt-team-season-selector > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch),
.rt-team-season-picker > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch),
.rt-team-dashboard-selector > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch),
.rt-team-season-dashboard__selector > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch),
.team-season-selector > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch),
.team-central-season-selector > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch),
.team-dashboard-selector > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch),
.team-central-dashboard__selector > :not(.rt-season-toggle):not(.team-season-toggle):not(.team-central-season-toggle):not(.rt-team-season-switch):not(.team-season-switch) {
  display: none !important;
}

/* The black season header becomes the top of the dashboard card. */
.rt-team-season-summary,
.rt-team-season-hero,
.rt-team-selected-season,
.rt-team-dashboard__season,
.rt-team-season-dashboard__summary,
.team-season-summary,
.team-season-hero,
.team-selected-season,
.team-dashboard__season,
.team-season-dashboard__summary {
  position: relative !important;
  border-radius: 18px 18px 0 0 !important;
  margin-top: 0 !important;
  padding-right: clamp(1.5rem, 34vw, 28rem) !important;
}

/* When the JS moves the toggle into the black header, this positions it inline with the season title. */
.rt-team-season-summary .rt-season-toggle,
.rt-team-season-summary .team-season-toggle,
.rt-team-season-summary .team-central-season-toggle,
.rt-team-season-summary .rt-team-season-switch,
.rt-team-season-summary .team-season-switch,
.rt-team-season-hero .rt-season-toggle,
.rt-team-season-hero .team-season-toggle,
.rt-team-season-hero .team-central-season-toggle,
.rt-team-season-hero .rt-team-season-switch,
.rt-team-season-hero .team-season-switch,
.rt-team-selected-season .rt-season-toggle,
.rt-team-selected-season .team-season-toggle,
.rt-team-selected-season .team-central-season-toggle,
.rt-team-selected-season .rt-team-season-switch,
.rt-team-selected-season .team-season-switch,
.rt-team-season-dashboard__summary .rt-season-toggle,
.rt-team-season-dashboard__summary .team-season-toggle,
.rt-team-season-dashboard__summary .team-central-season-toggle,
.rt-team-season-dashboard__summary .rt-team-season-switch,
.rt-team-season-dashboard__summary .team-season-switch,
.team-season-summary .rt-season-toggle,
.team-season-summary .team-season-toggle,
.team-season-summary .team-central-season-toggle,
.team-season-summary .rt-team-season-switch,
.team-season-summary .team-season-switch,
.team-season-hero .rt-season-toggle,
.team-season-hero .team-season-toggle,
.team-season-hero .team-central-season-toggle,
.team-season-hero .rt-team-season-switch,
.team-season-hero .team-season-switch,
.team-selected-season .rt-season-toggle,
.team-selected-season .team-season-toggle,
.team-selected-season .team-central-season-toggle,
.team-selected-season .rt-team-season-switch,
.team-selected-season .team-season-switch,
.team-season-dashboard__summary .rt-season-toggle,
.team-season-dashboard__summary .team-season-toggle,
.team-season-dashboard__summary .team-central-season-toggle,
.team-season-dashboard__summary .rt-team-season-switch,
.team-season-dashboard__summary .team-season-switch {
  position: absolute !important;
  top: clamp(1.25rem, 2.5vw, 2rem) !important;
  right: clamp(1.25rem, 3vw, 2.5rem) !important;
  z-index: 5 !important;
  margin: 0 !important;
  width: min(360px, 42vw) !important;
}

/* Remove any leftover white cap spacing above the black header. */
.rt-team-season-dashboard,
.team-season-dashboard,
.team-central-dashboard {
  overflow: hidden !important;
}

@media (max-width: 760px) {
  .rt-team-season-summary,
  .rt-team-season-hero,
  .rt-team-selected-season,
  .rt-team-dashboard__season,
  .rt-team-season-dashboard__summary,
  .team-season-summary,
  .team-season-hero,
  .team-selected-season,
  .team-dashboard__season,
  .team-season-dashboard__summary {
    padding-right: clamp(1rem, 5vw, 1.5rem) !important;
    padding-top: clamp(5rem, 16vw, 6.5rem) !important;
  }

  .rt-team-season-summary .rt-season-toggle,
  .rt-team-season-summary .team-season-toggle,
  .rt-team-season-summary .team-central-season-toggle,
  .rt-team-season-summary .rt-team-season-switch,
  .rt-team-season-summary .team-season-switch,
  .rt-team-season-hero .rt-season-toggle,
  .rt-team-season-hero .team-season-toggle,
  .rt-team-season-hero .team-central-season-toggle,
  .rt-team-season-hero .rt-team-season-switch,
  .rt-team-season-hero .team-season-switch,
  .rt-team-selected-season .rt-season-toggle,
  .rt-team-selected-season .team-season-toggle,
  .rt-team-selected-season .team-central-season-toggle,
  .rt-team-selected-season .rt-team-season-switch,
  .rt-team-selected-season .team-season-switch,
  .rt-team-season-dashboard__summary .rt-season-toggle,
  .rt-team-season-dashboard__summary .team-season-toggle,
  .rt-team-season-dashboard__summary .team-central-season-toggle,
  .rt-team-season-dashboard__summary .rt-team-season-switch,
  .rt-team-season-dashboard__summary .team-season-switch,
  .team-season-summary .rt-season-toggle,
  .team-season-summary .team-season-toggle,
  .team-season-summary .team-central-season-toggle,
  .team-season-summary .rt-team-season-switch,
  .team-season-summary .team-season-switch,
  .team-season-hero .rt-season-toggle,
  .team-season-hero .team-season-toggle,
  .team-season-hero .team-central-season-toggle,
  .team-season-hero .rt-team-season-switch,
  .team-season-hero .team-season-switch,
  .team-selected-season .rt-season-toggle,
  .team-selected-season .team-season-toggle,
  .team-selected-season .team-central-season-toggle,
  .team-selected-season .rt-team-season-switch,
  .team-selected-season .team-season-switch,
  .team-season-dashboard__summary .rt-season-toggle,
  .team-season-dashboard__summary .team-season-toggle,
  .team-season-dashboard__summary .team-central-season-toggle,
  .team-season-dashboard__summary .rt-team-season-switch,
  .team-season-dashboard__summary .team-season-switch {
    top: 1.1rem !important;
    left: clamp(1rem, 5vw, 1.5rem) !important;
    right: clamp(1rem, 5vw, 1.5rem) !important;
    width: auto !important;
  }
}
'''

js_marker = '// RT NOVA Team Central: move season toggle into black header'
js = r'''

// RT NOVA Team Central: move season toggle into black header
(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    var page = document.querySelector('.rt-team-central, .team-central, [data-page="teams"]');
    if (!page && !/\/teams\/?$/.test(window.location.pathname)) return;

    var toggle = document.querySelector(
      '.rt-season-toggle, .team-season-toggle, .team-central-season-toggle, .rt-team-season-switch, .team-season-switch, [data-team-season-toggle]'
    );

    var header = document.querySelector(
      '.rt-team-season-summary, .rt-team-season-hero, .rt-team-selected-season, .rt-team-dashboard__season, .rt-team-season-dashboard__summary, .team-season-summary, .team-season-hero, .team-selected-season, .team-dashboard__season, .team-season-dashboard__summary'
    );

    if (!toggle || !header || header.contains(toggle)) return;
    header.appendChild(toggle);
    header.classList.add('rt-season-toggle-inline-ready');
  });
}());
'''

if not css_path.exists():
    raise SystemExit('Missing assets/css/main.css')
text = css_path.read_text()
if css_marker not in text:
    css_path.write_text(text.rstrip() + '\n\n' + css + '\n')

if js_path.exists():
    jstext = js_path.read_text()
    if js_marker not in jstext:
        js_path.write_text(jstext.rstrip() + '\n' + js + '\n')
else:
    print('Note: assets/js/main.js not found; CSS was applied, but the toggle may not move if the template places it outside the black header.')

print('Applied Team Central black inline season toggle fix.')
