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
eyebrow: 2027 Tryouts
message: Dates & details are now available
link_label: View tryouts
url: /tryouts/
```

Keep the message concise so it remains a single compact line. Use site-relative URLs for internal pages and full `https://` URLs for external destinations.

The bar is intended for time-sensitive program-wide information such as tryouts, registration deadlines, cancellations, or major schedule changes. Disable it when the announcement is no longer current.

## Layout behavior

The announcement is a centered, content-width panel inside the fixed header. It grows naturally with the optional eyebrow, message, and optional link until it reaches the available page width.

- `eyebrow` is optional and acts as the orange category badge, such as `Tryouts`, `Weather`, `Schedule`, or `Program Update`.
- `message` should be short enough to remain readable in the compact bar.
- `url` and `link_label` are optional. When omitted, the message remains centered.
- On narrow screens, the category badge is hidden and the message and link receive the available width.
- The panel is lightly translucent over a hero and becomes solid charcoal after scrolling or on a non-hero page.

## Validation

After changing the announcement:

1. Review the homepage and an inner hero page before and after scrolling.
2. Review a non-hero page to confirm its content begins below the fixed header.
3. Test the mobile menu and announcement at narrow widths.
4. Run `hugo --minify --cleanDestinationDir`.
