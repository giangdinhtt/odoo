# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from base64 import b64decode
import xlrd
import logging

log = logging.getLogger(__name__)


class ProductUpdate(models.TransientModel):
    _name = 'sp.product.update'

    file_import = fields.Binary('Import')

    @api.multi
    def action_import(self):
        workbook = xlrd.open_workbook(file_contents=b64decode(self.file_import))
        sheet = workbook.sheet_by_index(0)
        header = sheet.row_values(0)
        product_env = self.env['product.product']
        name_index = header.index('name(en)') or -1
        sku_index = header.index('sku') or -1
        price_index = header.index('price') or -1
        image_name_index = header.index('image_name') or -1
        if name_index < 0:
            raise UserError(_('Cannot find column name(en)'))
        if sku_index < 0:
            raise UserError(_('Cannot find column sku'))
        if image_name_index < 0:
            raise UserError(_('Cannot find column image_name'))
        for r in range(1, sheet.nrows):
            row = sheet.row_values(r)
            name = row[name_index]
            sku = row[sku_index]
            image_name = row[image_name_index]
            price = row[price_index] or 0.0
            vals = {'name': name,
                    'default_code': sku,
                    'image_name': image_name,
                    'barcode': sku,
                    'sale_ok': True,
                    'purchase_ok': True,
                    'lst_price': price,
                    'standard_price': price,
                    }
            product_id = product_env.search([('default_code', '=', sku)])
            if product_id:
                product_id.write(vals)
                log.info('Update Product: %s' % (product_id.default_code,))
            else:
                product_id_new = product_env.create(vals)
                log.info('New Product: %s' % (product_id_new.default_code,))
        return True
