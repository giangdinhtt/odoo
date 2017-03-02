odoo.define('shopthucong.models', function (require) {
"use strict";

var module = require('point_of_sale.models');

var models = module.PosModel.prototype.models;
for (var i = 0; i < models.length; i++) {
    var model = models[i];
    if (model.model === 'res.company') {
        // if 'fields' is empty all fields are loaded, so we do not need
        // to modify the array
        if ((model.fields instanceof Array) && model.fields.length > 0) {
            model.fields.push('street');
        }
    } else if (model.model === 'product.product') {
        if ((model.fields instanceof Array) && model.fields.length > 0) {
            model.fields.push('image_uri', 'image_url');
        }
    }
}

var orderModel = module.Order;
var CustomOrderModel = module.Order.extend({
    generate_unique_id: function() {
        // Generates a public identification number for the order.
        // The generated number must be unique and sequential. They are made 12 digit long
        // to fit into EAN-13 barcodes, should it be needed

        function zero_pad(num,size){
            var s = ""+num;
            while (s.length < size) {
                s = "0" + s;
            }
            return s;
        }
        var d = new Date();
        var uid = zero_pad(d.getFullYear() % 100,2) +
               zero_pad(d.getMonth() + 1,2) +
               zero_pad(d.getDate(),2) +
               zero_pad(this.pos.pos_session.id,2) +
               zero_pad(this.sequence_number,3);
        // return addCheckDigit(12 , uid);
        return uid;
    },
    export_for_printing: function() {
        var receipt = orderModel.prototype.export_for_printing.call(this);
        receipt.company.contact_address = this.pos.company.street;
        return receipt;
    }
});
module.Order = CustomOrderModel;

});
