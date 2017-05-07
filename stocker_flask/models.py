# -*- coding: utf-8 -*-
from config import db

# Create your models here.

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    purchases = db.relationship('Purchase', backref='portfolio')

    def __init__(self, username, email):
        self.username = username
        self.email = email

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    stock_id = db.Column(db.String(5))
    volume = db.Column(db.Integer)
    price = db.Column(db.Integer)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))

    def __init__(self, name, stock_id, volume, price, portfolio_id):
        self.name = name
        self.stock_id = stock_id
        self.volume = volume
        self.price = price
        self.portfolio = Portfolio.query.get(portfolio_id)

db.create_all()