from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key_here'

db.init_app(app)
Bootstrap(app)

with app.app_context():
    from models import Book
    db.create_all()

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    
    query = Book.query
    
    if category:
        query = query.filter(Book.category == category)
    
    if search:
        query = query.filter(Book.title.ilike(f'%{search}%') | Book.author.ilike(f'%{search}%'))
    
    pagination = query.order_by(Book.id).paginate(page=page, per_page=10)
    books = pagination.items
    
    categories = Book.query.with_entities(Book.category).distinct().all()
    categories = [c[0] for c in categories]
    
    return render_template('index.html', books=books, pagination=pagination, 
                           category=category, search=search, categories=categories)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('detail.html', book=book)

@app.route('/api/books')
def api_books():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    
    query = Book.query
    
    if category:
        query = query.filter(Book.category == category)
    
    if search:
        query = query.filter(Book.title.ilike(f'%{search}%') | Book.author.ilike(f'%{search}%'))
    
    pagination = query.order_by(Book.id).paginate(page=page, per_page=20)
    books = [{
        'id': b.id,
        'title': b.title,
        'author': b.author,
        'category': b.category,
        'publisher': b.publisher,
        'publish_date': b.publish_date,
        'isbn': b.isbn,
        'price': float(b.price),
        'stock': b.stock,
        'description': b.description
    } for b in pagination.items]
    
    return jsonify({
        'books': books,
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': pagination.page
    })

@app.route('/api/book/<int:book_id>')
def api_book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'category': book.category,
        'publisher': book.publisher,
        'publish_date': book.publish_date,
        'isbn': book.isbn,
        'price': float(book.price),
        'stock': book.stock,
        'description': book.description
    })

if __name__ == '__main__':
    app.run(debug=True)
