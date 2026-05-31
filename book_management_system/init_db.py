import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from data.books_data import books_data
from models import Book

with app.app_context():
    db.drop_all()
    db.create_all()
    
    for book_data in books_data:
        book = Book(
            title=book_data['title'],
            author=book_data['author'],
            category=book_data['category'],
            publisher=book_data['publisher'],
            publish_date=book_data['publish_date'],
            isbn=book_data['isbn'],
            price=book_data['price'],
            stock=book_data['stock'],
            description=book_data['description']
        )
        db.session.add(book)
    
    db.session.commit()
    print(f"Successfully added {len(books_data)} books to the database.")
