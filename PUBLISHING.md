# Packaging and publication

This project currently delivers a local Odoo 19 Community release. GitHub push and Odoo Apps publication have not been performed.

1. Run preference, stylesheet, Python integration and browser suites against disposable Odoo 19 databases. Record the result in `minimalism_theme/VALIDATION.md`.
2. Capture real screens with `npm run capture` and the `MIN_TEST_*` environment variables described in README. Capture writes fictional records and restores the shared Blue preset.
3. Run `node tools/render_icon.cjs` and `npm run render` with Playwright/Chrome and FFmpeg available. All compositions use local real screenshots; no MuK/reference screenshots are reused.
4. Run `npm run build`. The builder validates manifest paths, listing markup, local images, Python/XML syntax and ZIP integrity. It writes a SHA-256 checksum and self-contained listing and thumbnail previews under `dist/`.
5. Inspect both previews at desktop and mobile widths. Build twice and compare checksums before distribution.
6. When publication is requested, create the intended remote and publish a tested `19.0` branch. Recheck current Odoo vendor and submission requirements, register the repository with the publisher account, scan it and inspect the actual public card/detail page.

`cover.gif` is the landscape app cover. `theme_screenshot.gif` is the single manifest image ending in `_screenshot`, selecting the portrait theme catalog card. `theme-preview.png` is only a poster; ordinary screenshots have different names. Do not add competing `_screenshot` entries.

The release ZIP contains only `minimalism_theme/`, including its license and user docs. Development tools, npm dependencies, database storage, logs and source screenshot intermediates are excluded. Preserve third-party notices. No paid metadata or invented support address is supplied.
