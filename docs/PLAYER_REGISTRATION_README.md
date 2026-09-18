# Player registration / Become a Tiger

The `/become-a-tiger/` page embeds the player registration Jotform. Hugo owns the surrounding page; Jotform owns the form fields, conditional logic, submissions, and configured emails.

## Source files

- `content/become-a-tiger.md`: page copy and `jotform_id` / `jotform_url`.
- `layouts/_default/become-a-tiger.html`: page layout and iframe with `data-player-registration`.
- `assets/css/become-a-tiger.css`: page spacing, introductory steps, and iframe wrapper.
- `assets/js/player-registration.js`: forwards a supported age to Jotform.
- `layouts/partials/head/scripts.html`: loads the registration script on this page.

When replacing the form, update both front-matter fields together. The current form ID is `261354423024043`; its URL is `https://form.jotform.com/261354423024043`. The layout also has fallback values, so review those when replacing the form.

## Age preselection

Links such as `/become-a-tiger/?age=11U` preselect the competition age. The script accepts exactly `10U`, `11U`, `12U`, `13U`, and `14U`. Missing or unsupported values leave the configured iframe URL unchanged.

The script writes the accepted value to the iframe URL's `playerCopetition` parameter. This spelling matches the existing Jotform field's unique name; do not correct it in JavaScript unless the field's unique name is also changed in Jotform. Changing only the displayed question label does not require changing this mapping. Existing iframe URL parameters are preserved.

When adding an age or replacing the form, coordinate the tryout age data, this script's allowlist, and Jotform's actual field choices and unique name. See [`TRYOUTS_README.md`](TRYOUTS_README.md) for the links that generate age parameters.

## Styling the embedded form

The Hugo stylesheet controls the outer page and iframe dimensions, not the fields inside Jotform's cross-origin iframe. Edit the Classic Form's internal CSS in Jotform under **Form Designer → Styles → Inject Custom CSS**. Save a backup before replacing the existing custom stylesheet.

Use the site's Inter body font, Oswald display font, black/white/cream surfaces, and orange accents as references. The requested form styling omits the orange bottom border on the black registration heading and the orange left borders on section headings.

For compatibility with Jotform's CSS editor, prefer explicit colors and conventional media queries instead of CSS variables and `clamp()`. Preserve Jotform's conditional visibility, collapse controls, validation, and keyboard focus indicators. Do not force help text visible with opacity or display overrides.

The styling draft prepared outside this repository is not automatically loaded by Hugo and is not a verified record of the CSS currently saved in Jotform. Check the editor before making further changes. The embed uses a fixed height in `assets/css/become-a-tiger.css`, so review scrolling after form layout changes.

## Verification

1. Open the page without an age parameter and confirm the form loads normally.
2. Follow a tryout group's registration button and confirm its age is selected inside Jotform.
3. Check every supported age and an unsupported value; unsupported input should not be forwarded.
4. Preview conditional fields, collapsible sections, focus states, and validation without submitting a real registration.
5. Review desktop, tablet, and mobile widths, including scrolling to the submit button within the embed.
6. For repository changes, run the standard build and validation commands in [`FRONTEND_MAINTENANCE.md`](FRONTEND_MAINTENANCE.md).
