# -*- coding: utf-8 -*-
# Copyright 2012-2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{"name": "Multicurrency revaluation",
 "version": "10.0.2.1.0",
 "category": "Finance",
 "summary": "Manage revaluation for multicurrency environment",
 "author": "Camptocamp,Odoo Community Association (OCA)",
 "license": 'AGPL-3',
 "depends": [
     "account_reversal",
     "account_financial_report_qweb",
 ],
 "demo": [
     "demo/account_demo.xml",
     "demo/currency_demo.xml",
 ],
 "data": [
     "views/res_config_view.xml",
     "security/security.xml",
     "views/account_view.xml",
     "wizard/print_currency_unrealized_report_view.xml",
     "wizard/wizard_currency_revaluation_view.xml",
     "report/report.xml",
     "report/unrealized_currency_gain_loss.xml",
 ],
 "tests": [
     "tests/test_currency_revaluation.py",
     "tests/test_currency_revaluation_report.py"
 ],
 'installable': True,
 }
