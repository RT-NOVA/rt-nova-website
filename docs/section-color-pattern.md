# Rawlings Tigers NOVA Section Color Pattern

Use this as a planning guide for future page redesigns so the site feels consistent across Home, About, Teams, Accolades, Tryouts, Coaches, and Social Hub pages.

## Core roles

- **Black / charcoal**: structure, contrast, anchors, high-impact bands, navigation, the homepage proof band, footer copyright, and important section breaks.
- **Cream / warm white**: default content background for readable parent-facing information, cards, forms, bios, FAQs, and footer content.
- **Rawlings orange**: actions and emphasis. Use for primary buttons, small labels, hover states, thin accents, highlighted text links, and warm transitions. Avoid large full-orange sections unless the message is urgent or temporary.
- **Images**: emotion and proof. Use for heroes, Program Focus cards, team pages, player highlights, accolades, and social previews.

## Recommended page rhythm

1. **Image hero**  
   Large photo, white headline, minimal copy, clear primary action.

2. **White primary section**
   Inner pages move directly into their main task or explanation. Relevant facts belong with the section that explains them rather than in a separate proof strip.

3. **Cream information section**  
   Supporting explanation, family/program details, or cards.

4. **Image/card section**  
   Visual navigation, program highlights, team images, coach photos, or accolade previews.

5. **Cream detail section**  
   Supporting information, FAQs, locations, rosters, schedules, or forms.

6. **Non-white final section**
   End page content on cream, dark, orange, or an image-led treatment so it remains distinct from the footer.

7. **White footer**  
   Contact, resources, logo, and social links.

8. **Black copyright bar**  
   Simple legal/credits row.

## When to use black sections

Use black or charcoal when the section needs strength or contrast:

- The homepage proof band
- Tryout registration highlights
- Tournament/accolade feature bands
- Schedule or result emphasis blocks
- Page breaks between image-heavy and text-heavy areas
- Footer copyright area

## When to use orange

Use orange as an accent, not the default background:

- Primary buttons such as View Teams or Become A Tiger
- Eyebrow labels
- Important hover states
- Small badges
- Text links that need emphasis

Large orange blocks should be rare and reserved for urgent tryout deadlines, registration alerts, or special announcements.

## When to use cream

Cream should carry most of the site:

- Local Roots / National Standards
- Program explanations
- Coach bios
- Parent/family information
- Team details
- Social Hub background
- Footer content

## Homepage pattern

Current homepage target pattern:

1. Transparent-header image hero
2. Dark proof strip
3. Program Focus image cards
4. Player Development Pathway and competitive-team proof
5. Centered Local Roots section
6. Social Hub cream section
7. White Brick-style footer
8. Black copyright bar


## Footer Baseline

Use a clean white footer on every page. Do not use a full orange footer, an orange divider band, or an orange-to-cream fade. The page's final content section should be non-white, while the footer uses its subtle charcoal top border, soft upward shadow, clear vertical spacing, and black copyright bar. Orange should remain a link/button accent only.

## Inner-page baseline

Inner pages use this shared rhythm:

1. Transparent-header hero where appropriate
2. White primary content section
3. Alternating supporting sections chosen for content and contrast
4. Non-white final content section
5. White footer
6. Black copyright bar

Do not add a proof or quick-facts strip between an inner-page hero and its primary content. If a fact is important, place it in the section where visitors act on or understand it. The homepage dark proof band is an intentional exception.

## Inner Page Transparent Header Routes

The homepage uses the largest visual hero. Core inner pages may still use the transparent header at first load, but with a shorter/smaller hero treatment and enough top safe space for the centered logo/nav stack.

Current transparent-header inner routes:

- `/about/`
- `/become-a-tiger/`
- `/coaching-opportunities/`
- `/tryouts/`
- `/accolades/`
- `/coaches/`
- `/schedules/`
- `/watch-now/`
- `/training-locations/`

Utility pages such as icon credits, tags, categories, and other low-visual pages should keep the solid black header instead of using the transparent overlay treatment.


## Transparent header repair note

The following inner pages are intentionally treated like hero pages at first load so the header starts transparent and becomes solid black after scrolling: `/about/`, `/become-a-tiger/`, `/coaching-opportunities/`, `/tryouts/`, `/accolades/`, `/coaches/`, `/schedules/`, `/watch-now/`, and `/training-locations/`.

For these pages, the first hero/masthead section must include enough top safe space for the full centered-logo header stack. Later page-specific CSS should not remove the inner hero safe-area rules in `assets/css/hero-natural-reset.css`.
