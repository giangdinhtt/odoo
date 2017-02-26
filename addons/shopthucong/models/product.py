# -*- coding: utf-8 -*-


from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.one
    @api.depends('company_id.website', 'image_name', 'company_id')
    def _get_image_uri(self):
        print ' in _get_image uri'
        print self.name, self.image_name, self.company_id.website
        self.image_uri = self.company_id.website or '' + '/' + self.image_name
        self.image_url = """<img src="%s" height="128" width="128"/>""" % (self.image_uri,)

    image_uri = fields.Char('Image URL', compute='_get_image_uri', store=True)
    image_url = fields.Char('Image URL tag ', compute='_get_image_uri', store=False)
    image_name = fields.Char('Image name')
