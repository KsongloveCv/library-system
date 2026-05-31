from database import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(100))
    publish_date = db.Column(db.String(20))
    isbn = db.Column(db.String(20))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer, default=0)
    description = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Book {self.title}>'
