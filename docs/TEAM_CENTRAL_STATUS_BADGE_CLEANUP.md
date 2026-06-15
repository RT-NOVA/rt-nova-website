# Team Central Status Badge Cleanup

This update removes duplicate status indicators from the Team Central dashboard.

The Current/Upcoming selector now provides the main context, so the table no longer needs:

- Current / Upcoming badge in the season heading
- Active / Past / Upcoming badges beside Spring/Fall headings
- Coming Soon badges
- Status column
- Status badge in every row

The simplified table should read as:

```text
Team | Head Coach | Record | Team Links
```

The CSS also keeps banded rows for readability and preserves mobile stacking behavior.
