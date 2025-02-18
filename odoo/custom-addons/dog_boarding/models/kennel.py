from odoo import models, fields

class Kennel(models.Model):
    _name = 'dog.kennel'
    _description = 'Kennel Information'

    name = fields.Char(string='Kennel Name', required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Kennel name must be unique!')
    ]
