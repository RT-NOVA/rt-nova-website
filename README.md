# Rawlings Tigers NOVA Hugo Website

This repository contains the Hugo-based Rawlings Tigers NOVA website.

The site is organized around reusable layouts, Hugo data files, and Markdown content so common updates can be made without editing page HTML.

## Common update locations

| Area | URL | Edit source |
|---|---|---|
| Home | `/` | `layouts/index.html`, `data/homepage.yaml`, `content/social-hub/`, `content/news/` |
| News | `/news/` | `content/news/*.md` |
| Social Hub | Homepage section | `content/social-hub/*.md` and selected news articles |
| Team Central | `/teams/` | `data/teams.yaml` |
| Coaches | `/coaches/` | `data/coaches.yaml` |
| Tryouts | `/tryouts/` | `data/tryouts.yaml` |
| Accolades | `/accolades/` | `data/accolades.yaml` |
| Sponsors | `/sponsors/` | `data/sponsors.yaml` |
| Footer | Site-wide | `data/footer.yaml` |

## Team Central

Team Central is managed from:

```text
data/teams.yaml
```

The current `/teams/` page is focused on current and upcoming teams only. It uses a Current / Upcoming toggle, a black season dashboard header, Spring/Fall subsections, and a compact team table.

For full maintenance instructions, see:

```text
docs/TEAMS_README.md
```

## News and Social Hub

News articles are created under:

```text
content/news/
```

Social-style cards are created under:

```text
content/social-hub/
```

Selected news articles can also appear on the homepage Social Hub by setting the article front matter:

```yaml
show_on_home_social: true
```

Use `content/social-hub/` for Instagram, Facebook, or static update cards that are not full news articles.

## Run locally

Install Hugo Extended, then run:

```bash
hugo server -D
```

Open:

```text
http://localhost:1313/
```

## Build

```bash
hugo --minify
```

Generated output goes to:

```text
public/
```

Do not edit files in `public/` directly.

## Cloudflare Workers build

This site is built through `build.sh` for Cloudflare Workers.

Recommended Cloudflare build settings:

```text
Build command: ./build.sh
Deploy command: npx wrangler deploy
Non-production branch deploy command: npx wrangler versions upload
Root directory: /
```

Recommended variable:

```text
HUGO_VERSION=0.163.0
```

The build script should keep production and preview base URLs consistent for `main` and `preview` branch builds.

## Responsive QA

Before pushing layout changes, check:

```text
390px phone
430px large phone
768px tablet portrait
1024px tablet landscape
1280px desktop
```

Watch for:

```text
No horizontal scrolling
Clean mobile header/nav
Readable homepage Social Hub cards
Readable Team Central tables/cards
Footer stacks cleanly
CTA buttons do not crowd each other
```

## Backup files

Do not leave backup files inside Hugo-managed folders like `data/`, `content/`, or `layouts/`.

Bad example:

```text
data/teams.yaml.bak-teamcentral-selector-cleanup
```

Hugo may try to load these and fail.

Use `.backups/` or another ignored folder instead.
