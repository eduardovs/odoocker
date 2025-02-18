from odoo import models, fields, api

class Booking(models.Model):
    _name = 'dog.booking'
    _description = 'Dog Boarding Booking'

    dog_id = fields.Many2one('dog.dog', string='Dog', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner', related='dog_id.owner_id', store=True)
    dropoff_datetime = fields.Datetime(string='Drop-off Date/Time', required=True)
    pickup_datetime = fields.Datetime(string='Pick-up Date/Time', required=True)
    kennel_id = fields.Many2one('dog.kennel', string='Kennel')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', required=True)

    @api.constrains('dropoff_datetime', 'pickup_datetime')
    def _check_dates(self):
        for booking in self:
            if booking.dropoff_datetime and booking.pickup_datetime:
                if booking.dropoff_datetime >= booking.pickup_datetime:
                    raise models.ValidationError('Pick-up date must be after drop-off date')
