# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Odoo 13 Full Accounting Kit',
    'version': '13.0.1.3.1',
    'category': 'Accounting',
    'summary':  """ This Module will bring back the accounting features such  
                    Asset Management, Budget Management,  Accounting Reports, 
                    PDC Management, Account Lock dates, Customer Credit Limit 
                    and Follow Ups, Day book, Bank book and Cash book reports. 
                """,
    'description':  """
                    Odoo 13 Accounting,Accounting Reports, Odoo 13 Accounting 
                    PDF Reports, Asset Management, Budget Management, 
                    Customer Credit Limit, Recurring Payment,
                    PDC Management, Customer Follow-up,
                    Lock Dates into Odoo 13 Community Edition, 
                    Odoo Accounting,Odoo 13 Accounting Reports,Odoo 13,, 
                    Full Accounting, Complete Accounting, 
                    Odoo Community Accounting, Accounting for odoo 13, 
                    Full Accounting Package, 
                    Financial Reports, Financial Report for Odoo 13
                    """,
    'author': ' Odoo SA,Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'account', 'sale', 'account_check_printing',
                'base_account_budget'],
    'data': [
        'security/ir.model.access.csv',
        'security/account_asset_security.xml',
        'data/account_financial_report_data.xml',
        'data/cash_flow_data.xml',
        'data/account_pdc_data.xml',
        'data/followup_levels.xml',
        'data/account_asset_data.xml',
        'views/reports_config_view.xml',
        'views/accounting_menu.xml',
        'views/credit_limit_view.xml',
        'views/account_configuration.xml',
        'views/account_payment_view.xml',
        'views/res_config_view.xml',
        'views/recurring_payments_view.xml',
        'views/account_followup.xml',
        'views/followup_report.xml',
        'wizard/asset_depreciation_confirmation_wizard_views.xml',
        'wizard/asset_modify_views.xml',
        'views/account_asset_views.xml',
        'views/account_move_views.xml',
        'views/account_asset_templates.xml',
        'views/product_template_views.xml',
        'wizard/financial_report.xml',
        'wizard/general_ledger.xml',
        'wizard/partner_ledger.xml',
        'wizard/tax_report.xml',
        'wizard/account_lock_date.xml',
        'wizard/trial_balance.xml',
        'wizard/aged_partner.xml',
        'wizard/journal_audit.xml',
        'wizard/cash_flow_report.xml',
        'wizard/account_bank_book_wizard_view.xml',
        'wizard/account_cash_book_wizard_view.xml',
        'wizard/account_day_book_wizard_view.xml',
        'wizard/recurring_payments_wizard.xml',
        'report/report_financial.xml',
        'report/general_ledger_report.xml',
        'report/report_journal_audit.xml',
        'report/report_aged_partner.xml',
        'report/report_trial_balance.xml',
        'report/report_tax.xml',
        'report/report_partner_ledger.xml',
        'report/cash_flow_report.xml',
        'report/account_bank_book_view.xml',
        'report/account_cash_book_view.xml',
        'report/account_day_book_view.xml',
        'report/account_asset_report_views.xml',
        'report/report.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': False,
}