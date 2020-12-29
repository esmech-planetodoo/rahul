from odoo import models, fields, api


class Library(models.Model):
    _name = "library.details"
    _description = "books issued in library details"

    students_ids = fields.One2many('students.details', 'library_ids', "Students")
    books_ids = fields.One2many('book.details', 'library_ids', "Books")

    issue_date = fields.Date("Issue Date")
    return_date = fields.Date("Return Date")
