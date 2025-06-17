from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    developer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    price = db.Column(db.Float)
