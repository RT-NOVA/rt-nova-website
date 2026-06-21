# Coaching Registration Page

Adds a modern `/coaching-registration/` page styled to match the existing `become-a-tiger` registration page.

## Files

- `content/coaching-registration.md`
- `layouts/_default/coaching-registration.html`

## Notes

- Reuses `assets/css/become-a-tiger.css` so the page visually matches the Become A Tiger registration flow.
- Uses the legacy Coaching Registration copy for the intro, three-step checklist, and confirmation note.
- Embeds the coaching registration Jotform configured in front matter:
  - `jotform_id: "253625311709152"`
  - `jotform_url: "https://form.jotform.com/253625311709152"`

## Link updates

- `data/coaching_opportunities.yaml` now sends all Coaching Opportunities `Apply Now` buttons to `/coaching-registration/` instead of the old external TeamLinkt form.
- `data/coaches.yaml` now points the Coaches page CTA directly to `/coaching-registration/`.
- The Coaching Registration page front matter includes `opportunities_url: "/coaching-opportunities/"` for future cross-linking if needed.

## Correct Jotform ID

The embedded Coaching Registration Jotform has been corrected to match the legacy page source:

- Form ID: `261365848367167`
- Embed URL: `https://form.jotform.com/261365848367167`

The earlier `253625311709152` form was not the Coaching Registration form and may show as unavailable.
