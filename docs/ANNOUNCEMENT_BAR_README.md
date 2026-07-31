# Announcement Bar

The global announcement bar is configured in:

```text
data/announcement.yaml
```

It appears directly below the fixed header and remains visible while visitors scroll. Header offsets, page-hero safe areas, mobile navigation, non-hero pages, and schedule anchors account for the announcement height.

## Enable or disable

```yaml
enabled: true
```

Change `enabled` to `false` to remove the bar everywhere. No empty space remains when it is disabled.

## Content

```yaml
aria_label: Important tryout information
eyebrow: Tryouts
message: 2027 dates & details are available
mobile_message: 2027 details are available
url: /tryouts/
```

Keep the message concise. It remains a single compact line on desktop and may wrap on tablet or mobile. The optional `mobile_message` replaces it at narrower widths; when omitted, mobile automatically reuses `message`. Use site-relative URLs for internal pages and full `https://` URLs for external destinations.

The bar is intended for time-sensitive program-wide information such as tryouts, registration deadlines, cancellations, or major schedule changes. Disable it when the announcement is no longer current.

## Layout behavior

The announcement is a centered, content-width panel inside the fixed header. It grows naturally with the optional eyebrow, message, and optional link until it reaches the available page width.

- `eyebrow` is optional and acts as the orange category badge, such as `Tryouts`, `Weather`, `Schedule`, or `Program Update`.
- `message` should be concise enough to remain readable in the compact notice. It can wrap on tablet and mobile instead of being truncated.
- `mobile_message` is optional. Use it only when the desktop message needs a shorter mobile version; otherwise omit it to keep one source of wording.
- `url` is optional. When present, the entire notice becomes one large navigation target and displays an arrow. No separate link label is needed.
- When `url` is omitted, the notice remains informational and does not show link behavior or an arrow.
- On tablet and mobile, the category badge remains visible while the message wraps within the available width.
- The mobile notice is slightly taller than the desktop notice so longer messages remain readable without overlapping the page hero.
- The panel is lightly translucent over a hero and becomes solid charcoal after scrolling or on a non-hero page.

## Writing guidance

Because the whole notice is clickable, write the message so its destination is understandable without a separate call-to-action label. Examples:

```yaml
eyebrow: Tryouts
message: 2027 dates, locations, and registration details are available
mobile_message: 2027 details are available
url: /tryouts/
```

```yaml
eyebrow: Weather
message: Tonight's outdoor practices have moved indoors
url: /schedules/
```

Use `aria_label` to describe the purpose of the region for assistive technology. It does not appear visually.

## Validation

After changing the announcement:

1. Review the homepage and an inner hero page before and after scrolling.
2. Review a non-hero page to confirm its content begins below the fixed header.
3. Test the mobile menu and announcement at narrow widths.
4. Run `hugo --minify --cleanDestinationDir`.
