import re
from odoo import models, fields, api, _
from ..public_class import MainClass
from odoo.exceptions import ValidationError, UserError


class cls_person_files(models.Model):
    _name = 'mdl_person_files'

    fld_file = fields.Binary(string='Upload File')
    name = fields.Char()
    fld_persone_id = fields.Many2one('mdl_persones', ondelete='cascade')
