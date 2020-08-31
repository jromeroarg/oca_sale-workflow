# Copyright 2013-15 Agile Business Group sagl (<http://www.agilebg.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_use_product_description_or_name_per_so_line = fields.Boolean(
        "Permite usar name o description_sale en línea de orden de venta",
        help="Permite usar o el nombre del producto, o la descripción del "
        " producto. Además puede anteponer el código del mismo"
        )
    group_use_product_description_or_name_per_so_line_selection = fields.Selection([
        ('only_name', 'Solo mostrar el nombre del producto'),
        ('code_name', 'Mostrar [codigo] + nombre del producto'),
        ('only_desc', 'Solo mostrar descripcion_para_ventas del producto'),
        ('code_desc', 'Mostrar [Codigo] + descripcion_para_ventas del producto')
        ], default='only_name')
