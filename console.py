import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()

book1 = Book("Harry Potter", 2001, "JK Rowling")
book_repository.save(book1)
