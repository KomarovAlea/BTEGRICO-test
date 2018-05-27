# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.tools.translate import html_translate


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    website_features = fields.Html('Features description for the website', sanitize_attributes=False, translate=html_translate)
    website_composition = fields.Html('Composition description for the website', sanitize_attributes=False, translate=html_translate)
    website_using = fields.Html('Using description for the website', sanitize_attributes=False, translate=html_translate)
