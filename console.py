import pdb
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Terry", "Pratchet")
author_repository.new_author(author_1)

book_1 = Book("The Colour of Magic", "Fantasy", "Colin Smythe", author_1)
book_repository.new_book(book_1)

author_2 = Author("Candace", "Pert")
author_repository.new_author(author_2)

book_2 = Book("Molecules of Emotion", "Neuroscience", "Simon & Schuster UK", author_2)
book_repository.new_book(book_2)

book_3 = Book("Mort", "Fantasy", "Colin Smythe", author_1)
book_repository.new_book(book_3)

for book in book_repository.select_all():
    print(book.__dict__)
    
# for author in author_repository.select_all():
#     print(author.__dict__)