# Header Navigation Guide

This document explains how the Rawlings Tigers NOVA Hugo site header is managed after the v2 header navigation update.

The header is data-driven from:

```text
data/navigation.yaml
```

Most header changes should be made in that YAML file. You should not need to edit the header HTML, CSS, or JavaScript for normal navigation updates.

---

## Quick start

From a clean local copy of the preview branch:

```bash
git checkout preview
git fetch origin
git reset --hard origin/preview
git clean -f -d
hugo server -D --disableFastRender
```

Edit:

```text
data/navigation.yaml
```

Then restart Hugo if the change does not appear immediately.

---

## Navigation file structure

The header reads from the `main:` section in `data/navigation.yaml`.

Example:

```yaml
main:
  - name: Teams
    url: /teams/
    children:
      - name: Team Central
        url: /teams/
      - name: Accolades
        url: /accolades/
      - name: Coaches
        url: /coaches/
      - name: Schedules
        url: /schedules/

  - name: Tryouts
    url: /tryouts/

  - name: Player Development
    url: /player-development/

  - name: Sponsors
    url: /sponsors/

  - name: Family Hub
    url: /family-hub/
```

---

## Ordering

Items render in the exact order they are listed.

Do not use `weight`.

Good:

```yaml
main:
  - name: Teams
    url: /teams/

  - name: Tryouts
    url: /tryouts/

  - name: Sponsors
    url: /sponsors/
```

Avoid:

```yaml
main:
  - name: Teams
    url: /teams/
    weight: 10
```

---

## Adding a normal top-level link

To add a normal link to the main header, add a new item under `main:`.

Example:

```yaml
main:
  - name: Camps
    url: /camps/
```

A normal top-level item has:

```yaml
name: Page Name
url: /page-url/
```

It does not have `children`.

---

## Adding a dropdown/folder

A top-level item becomes a dropdown automatically when it has `children`.

Example:

```yaml
main:
  - name: Teams
    url: /teams/
    children:
      - name: Team Central
        url: /teams/
      - name: Coaches
        url: /coaches/
```

The parent item still has a `url`. That URL is useful as a fallback and can point to the main landing page for that section.

The dropdown/folder will automatically show a plus sign in the header.

---

## Adding submenu links

Add submenu links under the parent item’s `children:` list.

Example:

```yaml
main:
  - name: Teams
    url: /teams/
    children:
      - name: Team Central
        url: /teams/
      - name: 14U Black
        url: /teams/14u-black/
      - name: 13U Black
        url: /teams/13u-black/
```

Submenu items render in the order listed.

---

## Future nested dropdowns

The Hugo partial is designed so nested `children` can be supported later.

Example structure:

```yaml
main:
  - name: Teams
    url: /teams/
    children:
      - name: 14U
        url: /teams/14u/
        children:
          - name: 14U Black
            url: /teams/14u-black/
          - name: 14U Orange
            url: /teams/14u-orange/
```

The first priority for the current header is a clean first-level dropdown. If deeper nested menus are added later, test desktop and mobile carefully.

---

## Header behavior

The header uses a button-based disclosure navigation pattern.

Dropdown headings render as buttons with:

```html
aria-expanded="false"
aria-controls="..."
```

Behavior:

- Dropdowns are collapsed by default.
- Dropdowns open on hover/focus on desktop.
- Dropdowns open/close on click or tap.
- Only one sibling dropdown should be open at a time.
- Dropdowns close when clicking outside.
- Dropdowns close with Escape.
- Dropdowns close when the cursor leaves the dropdown area on desktop.
- Normal links do not show a persistent active underline.
- Top-level underline appears only on hover, focus, or when the dropdown is open.

---

## Styling notes

The header intentionally uses isolated v2 class names to avoid conflicts with the older header styles.

Main class names:

```text
rt-header
rt-nav
rt-nav__item
rt-nav__link
rt-nav__trigger
rt-nav__dropdown
rt-nav__plus
```

The main header CSS file is:

```text
assets/css/header-nav.css
```

The main header JavaScript file is:

```text
assets/js/header-nav.js
```

The header partial loads these files directly so the header does not depend on changes to the main site asset pipeline.

---

## Changing header text size

Edit:

```text
assets/css/header-nav.css
```

Look for the top-level nav text rule. It should include selectors similar to:

```css
.rt-nav__link,
.rt-nav__trigger,
.rt-nav__utility,
.rt-header-actions__link {
  font-size: .86rem;
}
```

Recommended sizes:

```css
font-size: .86rem;
```

or slightly larger:

```css
font-size: .9rem;
```

Avoid going much larger unless the nav is shortened, because the header can become crowded on tablet and laptop widths.

---

## Changing the plus sign color

Edit:

```text
assets/css/header-nav.css
```

Look for:

```css
.rt-nav__plus {
  color: #fff;
}
```

Recommended current setting:

```css
.rt-nav__plus {
  color: #fff;
}
```

Orange can be used, but white gives the cleaner header style.

---

## Changing underline color

Top-level hover/open underline should be white.

Look for a rule similar to:

```css
.rt-nav__link::after,
.rt-nav__trigger::after {
  background: #fff;
}
```

or hover/open rules that set the underline background.

Recommended:

```css
background: #fff;
```

Avoid bringing back orange underlines unless the design intentionally needs more accent color.

---

## Troubleshooting

### Header change does not show up

Restart Hugo with fast render disabled:

```bash
pkill -f "hugo server" 2>/dev/null || true
hugo server -D --disableFastRender
```

Then hard refresh the browser:

```text
Mac: Cmd + Shift + R
Windows: Ctrl + Shift + R
```

### Dropdown is always open

Check the YAML indentation. A dropdown only works correctly when `children:` is nested under the intended parent item.

Good:

```yaml
main:
  - name: Teams
    url: /teams/
    children:
      - name: Team Central
        url: /teams/
```

Bad:

```yaml
main:
  - name: Teams
    url: /teams/
children:
  - name: Team Central
    url: /teams/
```

### Double underline appears again

This usually means old header CSS is matching the new header elements or a new rule was added that applies a second underline.

Check for duplicate underline methods such as:

```css
border-bottom
text-decoration: underline
box-shadow: inset 0 -2px
::after
```

The v2 header should use one underline system only.

### Orange active underline comes back

Look for rules involving:

```css
.active
.current
[aria-current="page"]
```

The site can keep `aria-current` for accessibility, but it should not create a persistent visual underline in the top-level header.

---

## Files involved

Normal navigation edits:

```text
data/navigation.yaml
```

Header rendering:

```text
layouts/partials/site-header.html
layouts/partials/site-nav-item.html
```

Header styling:

```text
assets/css/header-nav.css
```

Header behavior:

```text
assets/js/header-nav.js
```

Documentation:

```text
docs/header-navigation.md
```

---

## Safe workflow for header updates

Use this workflow before making header changes:

```bash
git checkout preview
git fetch origin
git reset --hard origin/preview
git clean -f -d
hugo server -D --disableFastRender
```

After editing:

```bash
git diff
hugo server -D --disableFastRender
```

When satisfied:

```bash
git add data/navigation.yaml assets/css/header-nav.css assets/js/header-nav.js layouts/partials/site-header.html layouts/partials/site-nav-item.html docs/header-navigation.md
git commit -m "Update header navigation"
git push origin preview
```

Only add the files that actually changed.

---

## Important warnings

Do not place backup files inside:

```text
data/
```

Hugo tries to parse files under `data/`. Files like these can break the build:

```text
data/navigation.yaml.bak
data/navigation.old
data/navigation.backup
```

If you need backups, keep them outside the repo or use Git.

