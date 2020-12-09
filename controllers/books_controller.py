from flask import Flask, render_template, Blueprint
from repositories import author_repository
from repositories import book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html")
# NEW
# GET '/books/new'

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

