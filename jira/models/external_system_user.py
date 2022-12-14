from odoo import fields, models


class ExternalSystemUser(models.Model):
    """
    External system user needs for keeping a login and password of user
    to a connection to the server
    """
    _name = 'integration.external_system_user'
    _description = 'External system user'

    name = fields.Char()
    system_id = fields.Many2one(comodel_name='integration.external_system')
    user_id = fields.Many2one(comodel_name='res.users')
    login = fields.Char()
    password = fields.Char()
