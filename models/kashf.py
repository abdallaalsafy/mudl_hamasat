# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from ..public_class import MainClass


class cls_kashf(models.Model):
    _name = 'mdl_kashf'
    _rec_name = "fld_sequence"
    _sql_constraints = [('unique_kashf', 'unique (name)', 'The Name Of Kashf Is Exite Before')]

    def fnc_renum(self): MainClass().fnc_renum(self)

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            val['fld_sequence'] = self.env['ir.sequence'].next_by_code('kashf_sqnce_code')
        return super(cls_kashf, self).create(vals)

    name = fields.Char(string="Kashf Name", required=True, index=True)
    fld_info = fields.Text(string="description Of Kashf")
    fld_persons_ids = fields.Many2many('mdl_persones', string="Persones In Kashf")
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')
    fld_sequence = fields.Char(string='Sequence', default=lambda self: _('New'))



