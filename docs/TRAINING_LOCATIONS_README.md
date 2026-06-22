# Training Locations Specific Facility Update

This update removes generic location language and keys the page around actual Rawlings Tigers NOVA training locations.

## Outdoor fields

- Veterans Memorial Park — Field 4
- Eagle Field at Neabsco / Neabsco Eagles Field

## Winter facilities

- D-BAT Manassas
- Metro Baseball Facility

## Notes

- The D-BAT logo is included as a local static asset at `static/images/training-locations/dbat-logo.webp`.
- Location cards now support address, field name, map links, and facility links.
- The expectation/parent planning feature list is now data-driven from `data/training_locations.yaml`.

## v6 template scope fix

Fixed the Hugo template scope bug in the winter facility logo block. The template now captures each facility as `$facility` before entering `with $facility.logo`, so the image alt text can reference `$facility.name` safely.

## v7 copy and facility card refinement

- Condensed the parent-planning copy and removed specific field names from that intro text.
- Restored the top proof-strip labels/values requested by the program.
- Updated Veterans Memorial Park Field 4 address to `14300 Veterans Dr, Woodbridge, VA 22191`.
- Removed `Facility Info` links from outdoor field cards while keeping map links.
- Added Veterans Community Center to the winter training facilities using the same Veterans Memorial Park address.
- Made the D-BAT logo presentation transparent instead of sitting on a white logo card.

## Outdoor field grid

- Outdoor section title is `Outdoor Field Locations`.
- Outdoor cards use a responsive grid: 3 cards render in one row on desktop; 4 cards render in a 2x2 pattern.
