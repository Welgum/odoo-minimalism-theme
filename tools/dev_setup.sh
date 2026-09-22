#!/usr/bin/env bash
# Initialize only this project's disposable local development database.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist/compose/pgdata dist/compose/odoodata
chmod 777 dist/compose/pgdata dist/compose/odoodata
docker compose up -d db
docker compose run --rm odoo odoo -d minimalism19 -i minimalism_theme,contacts,crm,project,calendar --without-demo --stop-after-init
docker compose up -d odoo
