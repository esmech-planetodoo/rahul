from odoo import models, fields, api


class Books(models.Model):
    _name = "book.details"
    _description = "books details"

    library_ids = fields.Many2one('library.details', "book class")

    name = fields.Char("Name")
    author = fields.Char("Author")
    price = fields.Float("Price")
    description = fields.Text("Description")
    availability = fields.Boolean("Is Available")

