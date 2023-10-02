# -*- coding: utf-8 -*-


from odoo import models, fields, api,exceptions

class Doctor(models.Model):

    _name="dr_patients.doctor"
    _description="Doctor"
    _rec_name="full_name"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full Name",)
    date_of_birth = fields.Date(string="Date of Birth", required=True)
    age = fields.Integer(string="Age", readonly=True, compute="_compute_age")
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True,unique=True)
    department  = fields.Many2one(comodel_name="dr_patients.department", string="Department")

    shift_start = fields.Float(string="Shift Start", required=True, widget='float_time')
    shift_end = fields.Float(string="Shift End", required=True, widget='float_time')

    @api.constrains('email')
    def _check_unique_email(self):
        for rec in self:
            if self.search_count([('email', '=', rec.email)]) > 1:
                raise exceptions.ValidationError("Email address must be unique.")
            

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                # Burada yaş hesaplaması yapılır (örneğin, günümüz tarihinden doğum tarihini çıkararak)
                # Sonucu 'age' alanına kaydedebilirsiniz.
                # Örnek kod:
                today = fields.Date.today()
                birth_date = fields.Date.from_string(record.date_of_birth)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

                