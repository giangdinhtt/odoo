odoo.define('shopthucong.BaseWidget', function (require) {
"use strict";

var baseWidget = require('point_of_sale.BaseWidget');
baseWidget.include({
    generate_barcode: function (selector, value, barcodeType, settings) {
        // http://www.jqueryscript.net/demo/Simple-jQuery-Based-Barcode-Generator-Barcode/
        var type = barcodeType ? barcodeType : 'code128';
        setTimeout(function() {!settings ? $(selector).barcode(value, type) : $(selector).barcode(value, type, settings);}, 100);
    }
});

});
