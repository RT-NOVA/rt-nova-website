# Page flow reference

Use this guide when adding or refreshing a page. It describes the current visual system; it is not a requirement to make every page identical.

## Global frame

1. **Header**
   - Centered Rawlings Tigers NOVA logo on desktop.
   - Transparent over image/dark heroes at the top of the page.
   - Transitions to solid black after scrolling.
   - Compact, scrollable mobile navigation.

2. **Hero**
   - Homepage: tall, image-led, emotional, and limited to a strong headline and primary actions.
   - Program subpages: shorter hero with a clear title and concise lead.
   - Utility pages: a compact dark or text-led header is acceptable when an image adds no value.
   - Transparent headers require one safe-area layer on the actual hero component; do not add spacing to arbitrary children of `main`.

3. **Body sections**
   - Inner pages move directly from the hero into a white primary content section; do not place a proof strip between them.
   - Alternate purposefully between white, cream, dark, orange, and image-led sections after that opening section.
   - Use open rows for schedules, team lists, filters, and operational information.
   - Use cards for people, rosters, social/news posts, and strongly visual destinations.
   - Keep homepage copy concise and direct families to the detailed page.
   - End page content on a non-white section so the global white footer remains visually distinct.

4. **Footer**
   - Global footer remains white so it is consistent on every route.
   - Use subtle structural separation rather than orange gradients or mandatory transition bands.
   - The copyright strip remains black.

## Section color roles

- **Black/charcoal:** header states, the homepage proof band, high-contrast anchors, and the copyright bar.
- **Cream/white:** the default readable content backgrounds.
- **Orange:** primary actions, eyebrows, links, small rules, and meaningful highlights.
- **Images:** emotion, coaching, team culture, competition, and program proof.

Avoid full orange sections as a default. They should be reserved for a rare urgent announcement or campaign. See [`section-color-pattern.md`](section-color-pattern.md) for more detail.

## Recommended page rhythm

```text
Image or dark hero
Primary white content
Image-led or dark feature section
Supporting details, FAQ, directory, or data rows
Non-white final section (cream, dark, orange, or image-led)
White footer
Black copyright strip
```

Do not add a section solely to satisfy the pattern. Each section should answer a visitor question or provide a next action.
The homepage intentionally keeps its dark proof band; this inner-page rule does not apply to it.

## Calls to action

- Orange is for the page's highest-priority action.
- Black or outlined buttons support secondary and social actions.
- Link to detailed pages rather than repeating all team, tryout, location, or family information on the homepage.
- Do not show a registration CTA when registration is not actually available; use a stable information link instead.

## Responsive checks

- Keep hero text below the transparent-header safe area.
- Let wide grids step from three columns to two and then one before content becomes cramped.
- Ensure menus and long pages remain scrollable on mobile.
- Do not solve one page with generic `main > :first-child` selectors.
- Verify linked cards, images, and buttons with mouse, keyboard, and touch-sized layouts.
