# Design and engineering notes

## Visual direction

The primary reference is the local shadcn/ui repository, especially its Button, Input, Table and theme-token design. Minimalism translates that language into Odoo's existing interface: zinc surfaces, 1px separators, medium-weight system typography, 8px controls, 12px cards, small soft shadows and a neutral navigation bar. Blue is the initial action accent. Cards and navigation remain neutral for all seven presets.

Odoo's composite field widgets retain their native geometry and bottom input borders. Giving every nested input a padded rounded rectangle breaks date ranges, relational selectors and editable lists; full boxes belong to native standalone controls and search.

`theme.css` owns screen-scoped semantic tokens. Private SCSS bundles compile native dark styles for installed apps. The graph adapter updates canvas text/grid colors on appearance changes while preserving data-series colors. Status colors are independent of the accent. Focus rings have their own neutral contrast token.

## Independent MuK edge-case review

The MuK reference was inspected for behavior, without copying implementation or assets:

| Observed issue | Minimalism decision |
| --- | --- |
| Systray badges grow after initial navbar measurement | A width observer schedules Odoo's existing menu-fitting algorithm on the next frame; it cleans up on unmount. |
| Narrow navbar and long company names | Allow systray scrolling on mobile while keeping native navigation and dropdown portals. |
| Borderless fields hide required/invalid states | Visible input boundaries; required and invalid states have explicit precedence. |
| Dialog sizing and small screens | Preserve Odoo's modal layout/fullscreen behavior; style surfaces only. |
| Chatter width and form layout changes | Preserve native responsive layout; do not patch form compilation or force a sidebar width. |
| App-menu search and keyboard interaction | Retain the native apps menu, command palette, menu services and hotkeys. |

Minimalism does not include MuK's app launcher, appsbar, chatter resizer, refresh service, group-expansion controls or maximize-dialog feature. These are separate product features rather than requirements for this theme.

## Reused RivetFox foundation

The original theme provides settings persistence, sanitized session data, preference normalization, transactional CSS staging/restoration, Owl controls, graph integration and regression tools. Every live namespace is changed: `minimalism_theme`, `min_`, `o_min_`, `--min-`, `data-min-`, `MIN:APPEARANCE_CHANGED`, and development variables prefixed `MIN_`.

This branch targets Odoo 18 Community. The `16.0`, `17.0`, `18.0` and `19.0` branches adapt native asset bundles, settings markup, user services, patch APIs and chart APIs for each version; `main` follows `19.0`. CSS is screen-only, uses logical properties where direction matters, and avoids changing z-index, scroll ownership, drag transforms or business actions.
