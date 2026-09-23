# Technical Specs Appendix (SE-level detail, kept separate from interview narrative)

Granular product specs that go deeper than what's needed for the account-manager interview conversation. Reference only if a technical/deployment question comes up.

## HPE Alletra Storage MP X10000 — physical dimensions

Built on the common HPE Alletra Storage MP 2U Chassis (shared enclosure across the MP platform's block and object/file node types — B10000 and X10000 differ by software/node role, not by enclosure).

| Spec | Value |
|---|---|
| Height | 3.44 in / 87.5 mm (2U) |
| Width | 19.00 in / 483 mm |
| Depth | 33.11 in / 841 mm |
| Weight | 74.0 lbs / 33.6 kg (base enclosure: enclosure + 2 controller IOMs + 2 power supplies + 1 CDM, no drives/HBAs) |

Scales up to 16 nodes per system — a maximum config consumes up to 32U of rack space, close to a full standard 42U rack once switching/patch space is added. Relevant if a conversation ever gets into physical footprint at Comcast's regional edge facilities, where rack/power/cooling space per site is a real constraint.
