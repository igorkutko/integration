from odoo import fields, models


class ExternalServiceParameter(models.Model):
    """
    External service parameter keeps additional parameter
    for a method to a connection to the server
    """
    _name = 'integration.external_service_parameter'
    _description = 'External service parameter'

    name = fields.Char()
    service_id = fields.Many2one(comodel_name='integration.external_service')
    value = fields.Char()
    description = fields.Char()
