from odoo import models, fields

class DogWalk(models.Model):
    _name = 'dog.walk'
    _description = 'Dog Walk Records'

    dog_id = fields.Many2one('dog.dog', string='Dog', required=True)
    walker_id = fields.Many2one('res.partner', string='Walker', required=True)
    date = fields.Datetime(string='Walk Date/Time', required=True, default=fields.Datetime.now)
    image_ids = fields.Many2many('ir.attachment', string='Pictures')
