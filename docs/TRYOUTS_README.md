# Tryouts Page Maintenance

The Tryouts page is rendered from:

```text
data/tryouts.yaml
layouts/partials/page-tryouts.html
assets/css/tryouts.css
```

## Update tryout schedule dates

Edit `data/tryouts.yaml` under `groups:`.

Example:

```yaml
- age_group: Rising 12U
  coach: Ken Torres
  sessions:
    - type: Open Evaluation
      date: Tuesday, May 5, 12, 19, 26
      time: 6:00–8:00 pm
      location: Dale City Recreation Center, Baseball Field 2
```

If a value includes a colon, quote it:

```yaml
coach: "Black: Chris Cheshire · Orange: Tim Jacoby"
```

## Update the age chart

Edit `age_chart.rows` in `data/tryouts.yaml`.

```yaml
age_chart:
  title: 2027 Baseball Age Chart
  rows:
    - age_group: 14U
      birth_window: May 1, 2012 – April 30, 2013
```

## Update FAQ

Edit the `faq:` list in `data/tryouts.yaml`.

```yaml
faq:
  - question: How do I register?
    answer: Use the Become a Tiger registration link on this page.
```
