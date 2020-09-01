# Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_use_product_description_or_name_per_so_line = fields.Boolean(
        "Permite usar name o description_sale en línea de orden de venta",
        implied_group="sale_order_line_description_or_name."
        "group_use_product_description_or_name_per_so_line",
        help="Permite usar o el nombre del producto, o la descripción del "
        " producto. Además puede anteponer el código del mismo"
        )
