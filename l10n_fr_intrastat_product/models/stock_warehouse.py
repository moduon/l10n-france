# Copyright 2010-2022 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, models
from odoo.exceptions import UserError


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    def _get_fr_department(self):
        self.ensure_one()
        if not self.partner_id:
            raise UserError(_("Missing partner on warehouse '%s'.") % self.display_name)
        return self.partner_id.country_department_id
