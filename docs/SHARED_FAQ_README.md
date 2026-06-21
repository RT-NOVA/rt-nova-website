# Shared FAQ Component

Adds a reusable FAQ accordion component for current and future Hugo pages.

## Files

- `layouts/partials/faq-list.html`
- `assets/css/faq.css`
- `layouts/partials/page-tryouts.html`
- `layouts/_default/training-locations.html`
- `assets/css/tryouts.css`
- `assets/css/training-locations.css`

## Usage

Call the partial from any page layout:

```go-html-template
{{ partial "faq-list.html" (dict
  "id" "page-faq"
  "theme" "cream"
  "eyebrow" "Frequently Asked Questions"
  "title" "FAQ"
  "intro" "Optional intro text."
  "items" $data.faq
) }}
```

Each FAQ item should have:

```yaml
- question: "Question text?"
  answer: "Answer text."
```

## Applied pages

- `/tryouts/`
- `/training-locations/`

The component uses a cleaner accordion style with subtle dividers, no heavy card borders, and an orange plus/minus marker.
