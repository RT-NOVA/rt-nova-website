#!/usr/bin/env python3
from pathlib import Path
import re

layout_path = Path("layouts/partials/page-tryouts.html")
css_path = Path("assets/css/tryouts.css")

if not layout_path.exists():
    raise SystemExit(f"Missing {layout_path}")

text = layout_path.read_text()

replacement = '''\\g<indent>{{ $sessionType := .type | default "Evaluation" }}
\\g<indent>{{ $sessionTypeLower := lower $sessionType }}
\\g<indent>{{ $sessionClass := "rt-tryout-session-badge" }}
\\g<indent>{{ if in $sessionTypeLower "formal" }}{{ $sessionClass = printf "%s rt-tryout-session-badge--formal" $sessionClass }}{{ else if in $sessionTypeLower "open" }}{{ $sessionClass = printf "%s rt-tryout-session-badge--open" $sessionClass }}{{ end }}
\\g<indent><div role="cell" data-label="Session">
\\g<indent>  <span class="{{ $sessionClass }}">{{ $sessionType }}</span>
\\g<indent></div>'''

if "rt-tryout-session-badge" not in text:
    pattern = re.compile(
        r'(?P<indent>\s*)<div role="cell" data-label="Session">\s*\n'
        r'\s*<span>\{\{ \.type \}\}</span>\s*\n'
        r'\s*</div>',
        re.MULTILINE,
    )

    new_text, count = pattern.subn(replacement, text, count=0)

    if count == 0:
        pattern = re.compile(
            r'(?P<indent>\s*)<div role="cell" data-label="Session">[\s\S]*?<span>\{\{ \.type \}\}</span>[\s\S]*?</div>',
            re.MULTILINE,
        )
        new_text, count = pattern.subn(replacement, text, count=0)

    if count == 0:
        raise SystemExit(
            "Could not find the Session cell in layouts/partials/page-tryouts.html. "
            "No template changes made."
        )

    layout_path.write_text(new_text)
    print(f"Updated {layout_path}: added session badges to {count} Session cell template block(s).")
else:
    print(f"{layout_path} already contains rt-tryout-session-badge; skipped template update.")

css_path.parent.mkdir(parents=True, exist_ok=True)
css = css_path.read_text() if css_path.exists() else ""

marker = "/* Tryout session type badges */"
if marker not in css:
    css = css.rstrip() + '''

/* Tryout session type badges */
.rt-tryout-session-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 1.75rem;
  padding: .35rem .65rem;
  border: 1px solid rgba(7, 16, 31, .18);
  background: #fff;
  color: var(--rt-navy);
  font-size: .68rem;
  font-weight: 950;
  letter-spacing: .08em;
  line-height: 1;
  text-transform: uppercase;
  white-space: nowrap;
}

.rt-tryout-session-badge--open {
  border-color: rgba(7, 16, 31, .2);
  background: #fff;
  color: var(--rt-navy);
}

.rt-tryout-session-badge--formal {
  border-color: var(--rt-orange);
  background: var(--rt-orange);
  color: #fff;
}

@media (max-width: 980px) {
  .rt-tryout-session-badge {
    width: fit-content;
  }
}
'''
    css_path.write_text(css)
    print(f"Updated {css_path}: added tryout session badge styles.")
else:
    print(f"{css_path} already contains tryout session badge styles; skipped CSS update.")

print("Done. Run: hugo server -D --disableFastRender")
