# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    month = db.Column(db.String(10))  # format YYYY-MM


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    description = db.Column(db.String(200))
    month = db.Column(db.String(10))  # YYYY-MM
    date = db.Column(db.Date)
