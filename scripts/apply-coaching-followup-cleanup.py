#!/usr/bin/env python3
from pathlib import Path
import re

layout_path = Path("layouts/partials/page-coaching-opportunities.html")
css_path = Path("assets/css/coaching-opportunities.css")

if not layout_path.exists():
    raise SystemExit(f"Missing {layout_path}")
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}")

text = layout_path.read_text()

# Remove Apply Now from the page hero actions. Keep the two PDF buttons.
text = re.sub(
    r'\n\s*\(dict "label" "Apply Now" "url" \$data\.apply_url "class" "rt-btn-primary"\),?',
    '',
    text,
    count=1,
)

# Add a role tone modifier to each Head/Assistant role card.
if 'coaching-role-card--{{ $roleTone }}' not in text:
    text = text.replace(
        '    {{ range $data.roles }}\n      <article class="coaching-role-card">',
        '    {{ range $data.roles }}\n      {{ $roleTone := cond (in (lower .title) "assistant") "assist" "head" }}\n      <article class="coaching-role-card coaching-role-card--{{ $roleTone }}">',
        1,
    )

# Remove Start / Type sub cards from each role card.
text = re.sub(
    r'\n\s*<dl class="coaching-role-card__meta">[\s\S]*?</dl>',
    '',
    text,
    count=0,
)

# Remove Apply Now button from the Head Coach / Assistant Coach role cards.
text = re.sub(
    r'\n\s*<a class="rt-btn rt-btn-primary" href="\{\{ partial "url\.html" \$\.Site\.Data\.coaching_opportunities\.apply_url \}\}">Apply Now</a>',
    '',
    text,
    count=0,
)
text = re.sub(
    r'\n\s*<a class="rt-btn rt-btn-primary" href="\{\{ \$\.Site\.Data\.coaching_opportunities\.apply_url \}\}">Apply Now</a>',
    '',
    text,
    count=0,
)
text = re.sub(
    r'\n\s*<a class="rt-btn rt-btn-primary" href="\{\{ \$data\.apply_url \}\}">Apply Now</a>',
    '',
    text,
    count=0,
)

# Add differentiated classes to the Applies To pills in the expectation table.
old_pill = '<th><span class="coaching-pill">{{ .applies_to }}</span></th>'
new_pill = '''<th>
              {{ $appliesLower := lower .applies_to }}
              {{ $appliesClass := "coaching-pill" }}
              {{ if in $appliesLower "assistant" }}{{ $appliesClass = printf "%s coaching-pill--assist" $appliesClass }}{{ else if in $appliesLower "head" }}{{ $appliesClass = printf "%s coaching-pill--head" $appliesClass }}{{ else }}{{ $appliesClass = printf "%s coaching-pill--both" $appliesClass }}{{ end }}
              <span class="{{ $appliesClass }}">{{ .applies_to }}</span>
            </th>'''
if old_pill in text:
    text = text.replace(old_pill, new_pill, 1)

layout_path.write_text(text)
print(f"Updated {layout_path}")

css = css_path.read_text()

# Remove prior follow-up block if re-run.
start = "/* Coaching opportunities follow-up cleanup */"
end = "/* End coaching opportunities follow-up cleanup */"
css = re.sub(rf"\n?{re.escape(start)}[\s\S]*?{re.escape(end)}\n?", "\n", css)

cleanup_css = r'''
/* Coaching opportunities follow-up cleanup */
.coaching-role-card--head .coaching-role-card__badge {
  background:rgba(246,95,22,.09);
  color:var(--rt-orange-dark);
  border-color:rgba(246,95,22,.32);
}

.coaching-role-card--assist .coaching-role-card__badge {
  background:#0b0b0d;
  color:#fff;
  border-color:#0b0b0d;
}

.coaching-role-card--head .coaching-role-card__short {
  color:var(--rt-orange);
}

.coaching-role-card--assist .coaching-role-card__short {
  color:#0b0b0d;
  opacity:.92;
}

.coaching-role-card__actions {
  margin-top:auto;
}

.coaching-role-card__actions .coaching-btn-outline {
  width:fit-content;
}

.coaching-pill--head {
  background:rgba(246,95,22,.09);
  color:var(--rt-orange-dark);
  border-color:rgba(246,95,22,.32);
}

.coaching-pill--assist {
  background:#0b0b0d;
  color:#fff;
  border-color:#0b0b0d;
}

.coaching-pill--both {
  background:#f4eee6;
  color:#151515;
  border-color:rgba(5,5,5,.16);
}

@media (max-width:720px){
  .coaching-role-card__actions .coaching-btn-outline{
    width:100%;
  }
}
/* End coaching opportunities follow-up cleanup */
'''

css = css.rstrip() + "\n\n" + cleanup_css.strip() + "\n"

css_path.write_text(css)
print(f"Updated {css_path}")

# Audit the changed files for the old navy colors/patterns that caused the prior issue.
bad_patterns = [
    "#061120", "#0c1b2e", "#07101f", "#07111f", "#080f1b", "#0f172a",
    "rgba(6,17,32", "rgba(6, 17, 32",
    "rgba(3,10,20", "rgba(3, 10, 20",
    "rgba(8,15,27", "rgba(8, 15, 27",
    "rgba(7,16,31", "rgba(7, 16, 31",
    "navy",
]

hits = []
for path in [layout_path, css_path]:
    body = path.read_text(errors="ignore")
    for i, line in enumerate(body.splitlines(), start=1):
        low = line.lower()
        if any(pattern.lower() in low for pattern in bad_patterns):
            hits.append(f"{path}:{i}: {line.strip()}")

if hits:
    print("\nWARNING: possible old navy references found:")
    for hit in hits:
        print(hit)
    raise SystemExit(2)

print("Verified: no old navy hex/rgba values or 'navy' text were introduced in the changed coaching files.")
print("Run: hugo server -D --disableFastRender")
