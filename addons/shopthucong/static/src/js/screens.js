odoo.define('shopthucong.screens', function (require) {
"use strict";

var screens = require('point_of_sale.screens');
screens.ProductListWidget.include({
    get_product_image_url: function(product){
        return product.image_url;
    },
});
});

