# Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_use_product_descrip_name_per_so_line = fields.Boolean(
        "Usar sólo descripión o nombre del producto en línea de venta",
        help="Permitir usar sólo descricpion o nombre del producto en la linea "
        "de orden de venta, opcionalmente se puede anteponer el [codigo]."
        )
    group_use_product_descrip_name_per_so_line_sel = fields.Selection([
        ('only_name', 'Nombre del producto'),
        ('code_name', '[Codigo] Nombre producto'),
        ('only_desc', 'Descripcion del producto'),
        ('code_desc', '[Codigo] Descripcion producto')
        ])
