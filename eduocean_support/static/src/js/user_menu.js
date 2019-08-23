odoo.define('web_user_menu', function(require) {
    "use strict";

    var UserMenu = require('web.UserMenu');

    UserMenu.include({
        on_menu_documentation: function() {
            window.open('http://doc.dataocean.com/', '_blank');
        },
        on_menu_support: function() {
            window.open('https://www.dataocean.com/page/support', '_blank');
        },
        on_menu_account: function() {
            window.open('https://www.dataocean.com/web/login', '_blank');
        },
    });
});
