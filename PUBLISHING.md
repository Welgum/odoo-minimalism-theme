# Packaging and publication

Source: [Welgum/odoo-minimalism-theme](https://github.com/Welgum/odoo-minimalism-theme). Each Odoo Community version has its own implementation and release branch: `16.0`, `17.0`, `18.0`, `19.0`. `main` follows Odoo 19. Use the branch matching the target server; a manifest version change alone is not a port.

| Odoo | Branch | Odoo Apps repository reference |
| --- | --- | --- |
| 16 | `16.0` | `ssh://git@github.com/Welgum/odoo-minimalism-theme#16.0` |
| 17 | `17.0` | `ssh://git@github.com/Welgum/odoo-minimalism-theme#17.0` |
| 18 | `18.0` | `ssh://git@github.com/Welgum/odoo-minimalism-theme#18.0` |
| 19 | `19.0` | `ssh://git@github.com/Welgum/odoo-minimalism-theme#19.0` |

1. Run preference, stylesheet, Python integration and browser suites against disposable databases of the branch’s Odoo version. Record results in `minimalism_theme/VALIDATION.md`.
2. Capture real screens with `npm run capture` and the `MIN_TEST_*` variables described in README. Capture writes fictional records and restores the shared Blue preset. Never relabel another version’s screenshots.
3. Run `npm run render` with Playwright/Chrome and FFmpeg available. The shared local fox mark and licensed render font live in `tools/branding/`. The renderer derives its version badge from the manifest.
4. Run `npm run build` and `node tools/check_marketplace.cjs`. Check static/local listing HTML, asset paths, Python/XML syntax, every GIF frame, scene/version labels, loop reset, desktop/mobile previews and ZIP integrity. Build twice and compare checksums.
5. Commit and push the matching version branch. For shared fixes, port the behavior while preserving each branch’s bundle names, user service, settings markup, patch API and chart API. Keep `main` and `19.0` aligned.
6. Odoo Apps publication is separate: register the repository with the publisher account, scan each branch and inspect the actual public card/detail page. Check the current official [vendor guidelines](https://apps.odoo.com/apps/vendor-guidelines), [FAQ](https://apps.odoo.com/apps/faq) and [submission instructions](https://apps.odoo.com/apps/upload) first.

`cover.gif` is the landscape app cover. `theme_screenshot.gif` is the sole manifest image ending in `_screenshot`, selecting the portrait catalog card. `theme-preview.png` is its static poster. Do not add competing `_screenshot` entries.

The ZIP contains only `minimalism_theme/`, including its license, notices, documentation and original raster assets. Git metadata, tools, npm packages, fonts, source screenshot intermediates, databases and logs are excluded. No price or unconfirmed support address is supplied. No Odoo Apps scan or publication is claimed by local builds or a Git push.
