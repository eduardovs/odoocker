from odoo import models, fields, api

class Dog(models.Model):
    _name = 'dog.dog'
    _description = 'Dog Information'

    name = fields.Char(string='Dog Name', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner', required=True)
    breed = fields.Char(string='Dog Breed')
    notes = fields.Text(string='Care Instructions')
    age = fields.Integer(string='Age (Years)')
    image_ids = fields.Many2many('ir.attachment', string='Pictures')
    vaccination_ids = fields.One2many('dog.vaccination', 'dog_id', string='Vaccinations')

    _sql_constraints = [
        ('name_owner_uniq', 'unique(name, owner_id)', 'The combination of dog name and owner must be unique!')
    ]
