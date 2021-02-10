from odoo import api, fields, models, _


class Organization(models.Model):
    _name = 'organization.master'
    _description = 'Organization Details'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    client_id = fields.Char("Client")
    organization_id = fields.Char("Organization")
    organization_type = fields.Char("Organization Type")
    general_ledger = fields.Char("General Ledger")
    calender_id = fields.Date("Calendar")
    currency_id = fields.Many2one('res.currency')
    is_active = fields.Boolean("Active")
    is_allowed_period_control = fields.Boolean("Allow Period Control")
    is_ready = fields.Boolean("Ready")
    is_summary = fields.Boolean("Summary Level")
    name = fields.Char("Name")
    social_name = fields.Char("Social Name")
    search_key = fields.Char("Search Key")
    description = fields.Text("Description")
    legal_name = fields.Char("Legal Name")


# FIXME: Complete model and create view for it
class OrganizationInfo(models.Model):
    _name = 'organization.info'
    _description = 'Organization Details'
