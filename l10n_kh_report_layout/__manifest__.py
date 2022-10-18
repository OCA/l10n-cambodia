# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
{
    "name": "Cambodia Localization - Account Tax Invoice & Commerical Report Layout",
    "summary": """
            This addon will add two new print options on Customer Invoice,
            follows Cambodia Tax Invoice and Commercial Invoice
        """,
    "version": "14.0.1.0.0",
    "author": "SokreamPhan, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/l10n-cambodia",
    "category": "Localization / Accounting",
    "depends": ["account"],
    "data": [
        "views/res_partner_views.xml",
        "views/report_kh_tax_invoice.xml",
        "views/report_kh_commercial_invoice.xml",
    ],
    "installable": True,
}
