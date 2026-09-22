# SPDX-License-Identifier: LGPL-3.0-or-later
# Run in odoo shell against the disposable minimal ZIP-install database only.
import os
assert os.environ.get("MIN_ALLOW_TEST_WRITES") == "1", "Explicit disposable write opt-in required"
assert env.cr.dbname == os.environ.get("MIN_TEST_DB"), "Database must match the explicit disposable target"
module=env['ir.module.module'].search([('name','=','minimalism_theme')])
assert module.state=='installed',module.state
assert env['ir.config_parameter'].sudo().get_param('minimalism_theme.accent_preset')=='blue'
partners=env['res.partner'].search([('name','=','Min lifecycle retained partner')])
assert partners, 'Upgrade lost the unrelated partner'
print('UPGRADE PRESERVED:',module.read(['state','latest_version']), 'Blue preset and partner')
module.button_immediate_uninstall()
env.invalidate_all()
assert module.state=='uninstalled',module.state
assert not env['ir.model.data'].search_count([('module','=','minimalism_theme')])
assert partners.exists(),'Uninstall lost the unrelated partner'
env.cr.commit()
print('PASS: native module uninstall, external IDs removed, unrelated partner retained')
