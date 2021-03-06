# -*- coding: utf-8 -*-


from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.one
    @api.depends('company_id', 'company_id.website', 'image_uri')
    def _get_image_url(self):
        uri = self.image_uri if self.image_uri else ''
        self.image_url =  self.company_id.website + '/image/' + uri
        self.image_tag = """<img src="%s" height="128" width="128"/>""" % (self.image_url,)

    image_uri = fields.Char('Image URI')
    image_url = fields.Char('Image URL', compute='_get_image_url', store=False)
    image_tag = fields.Char('Image tag view', compute='_get_image_url', store=False)
