from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=True, unique=True)
    user_id = db.Column(db.Integer, nullable=True)
    currency_id = db.Column(db.Integer, nullable=True)
    balance = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'currency_id': self.currency_id,
            'balance': self.balance
        }

class Currency_new(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=True, unique=True)
    currency_name = db.Column(db.String, nullable=True)
    buy = db.Column(db.Integer, nullable=True)
    sale = db.Column(db.Integer, nullable=True)
    available_quantity = db.Column(db.Integer, nullable=True)
    date = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'currency_name': self.currency_name,
            'buy': self.buy,
            'sale': self.sale,
            'available_quantity': self.available_quantity,
            'date': self.date
        }

class Deposits(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=True, unique=True)
    currency_name = db.Column(db.String, nullable=True)
    balance = db.Column(db.Integer, nullable=True)
    interest_rate = db.Column(db.Integer, nullable=True)
    date_of_issue = db.Column(db.String, nullable=True)
    date_of_ixpiry = db.Column(db.String, nullable=True)
    storage_condition = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'currency_name': self.currency_name,
            'balance': self.balance,
            'interest_rate': self.interest_rate,
            'date_of_issue': self.date_of_issue,
            'date_of_ixpiry': self.date_of_ixpiry,
            'storage_condition': self.storage_condition
        }

class Raiting(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=True, unique=True)
    currency_name = db.Column(db.String, nullable=True)
    raiting = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'currency_name': self.currency_name,
            'raiting': self.raiting,
            'comment': self.comment
        }

class Transactions(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=True, unique=True)
    type_of_transaction = db.Column(db.String, nullable=True)
    currency_from_exchange = db.Column(db.String, nullable=True)
    currency_for_exchange = db.Column(db.String, nullable=True)
    date_time = db.Column(db.String, nullable=True)
    currency_spent = db.Column(db.Integer, nullable=True)
    currency_received = db.Column(db.Integer, nullable=True)
    comission = db.Column(db.Integer, nullable=True)
    account_from = db.Column(db.Integer, nullable=True)
    account_for = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'type_of_transaction': self.type_of_transaction,
            'currency_from_exchange': self.currency_from_exchange,
            'currency_for_exchange': self.currency_for_exchange,
            'date_time': self.date_time,
            'currency_spent': self.currency_spent,
            'currency_received': self.currency_received,
            'comission': self.comission,
            'account_from': self.account_from,
            'account_for': self.account_for
        }

class User(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=True, unique=True)
    login = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'password': self.password
        }
