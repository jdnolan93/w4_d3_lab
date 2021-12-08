from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title, year, author) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.year, book.author]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    pass



def select():
    pass


def delete_all():
    pass


def delete():
    pass


def update():
    pass
