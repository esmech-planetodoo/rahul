from odoo import models, fields, api


class Library(models.Model):
    _name = "library.details"
    _description = "books issued in library details"

    student_id = fields.Many2one("students.details", "Student Name")

    libraryline_ids = fields.One2many("library.line", 'library_id', "Library Details")


class LibraryLine(models.Model):
    _name = "library.line"
    _description = "class for holding info"
    _rec_name = 'book_id'

    issue_date = fields.Date("Issue Date")
    return_date = fields.Date("Return Date")

    book_id = fields.Many2one('book.details', "Book name")
    library_id = fields.Many2one('library.details', "lib details")
