# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.public_class import MainClass


class cls_zones(models.Model):
    _name = 'mdl_zones'
    _sql_constraints = [('unique_zones', 'unique (name)', 'The Zone Is Exite Before')]

    def fnc_renum(self): MainClass().fnc_renum(self)

    @api.onchange('name')
    def fnc_editstring(self): self.name = MainClass().fnc_editstring(self.name)

    name = fields.Char(string="ZnName", required=True, index=True)
    fld_info = fields.Text(string="description Of Zones")
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')



