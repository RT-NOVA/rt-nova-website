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

# 1) Remove all hero action buttons from the Coaching Opportunities hero.
# This removes Apply Now, Head Coach PDF, and Assistant Coach PDF from the hero.
text = re.sub(
    r'\n\s+"actions"\s+\(slice[\s\S]*?\n\s+\)',
    '',
    text,
    count=1,
)

# 2) Add role tone classes if not already present.
if 'coaching-role-card--{{ $roleTone }}' not in text:
    text = text.replace(
        '    {{ range $data.roles }}\n      <article class="coaching-role-card">',
        '    {{ range $data.roles }}\n      {{ $roleTone := cond (in (lower .title) "assistant") "assist" "head" }}\n      <article class="coaching-role-card coaching-role-card--{{ $roleTone }}">',
        1,
    )

# 3) Remove Start / Type metadata sub-cards from each role card.
text = re.sub(
    r'\n\s*<dl class="coaching-role-card__meta">[\s\S]*?</dl>',
    '',
    text,
    count=0,
)

# 4) Remove Apply Now buttons from Head Coach / Assistant Coach role cards.
text = re.sub(
    r'\n\s*<a class="rt-btn rt-btn-primary" href="\{\{\s*partial "url\.html" \$\.Site\.Data\.coaching_opportunities\.apply_url\s*\}\}">Apply Now</a>',
    '',
    text,
    count=0,
)
text = re.sub(
    r'\n\s*<a class="rt-btn rt-btn-primary" href="\{\{\s*\$data\.apply_url\s*\}\}">Apply Now</a>',
    '',
    text,
    count=0,
)
text = re.sub(
    r'\n\s*<a class="rt-btn rt-btn-primary" href="\{\{\s*\$\.Site\.Data\.coaching_opportunities\.apply_url\s*\}\}">Apply Now</a>',
    '',
    text,
    count=0,
)

# 5) Differentiate Applies To pills if still using the plain class.
old_pill = '<th><span class="coaching-pill">{{ .applies_to }}</span></th>'
new_pill = '''<th>
              {{ $appliesLower := lower .applies_to }}
              {{ $appliesClass := "coaching-pill" }}
              {{ if in $appliesLower "assistant" }}{{ $appliesClass = printf "%s coaching-pill--assist" $appliesClass }}{{ else if in $appliesLower "head" }}{{ $appliesClass = printf "%s coaching-pill--head" $appliesClass }}{{ else }}{{ $appliesClass = printf "%s coaching-pill--both" $appliesClass }}{{ end }}
              <span class="{{ $appliesClass }}">{{ .applies_to }}</span>
            </th>'''
if old_pill in text:
    text = text.replace(old_pill, new_pill, 1)

# 6) Remove the duplicate "Download the role listings" section.
# The PDF download buttons are already present on the role cards.
text = re.sub(
    r'\n<section class="rt-section rt-section--cream">\s*'
    r'<div class="rt-container rt-section-heading rt-section-heading--center">\s*'
    r'<p class="rt-eyebrow rt-eyebrow--dark">Job Description Downloads</p>[\s\S]*?'
    r'</section>\s*',
    '\n',
    text,
    count=1,
)

layout_path.write_text(text)
print(f"Updated {layout_path}")

css = css_path.read_text()

# Remove the previous top rule that made the third proof item orange.
css = re.sub(
    r'\A\s*/\*[^*]*\*/\s*',
    '',
    css,
    count=0,
)
css = re.sub(
    r'\n?\.coaching-proof-strip \.rt-proof-grid div:nth-child\(3\) strong,\s*'
    r'\n?\.coaching-proof-strip \.rt-proof-grid div:nth-child\(3\) span\s*\{[\s\S]*?\}\s*',
    '\n',
    css,
    count=1,
)

# Remove previous cleanup blocks if rerun.
start = "/* Coaching opportunities cleanup v3 */"
end = "/* End coaching opportunities cleanup v3 */"
css = re.sub(rf"\n?{re.escape(start)}[\s\S]*?{re.escape(end)}\n?", "\n", css)

cleanup_css = r'''
/* Coaching opportunities cleanup v3 */

/* Keep the white quick-facts row consistent. */
.coaching-proof-strip .rt-proof-grid strong,
.coaching-proof-strip .rt-proof-grid span {
  color:#151515 !important;
}

/* Role card differentiation */
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

/* The role-card actions now only contain the PDF download button. */
.coaching-role-card__actions {
  margin-top:auto;
}

.coaching-role-card__actions .coaching-btn-outline {
  width:fit-content;
}

/* Applies To pill differentiation */
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
/* End coaching opportunities cleanup v3 */
'''

css = css.rstrip() + "\n\n" + cleanup_css.strip() + "\n"
css_path.write_text(css)
print(f"Updated {css_path}")

# Verification: avoid reintroducing old navy values in the coaching files.
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
