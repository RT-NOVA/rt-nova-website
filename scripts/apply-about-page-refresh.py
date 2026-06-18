from pathlib import Path

root = Path.cwd()

about_md = root / "content" / "about.md"
about_md.write_text('''---
title: "About Rawlings Tigers NOVA"
summary: "Rawlings Tigers NOVA is a Northern Virginia travel baseball program focused on player development, professional coaching, competitive schedules, and team-first culture."
template: "about"
---
''')

partial_src = root / "layouts" / "partials" / "page-about.html"
if not partial_src.exists():
    raise SystemExit("Missing layouts/partials/page-about.html from patch extraction")

single = root / "layouts" / "_default" / "single.html"
text = single.read_text()
needle = '{{ else if eq $template "accolades" }}{{ partial "page-accolades.html" . }}'
insert = needle + '\n  {{ else if eq $template "about" }}{{ partial "page-about.html" . }}'
if '{{ partial "page-about.html" . }}' not in text:
    if needle not in text:
        raise SystemExit("Could not find template switch location in layouts/_default/single.html")
    text = text.replace(needle, insert, 1)
    single.write_text(text)
    print("Updated layouts/_default/single.html to route template: about")
else:
    print("layouts/_default/single.html already routes template: about")

print("Updated content/about.md and installed layouts/partials/page-about.html")
