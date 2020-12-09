from flask import Flask, render_template
from repositories import author_repository
from repositories import book_repository

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)
# NEW
# GET '/books/new'
@books_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_books = authors)

# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'

