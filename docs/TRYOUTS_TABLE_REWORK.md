# Tryouts Schedule-Style Visual Match

This patch tightens the Tryouts age-group schedule area so it visually matches the smaller table sections used on `/schedules/`.

## Changes

- Keeps the Age Group dropdown and search.
- Keeps one section per age group.
- Keeps the requested columns: `SESSION`, `DATE`, `TIME`, `LOCATION`, `MAP`.
- Makes the 14U/13U/12U section headings smaller and closer to the Schedules team headings.
- Moves coach text under the age-group heading instead of as a large right-side label.
- Removes the bullet before `Private Tryouts Upon Request`.
- Uses open rows, thin dividers, and tighter spacing similar to the Schedules page.

## v4 intro text cleanup

Updated the tryout schedule intro to only show: `Players only need to attend one open evaluation unless a coach requests a follow-up.`

## v5 intro text update

Updated the tryout schedule intro to: `Players only need to attend one evaluation or tryout unless otherwise noted`.

## v6 private tryout callout

When an age group has no open evaluations or formal tryouts listed, the fallback row is now a full-width orange callout with:

- `No open evaluations or tryouts currently scheduled`
- `Private Tryouts Upon Request`

## v7 private callout multiline refinement

Adjusted the orange private tryout callout so the notice and action text stack on separate centered lines instead of running together horizontally.

## v8 compact private callout

Reduced the orange private-tryout notice height and shadow, centered both lines, and resized the text so it reads as a compact status notice rather than a large hero banner.

## v9 centered compact callout fix

Ensures every private-tryout fallback callout uses the same inner wrapper and forces the notice to render as two centered lines with reduced height and a smaller headline.

## v10 section sync

Resynced the `Schedule Dates` heading with the rest of the Tryouts page by centering the heading block, matching the section-heading rhythm above it, and keeping only the tools/table/callout area in the wider schedule-style layout.

## v11 section heading match

Adjusted the `Schedule Dates` heading to use the same section-heading size and rhythm as the other Tryouts page sections instead of the larger schedule-hub style.

## v12 global private fallback

Private-only age groups are now hidden from the default all-age view. A single orange global notice appears below any posted tryout sections so families understand that private tryouts may be available for age groups without listed dates. If a parent selects an age group with no posted sessions from the dropdown, that age group still shows its private-tryout notice.

## v13 filter logic fix

Fixes the age-group dropdown logic so age groups with real posted tryout/evaluation dates remain visible in the default `All Age Groups` view, while age groups with only the private fallback are hidden behind the global private-tryout notice. Selecting an age group still shows that age group, including its private fallback when no posted dates exist.

## v14 filter logic rebuild

Rebuilt the Tryouts schedule filtering against the current committed code.

- Dropdown options now come from the age chart plus any explicitly configured age groups.
- Default `All Age Groups` view shows only age groups with real posted tryout/evaluation sessions.
- A global private-tryout notice appears when age groups exist without posted dates.
- Selecting an age group with no posted dates shows that age group with the private fallback notice.
- Age groups present only in the age chart, but not in `groups`, now still appear in the dropdown and get a generated private fallback when selected.

## v15 session type colors

Restored distinct visual treatments for session types so `Formal Tryout`, `Open Evaluations`, and `Private Tryouts` are easier to scan in the table. Formal sessions use the navy treatment, open evaluations use the orange treatment, and private fallback sessions use a muted treatment.

## v16 session text-only styling

Removed the session-type badge backgrounds, left borders, and row tinting. `Formal Tryout` now uses orange text only, while `Open Evaluations` uses normal dark text. Rows remain unshaded.
