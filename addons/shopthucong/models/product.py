# -*- coding: utf-8 -*-


from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.one
    @api.depends('company_id.website', 'image_name', 'company_id')
    def _get_image_uri(self):
        # print ' in _get_image uri'
        # print self.name, self.image_name, self.company_id.website
        self.image_url = self.company_id.website + '/image/' + self.image_uri
        self.image_tag = """<img src="%s" height="128" width="128"/>""" % (self.image_url,)

    image_uri = fields.Char('Image URI')
    image_url = fields.Char('Image URL', compute='_get_image_uri', store=False)
    image_tag = fields.Char('Image tag view', compute='_get_image_uri', store=False)
