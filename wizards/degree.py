import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from ..public_class import MainClass

class cls_persones(models.TransientModel):
    _name = 'wzrd_degree'

    def fnc_degree(self):
        x_ids = self.env['mdl_persones'].browse(self._context.get('active_ids'))
        for rcrd in x_ids:
            rcrd.fld_degree = self.fld_degree

    fld_degree = fields.Selection([('a', 'Strong'), ('b', 'Medium'), ('c', 'Low')], string="Degree")
