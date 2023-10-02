# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions




class Department(models.Model):
    _name = "dr_patients.department"
    _description = "Department"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True, unique=True, compute="_compute_code")

    @api.constrains('code')
    def _check_unique_code(self):
        for rec in self:
            if self.search_count([('code', '=', rec.code)]) > 1:
                raise exceptions.ValidationError("Code must be unique.")

    @api.depends('name')
    def _compute_code(self):
        for record in self:
            if record.name:
                record.code = record.name
            else:
                record.code = ''


