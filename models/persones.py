import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from odoo.public_class import MainClass


class cls_persones(models.Model):
    _name = 'mdl_persones'
    _order = "name"
    _sql_constraints = [('unique_persones', 'unique (name)', 'The Persone Is Existe Before'),
                        ('unique_persons_code', 'unique (fld_code_nation)', 'The Code Nation Of Person Is Existe Before')]

    def fnc_renum(self): MainClass().fnc_renum(self)

    def fnc_houseband(self):
        for rcrd in self:
            if rcrd.fld_sones_ids:
                x_str=""
                for rcrds in rcrd.fld_sones_ids:
                    x_adj = ""
                    if rcrds.fld_adj_id: x_adj = rcrds.fld_adj_id.name
                    x_str = x_str + "\n" + rcrds.name + " " + x_adj
                rcrd.fld_houseband = x_str
            else:
                rcrd.fld_houseband = ""

    def fnc_age(self):
        for rcrd in self:
            if rcrd.fld_code_nation:
                rcrd.fld_age = MainClass().fnc_get_age(rcrd.fld_code_nation)
            else:
                rcrd.fld_age = 0

    @api.depends('fld_code_nation')
    def fnc_birth(self):
        for rcrd in self:
            if rcrd.fld_code_nation:
                rcrd.fld_birth = MainClass().fnc_get_brth(rcrd.fld_code_nation)

    @api.depends('fld_code_nation')
    def fnc_gender(self):
        for rcrd in self:
            if rcrd.fld_code_nation:
                rcrd.fld_gender = MainClass().fnc_get_gender(rcrd.fld_code_nation)

    @api.onchange('name')
    def fnc_editstring(self): self.name = MainClass().fnc_editstring(self.name)

    @api.constrains('fld_code_nation')
    def fnc_is_code(self):
        for rcrd in self:
            obj = rcrd.fld_code_nation
            if obj:
                iscode = MainClass().fnc_is_code(obj)
                if not iscode:
                    raise ValidationError(_('The Code Nation Of Son Is Not Correct'))

    @api.onchange('fld_card_name_front', 'fld_card_name_back')
    def fnc_card_name(self):
        self.fld_card_name_front = "A.jpg"
        self.fld_card_name_back = "B.jpg"

    @api.constrains('fld_persone_id')
    def fnc_has_parent(self):
        for rcrd in self:
            if rcrd.fld_persone_id:
                rcrd.fld_zones_id = rcrd.fld_persone_id.fld_zones_id
                rcrd.fld_address = rcrd.fld_persone_id.fld_address
                rcrd.fld_degree = rcrd.fld_persone_id.fld_degree
                if not rcrd.fld_phones:
                    rcrd.fld_phones = rcrd.fld_persone_id.fld_phones

    def chk_fld(self):
        for rcrd in self:
            rcrd.fld_selected = True

    def un_chk_fld(self):
        for rcrd in self:
            rcrd.fld_selected = False

    name = fields.Char(string="Name", required=True, index=True)
    fld_code_nation = fields.Char(string="Code Nation", size=14)
    fld_phones = fields.Text(string="Phones")
    fld_address = fields.Text(string="Address")
    fld_health = fields.Selection([('sc', 'Sick'), ('hn', 'Handicapped')], string="Health")
    fld_health_info = fields.Text(string="Info Of Health")
    fld_social = fields.Selection([('bc', 'Bachelor'), ('mr', 'Married'), ('ab', 'Absolute'), ('wd', 'Widower')], string="Social")
    fld_degree = fields.Selection([('a', 'Strong'), ('b', 'Medium'), ('c', 'Low')], string="Degree")
    fld_sones = fields.Integer(string="Count Of Sones")
    fld_selected = fields.Boolean(string="Selected")
    active = fields.Boolean(default=True)
    fld_notes = fields.Text(string="Notes")
    fld_zones_id = fields.Many2one('mdl_zones', ondelete="set null", string="Zone Name")
    fld_sones_ids = fields.One2many('mdl_persones', 'fld_persone_id', string="Sones Data")
    fld_persone_id = fields.Many2one('mdl_persones', ondelete='cascade', string="Parent Name")
    fld_adj_id = fields.Many2one('mdl_sones_adj', ondelete='set null', string="Adjective")
    fld_kashfs_ids = fields.Many2many('mdl_kashf', string="Kashfs Of Person")
    fld_age = fields.Integer(string='Age', compute='fnc_age')
    fld_birth = fields.Char(string='Birth Date', compute='fnc_birth', store=True)
    fld_gender = fields.Char(string='Gender', compute='fnc_gender', store=True)
    fld_image = fields.Image(max_width=200, max_height=200,store=True)
    fld_card_front = fields.Binary(string='Card Nation Front')
    fld_card_back = fields.Binary(string='Card Nation Back')
    fld_card_name_front = fields.Char()
    fld_card_name_back = fields.Char()
    fld_files_ids = fields.One2many('mdl_person_files', 'fld_persone_id', string="The Files")
    fld_houseband = fields.Char(string='Houseband', compute='fnc_houseband')
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')
