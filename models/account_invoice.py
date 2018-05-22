# -*- coding: utf-8 -*-

from openerp import api, exceptions, fields, models, _
import openerp.addons.decimal_precision as dp
import logging
logger = logging.getLogger(__name__)



##
## Models
##
class AccountInvoice(models.Model):
    _inherit = 'account.invoice'


    @api.one
    @api.depends('invoice_line.price_subtotal', 'tax_line.amount')
    def _compute_amount(self):
        super(AccountInvoice, self)._compute_amount()
        self.register_tax = sum(line.amount if line.name.startswith('Te') else 0 for line in self.tax_line)
        self.amount_tax -= self.register_tax
        logger.info('rt = %s' % self.register_tax)
        self.amount_untaxed += self.register_tax

    register_tax = fields.Float(string='Register Taxe', digits_compute=dp.get_precision('Account'), compute='_compute_amount')



# class mymodel(models.Model):
#     """comment ... """
#     _name = "register_tax.mymodel"
#     _inherit = "..."
#
#     sprint_id = fields.Many2one('project.scrum.sprint', 'Sprint')
#     story_id = fields.Many2one('project.scrum.story', 'Story')
#     feature_id = fields.Many2one('project.scrum.feature', 'Feature')
#     date_start = fields.Datetime('Start date')
