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
from datetime import datetime, date

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class FilterRecurringEntries(models.Model):
    _inherit = 'account.move'

    recurring_ref = fields.Char()


class RecurringPayments(models.Model):
    _name = 'account.recurring.payments'

    def _get_next_schedule(self):
        if self.date:
            recurr_dates = []
            today = datetime.today()
            start_date = datetime.strptime(str(self.date), '%Y-%m-%d')
            while start_date <= today:
                recurr_dates.append(str(start_date.date()))
                if self.recurring_period == 'days':
                    start_date += relativedelta(days=self.recurring_interval)
                elif self.recurring_period == 'weeks':
                    start_date += relativedelta(weeks=self.recurring_interval)
                elif self.recurring_period == 'months':
                    start_date += relativedelta(months=self.recurring_interval)
                else:
                    start_date += relativedelta(years=self.recurring_interval)
            self.next_date = start_date.date()

    name = fields.Char('Name')
    debit_account = fields.Many2one('account.account', 'Debit Account',
                                    required=True,
                                    domain="['|', ('company_id', '=', False), "
                                           "('company_id', '=', company_id)]")
    credit_account = fields.Many2one('account.account', 'Credit Account',
                                     required=True,
                                     domain="['|', ('company_id', '=', False), "
                                            "('company_id', '=', company_id)]")
    journal_id = fields.Many2one('account.journal', 'Journal', required=True)
    analytic_account_id = fields.Many2one('account.analytic.account',
                                          'Analytic Account')
    date = fields.Date('Starting Date', required=True, default=date.today())
    next_date = fields.Date('Next Schedule', compute=_get_next_schedule,
                            readonly=True, copy=False)
    recurring_period = fields.Selection(selection=[('days', 'Days'),
                                                   ('weeks', 'Weeks'),
                                                   ('months', 'Months'),
                                                   ('years', 'Years')],
                                        store=True, required=True)
    amount = fields.Float('Amount')
    description = fields.Text('Description')
    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('running', 'Running')],
                             default='draft', string='Status')
    journal_state = fields.Selection(selection=[('draft', 'Unposted'),
                                                ('posted', 'Posted')],
                                     required=True, default='draft',
                                     string='Generate Journal As')
    recurring_interval = fields.Integer('Recurring Interval', default=1)
    partner_id = fields.Many2one('res.partner', 'Partner')
    pay_time = fields.Selection(selection=[('pay_now', 'Pay Directly'),
                                           ('pay_later', 'Pay Later')],
                                store=True, required=True)
    company_id = fields.Many2one('res.company',
                                 default=lambda l: l.env.user.company_id.id)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id.property_account_receivable_id:
            self.credit_account = self.partner_id.property_account_payable_id
