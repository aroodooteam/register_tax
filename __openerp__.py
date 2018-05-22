# -*- coding: utf-8 -*-

{
    "name": "Register tax",
    "version": "0.1",
    "author": "Haritiana Rakotomalala <haryoran04@gmail.com>",
    "category": "Tools",
    "complexity": "normal",
    "data": [
        # "data/templates.xml", # un comment to enable js, css code
        # "security/security.xml",
        # "security/ir.model.access.csv",
        "views/account_invoice_view.xml",
        # "actions/act_window.xml",
        # "menu.xml",
        # "data/data.xml",
    ],
    "depends": [
        "base",
        "decimal_precision",
        "account",
    ],
    "qweb": [
        # "static/src/xml/*.xml",
    ],
    "installable": True,
    "auto_install": False,
}
