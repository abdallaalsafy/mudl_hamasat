from odoo import models, fields, api, _
from odoo.public_class import MainClass


class cls_sones_adj(models.Model):
    _name = 'mdl_sones_adj'
    _sql_constraints = [('unique_sones_adj', 'unique (name)', 'The Adjective Is Existe Before')]

    def fnc_renum(self): MainClass().fnc_renum(self)

    @api.onchange('name')
    def fnc_editstring(self): self.name = MainClass().fnc_editstring(self.name)

    name = fields.Char(string="Name", required=True, index=True)
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')
