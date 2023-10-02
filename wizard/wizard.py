from odoo import models, fields, api


class AppointmentWizard(models.TransientModel):
    _name = 'dr_patients.appointment.wizard'
    _description = 'Create Appointment Wizard'

    patient = fields.Many2one('dr_patients.patient', string='Patient', required=True)
    doctor = fields.Many2many('dr_patients.doctor', string='Doctors')
    code = fields.Char(string='Code', required=True)

    def create_appointment(self):
        # Sihirbazdan alınan bilgileri kullanarak randevu oluşturun
        # Seçilen doktorlar ve hastanın adını kullanarak bir randevu oluşturun.
        appointment_vals = {

            'patient': self.patient.id,
            'doctor': [(6, 0, self.doctor.ids)],
            'code': self.code,
            'stage': 'draft',
            # Diğer gerekli alanlar...
        }
        self.env['dr_patients.appointment.wizard'].create(appointment_vals)