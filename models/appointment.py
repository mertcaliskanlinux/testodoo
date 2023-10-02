from odoo import models, fields, api, exceptions

class Appointment(models.Model):

    _name = "dr_patients.appointment"

    _rec_name = "doctor_full_name"
    
    _description = "Appointment"



    appointment_date_time = fields.Datetime(string="Appointment Date & Time", required=True)
    code = fields.Char(string="Code")
    doctor = fields.Many2one(comodel_name="dr_patients.doctor", string="Doctor", required=True)
    patient = fields.Many2one(comodel_name="dr_patients.patient", string="Patient", required=True)
    stage = fields.Selection(
        string="Stage",
        selection=[('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancel')],
        default='draft',
        required=True
    )
    
    treatment = fields.One2many(
        comodel_name="dr_patients.treatment",
        inverse_name="appointment",
        string="Treatment",
    )
    patient_full_name = fields.Char(string="Patient Name", compute="_compute_patient_full_name", store=True)
    doctor_full_name = fields.Char(string="Doctor Name", compute="_compute_doctor_full_name", store=True)

    @api.depends('patient')
    def _compute_treatment(self):
        for appointment in self:
            if appointment.patient:
                appointment.treatment = appointment.patient.treatment
            else:
                appointment.treatment = False

    def action_set_confirmed(self):
        # Your logic to set the appointment as confirmed goes here
        self.write({'stage': 'confirmed'})

    @api.depends('doctor')
    def _compute_doctor_full_name(self):
        for appointment in self:
            if appointment.doctor:
                appointment.doctor_full_name = appointment.doctor.full_name
            else:
                appointment.doctor_full_name = ""


    @api.depends('patient')
    def _compute_treatment(self):
        for appointment in self:
            if appointment.patient:
                appointment.treatment = appointment.patient.treatment
            else:
                appointment.treatment = False

    def action_set_in_progress(self):
        self.write({'stage': 'in_progress'})

    def action_set_done(self):
        self.write({'stage': 'done'})

    def action_set_draft(self):
        self.write({'stage': 'draft'})
