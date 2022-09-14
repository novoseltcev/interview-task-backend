from app.db import db


class Currency(db.Model):
    __tablename__ = 'currency'

    num_code = db.Column(db.Integer(), nullable=False, primary_key=True)
    char_code = db.Column(db.String(), nullable=False, unique=True)
    name = db.Column(db.String(), nullable=False)
    value = db.Column(db.Float(), nullable=False)
    nominal = db.Column(db.Integer(), nullable=False)

    def exchange_rate(self):
        return self.value / self.nominal
