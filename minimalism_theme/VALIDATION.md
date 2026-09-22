# Validation — Minimalism 19.0.1.0.0

Validated on **2026-09-22** against self-hosted **Odoo Community 19.0-20260908** (official `odoo:19.0`, arm64), PostgreSQL **17.7**, and desktop Google Chrome **153.0.8010.53** driven by Playwright **1.58.2**. Node **20.20.0** ran the pure preference tests.

Odoo image digest: `sha256:144175ec0039d52daff1d79f7e51c9281ca3c98b96c830feb49d09764a9f5d7c`.

Two isolated disposable databases were used: `minimalism19` with Contacts, Discuss, CRM, Calendar and Project; and `minimalism19_minimal` installed from the extracted release ZIP with only `minimalism_theme` and its declared dependencies. Neither reference theme was modified.

## Automated results

| Check | Result |
| --- | --- |
| `npm test` | PASS — malformed preferences, preset allowlist, blocked storage reads/writes/property access, user/database isolation, all 14 accent/mode contrasts, legacy cleanup, service races and failed loads. |
| Stylesheet lifecycle browser suite | PASS — inert staging, atomic activation, lazy native assets, exact media restoration, print participation, native-dark baseline restoration, timeout/failure/retry and no duplicate JavaScript. |
| Python settings suite on feature installation | PASS — 5 test methods, 0 failures/errors. All presets round-trip; arbitrary values rejected; corrupt settings sanitized; no global night policy; ordinary users cannot save shared settings. |
| `test_browser.cjs` | PASS — seven presets saved through actual settings UI, 14 mode/preset combinations, unchanged status colors, readable selected/hovered rows, administrator restrictions, employee mode/reload isolation, 390px settings layout, native form labels/chatter, unsaved form retention. |
| `test_night_mode.cjs` | PASS — interrupted CSS load/retry, Discuss/composer/dates, retained draft, emoji picker, semantic notices, Calendar, CRM, Project, settings, bar/line/pie views, live chart labels, pivot, theme disable/re-enable, unchanged global cookie. |
| `test_edge_cases.cjs` | PASS — whitelisted session settings, preserved native session keys, real cross-tab mode/density/disable/reset, reload, all swatches while disabled, navbar refitting after dynamic width growth, 390px CRM, a single search focus ring and input boundary contrast. |
| Extracted-ZIP minimal install | PASS — Python suite (5 methods), two private dark CSS bundles, mode/reload persistence, native light restoration, zero browser errors. Confirmed Contacts, CRM, Project, Calendar and Mail were not installed. |
| Module upgrade | PASS — Python suite (5 methods); shared Blue preset and an unrelated partner retained. |
| Module uninstall | PASS — module uninstalled, owned external IDs removed, unrelated partner retained. |
| Release builder | PASS — metadata and asset paths, local/static listing HTML, PNG/GIF signatures and dimensions, Python/XML syntax, ZIP structure and integrity. |
| Reproducibility | Two consecutive builds of the final source produce the same SHA-256 checksum. See the adjacent `.zip.sha256` file. |
| Preview/media checks | PASS — listing and portrait thumbnail at 1440px and 390px; all images decode and no horizontal overflow. Every GIF frame decoded using FFmpeg. |

Normal text targets **4.5:1** in tested states. Focus indicators and meaningful control boundaries target **3:1**. Measurements include composited backgrounds and opacity in the real-app night suite; this is tested coverage, not a claim of a complete accessibility audit.

## Visual review

Fresh real Odoo captures were reviewed for light/dark Contacts lists, contact form, kanban, Discuss, shared settings and the personal dialog. A 390px CRM capture and desktop/mobile listing and portrait card previews were reviewed. Review led to removal of duplicate composite focus rings and improved offline-member readability in Discuss. Captures show fictional records; optional apps are not dependencies of the theme.

All four GIFs were decoded and their timing checked:

| Asset | Dimensions | Frames | Encoded loop |
| --- | --- | --- | --- |
| `cover.gif` | 1120 × 560 | 90 | 3.00s |
| `theme_screenshot.gif` | 1000 × 1210 | 90 | 3.00s |
| `day-night-demo.gif` | 1120 × 760 | 80 | 2.67s |
| `accent-demo.gif` | 1120 × 760 | 140 | 4.67s |

These are animated comparisons of real captures, not recordings of interactions. The portrait GIF is the sole manifest `_screenshot` candidate.

## Reproduction and evidence

From the repository root, run `npm ci`, then `npm test`. Browser suites use `MIN_TEST_URL`, `MIN_TEST_DB`, `MIN_ALLOW_TEST_WRITES=1` and optional `MIN_CHROME_PATH`; see the root README. Run suites sequentially against each disposable database. `test_minimal.cjs` requires a minimal ZIP-install database. `tools/test_lifecycle.py` is a destructive test of the theme's uninstall only and checks both the database name and explicit test opt-in before running in `odoo shell`.

Python integration: `odoo -d TEST_DB -i minimalism_theme --without-demo --test-enable --test-tags=/minimalism_theme --stop-after-init` (use `-u` for upgrade). Packaging: `python3 tools/build_release.py`. Local preview checks: `node tools/check_previews.cjs`. The Docker development setup is supplied in `compose.yaml` and `tools/dev_setup.sh`.

Local logs and review screenshots remain under ignored `dist/`, including `browser-final.log`, `minimal-install.log`, `minimal-browser.log`, `upgrade.log`, `lifecycle.log`, `capture.log`, `render.log` and the 390px/1440px previews. The first Docker-volume attempt ran out of space; all completed validation used isolated host-backed database and filestore directories, without deleting unrelated Docker data.

## Limits

Only Odoo 19 Community is supported by this release. Enterprise, Odoo.sh, Studio, specialized editors, spreadsheets, RTL, other browser engines and simultaneous backend themes were not validated. Native baseline restoration has a focused browser lifecycle test; a full Enterprise installation with native dark mode was not run. Website, portal, POS, login and PDF reports are outside the backend theme's scope.

The source, ZIP and previews are local. No GitHub push, Odoo Apps scan, public listing or actual marketplace card rendering was performed. The local catalog preview verifies this project's composition only.
