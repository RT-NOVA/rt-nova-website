# Tryouts FAQ Notes

The Tryouts FAQ is managed in:

```text
data/tryouts.yaml
```

Look for:

```yaml
faqs:
```

Each item uses:

```yaml
- question: "Question text?"
  answer: "Answer text."
```

The page template reads this list and renders each item in the FAQ accordion. To add, remove, or reorder FAQ entries, edit the `faqs:` list in `data/tryouts.yaml`.
