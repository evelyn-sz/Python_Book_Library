import pdb
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_1 = Author("Terry", "Pratchet")
author_repository.save(author_1)

book_1 = Book("The Colour of Magic", "Fantasy", "Colin Smythe", author_1)

# for book in book_repository.select_all():
#     print(book.__dict__)
    
for author in author_repository.select_all():
    print(author.__dict__)