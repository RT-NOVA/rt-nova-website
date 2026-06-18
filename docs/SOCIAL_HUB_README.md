# Social Hub Content Guide

The Social Hub is now managed from Hugo content instead of hardcoded homepage cards.

The homepage shows the ordered Social Hub feed three cards at a time. The `/social-hub/` page shows the full archive with tabs:

```text
All | Team News | Facebook | Instagram
```

Local/outside news is included under **Team News** for now.

---

## Content sources

Social Hub cards come from two places:

```text
content/social-hub/
content/news/
```

Use `content/social-hub/` for quick Facebook or Instagram cards that link off-site.

Use `content/news/` for team-news style articles, recaps, announcements, or local coverage you want to treat as team news.

---

## Homepage behavior

The homepage Social Hub uses this order:

1. Items with `pin_to_home_social: true`, newest to oldest.
2. Remaining items, newest to oldest.
3. Only three cards are visible at a time.
4. The Previous/Next buttons switch between groups of three without making the page longer.

Pinned items affect the homepage only. The `/social-hub/` archive stays sorted by date.

---

## Archive behavior

The `/social-hub/` page is generated from:

```text
content/social-hub/_index.md
layouts/social-hub/list.html
```

The archive page is sorted newest to oldest by `date`.

Tabs filter by the normalized item type:

```text
All       = every Social Hub item
Team News = news articles and team-created updates
Facebook  = Facebook cards
Instagram = Instagram cards
```

---

## Add a Facebook card

Create a markdown file under `content/social-hub/`:

```text
content/social-hub/2026-06-15-11u-facebook-photo.md
```

Example:

```yaml
---
title: "11U Team Facebook Photo"
date: 2026-06-15
platform: "Facebook"
account: "Rawlings Tigers NOVA 11U"
link: "https://www.facebook.com/..."
button: "View on Facebook"
image: "/images/social/11u-facebook-photo.jpg"
image_alt: "Rawlings Tigers NOVA 11U team photo"
caption: "11U team update from Facebook. Tap through to view the full post."
build:
  render: never
  list: always
---
```

Keep `build.render: never` for Facebook cards that should appear in the Social Hub but should not create their own page.

---

## Add an Instagram card

Create a markdown file under `content/social-hub/`:

```text
content/social-hub/2026-06-14-instagram-highlight.md
```

Example:

```yaml
---
title: "Instagram Player Highlight"
date: 2026-06-14
platform: "Instagram"
account: "@rawlingstigersnova"
link: "https://www.instagram.com/..."
button: "View on Instagram"
image: "/images/social/instagram-highlight.jpg"
image_alt: "Rawlings Tigers NOVA Instagram player highlight"
caption: "Player highlight from Rawlings Tigers NOVA on Instagram."
build:
  render: never
  list: always
---
```

---

## Add a Team News item

Create a markdown file under `content/news/`:

```text
content/news/2026-06-20-13u-black-runner-up.md
```

Example:

```yaml
---
title: "13U Black Earns Runner-Up Finish"
date: 2026-06-20
show_on_home_social: true
badge: "Runner-Up"
team: "13U Black"
image: "/images/news/13u-black-runner-up.jpg"
image_alt: "Rawlings Tigers NOVA 13U Black runner-up team photo"
excerpt: "13U Black battled through the weekend and earned a runner-up finish."
---

Write the full article body here.
```

Set `show_on_home_social: true` when the article should appear in the homepage Social Hub and on the `/social-hub/` archive.

Do not use `build.render: never` for real team-news articles unless you do not want Hugo to create the article page.

---

## Pin an item to the homepage

Add this to any Social Hub or News item:

```yaml
pin_to_home_social: true
```

Multiple pinned items sort by date, newest first.

If fewer than three items are pinned, the newest unpinned items fill the remaining homepage slots.

---

## Hide an item

Hide a `content/social-hub/` card from the homepage:

```yaml
hide_from_home_social: true
```

Hide a `content/social-hub/` card from the `/social-hub/` archive:

```yaml
hide_from_social_hub: true
```

For `content/news/` items, remove or set this to false if it should not appear in the Social Hub:

```yaml
show_on_home_social: false
```

---

## Do not place assets/layouts under content

Global Hugo files should not live under `content/`.

Wrong:

```text
content/news/assets/js/social-hub.js
content/news/layouts/index.html
```

Correct:

```text
assets/js/social-hub.js
layouts/social-hub/list.html
```

If a previous patch created misplaced folders, remove them:

```bash
python3 scripts/apply-social-hub-page-fix.py
```
