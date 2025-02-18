from odoo import models, fields, api

class DogVaccination(models.Model):
    _name = 'dog.vaccination'
    _description = 'Dog Vaccination Records'

    dog_id = fields.Many2one('dog.dog', string='Dog', required=True)
    name = fields.Char(string='Vaccine Name', required=True)
    expiration_date = fields.Date(string='Expiration Date', required=True)
    document = fields.Binary(string='Vaccination Document', attachment=True, help='Upload vaccination certificate (PDF or Image)')
