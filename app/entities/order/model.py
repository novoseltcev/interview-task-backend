from app.db import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    num_order = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    rubble_cost = db.Column(db.Float, nullable=False)
