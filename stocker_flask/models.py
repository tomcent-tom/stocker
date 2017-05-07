# -*- coding: utf-8 -*-
from config import db

# Create your models here.

class Portfolio(db.Model):
    username = db.Column(db.String(200))
    id = db.Column(db.Integer, primary_key=True)

class Purchase(db.Model):
    name = db.Column(db.String(200))
    stock_id = db.Column(db.String(5))
    volume = db.Column(db.Integer)
    price = db.Column(db.Integer)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'),
                            nullable=False)
    portfolio = db.relationship('portfolio',
                               backref=db.backref('purchases'))

