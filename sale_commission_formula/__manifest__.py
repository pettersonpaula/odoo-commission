# Copyright 2016 Nicola Malcontenti - Agile Business Group
# Copyright 2016 Davide Corio - Abstract
# Copyright 2021 Tecnativa - Pedro M. Baeza
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Commission Formula",
    "version": "15.0.1.0.0",
    "category": "Sale",
    "license": "AGPL-3",
    "summary": "Sale commissions computed by formulas",
    "author": "Abstract,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/commission",
    "depends": ["sale_commission"],
    "data": ["views/sale_commission_view.xml"],
    "demo": ["demo/commission_demo.xml"],
    "assets": {
        "assets_backend": [
            "sale_commission_formula/static/src/css/sale_commission_formula.css"
        ]
    },    
    "installable": True,
}
