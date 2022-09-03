from flask import Flask, request

app = Flask(__name__)

import sqlite3
import datetime
from models import db
from models import Account, Currency_new, Deposits, Raiting, Transactions, User

datetime.datetime.now().strftime("%d-%m-%y")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# @app.route('/test')
# def test():
#     user_1_balance = Account.query.filter_by(user_id="1", currency_id="usd").first()
#     user_1_balance.balance = 500
#     db.session.commit()
#     return f"{result}"
#
# @app.route("/currency/rewiew")#Відображати перелік УСІХ валют
# def show_currency_list():
#      result = Currency_new.query.all()
#      return f"{result}"
#
# @app.route("/currency/<currency_name>/rewiew")#Відображати перелік ОДНІЄЇ валюти
# def show_currency_list2():
#      result = Currency_new.query.filter_by(currency_name="currency_name").first()
#      return f"{result}"

@app.route("/user/deposit")#Депозити юзера
def user_deposit_id():
    result = Deposits.query.all()
    return f"{result}"

# def get_data(querry: str): #"так виглядає коментарі аргумента"
#     conn = sqlite3.connect('db.db')
#     cursor = conn.execute(querry)
#     result = cursor.fetchall()
#     conn.close()
#     return result

# @app.get("/currency/<currency_UPS>")
# def currency_list(currency_UPS):
#     # result=get_data(f"select * from Currency where currency_name='{currency_UPS}'")
#     res = Currency.query.filter_by(currency_name=f'{currency_UPS}').first()
#     return f"{res}"
# #


# @app.get("/currency/trade/<currency_UPS1>/<currency_UPS2>")#
# def get_trade(currency_UPS1, currency_UPS2):
#     amount = 50
#     cur_price2 = Currency_new.query.filter_by(currency_name="eur").first()
#     # cur_price2 = Currency.query.filter_by(currency_name=f"{currency_UPS2}").first().price_usd
#     result_eur = cur_price2.price_usd * amount
#
#
#     return f"{result_eur}"



# @app.post("/currency/trade/<currency_UPS1>/<currency_UPS2>")#Відображати вартість по відношенню до іншой валюти(Трейд)
# def trade_currency_too_currency(currency_UPS1, currency_UPS2):
#     user_id = 1
#     amount_1 = request.get_json()["amount"]
#     user_balance = get_data(f"""SELECT balance from Account WHERE user_id="{user_id}' and currency_id = '{currency_UPS1}'""")
#     act_currency1 = get_data(f"""SELECT * From Currency WHERE currency_name =  '{currency_UPS1}' and date_time = datetime.datetime.now().strftime("%d-%m-%y")""")
#     cur1_cost_price_usd = act_currency2[0]["price_usd"]
#
#     act_currency2 = get_data(f"""SELECT * From Currency WHERE currency_name =  '{currency_UPS2}' and date_time = datetime.datetime.now().strftime("%d-%m-%y")""")
#     cur2_cost_price_usd = act_currency1[0]["price_usd"]
#
#     need_cur2 = amount_1 * 1.0 * cur1_cost_price_usd / cur2_cost_price_usd
#
#     exists_amount_currency2 = act_currency2[0]['available_quantity']
#     if (user_balance[0]["balance"] >= amount_1) and (exists_amount_currency2 > need_cur2):
#         get_data(f"UPDATE Currency set available_quantity = '{exists_amount_currency2 - need_cur2}' where date_time = datetime.datetime.now().strftime("%d-%m-%y") and currency_name = '{currency_UPS1}'")
#         get_data(f"UPDATE Currency set available_quantity = '{act_currency1[0]["available_quantity"] + amount1}' where date_time = datetime.datetime.now().strftime("%d-%m-%y") and currency_name = '{currency_UPS}'")
#
#         get_data(f"UPDATE Account set balance = '{user_balance[0]["balance"]-amount1}' where user_id = {user_id} and currency_name = '{currency_UPS1}'")
#         get_data(f"UPDATE Account set balance = '{user_balance2[0]["balance"]+need_cur2}' where user_id = {user_id} and currency_name = '{currency_UPS2}'")
#
#         get_data(f"""INSERT into Transactions (user_id, type_of_transaction, currency_from_exchange, currency_for_exchange, date_time, currency_spent, currency_received)
#         VALUES('{user_id}',"exchange",'{currency_UPS1}','{currency_UPS2}',datetime.datetime.now().strftime("%d-%m-%y"),'{amount_1}','{need_currency2}')""")
#         return "ok"
#     else:
#         return "not ok"
# @app.get("/currency/course/<currency_UPS>/<currency_UPS2>")#Відображати вартість по відношенню до іншой валюти(курс)
# def course_currency_too_currency(currency_UPS, currency_UPS2):
#     result = get_data"""(f"SELECT round((select price_usd from Currency WHERE currency_name='{currency_UPS}')/
#     (select price_usd from Currency WHERE currency_name='{currency_UPS2}'), 2)")"""
#     return result
#
# @app.get("/currency/<currency_name>")#Відображати кількість доступної валюти
# def show_currency_available(currency_name):
#     result = get_data(f"SELECT available_quantity from CURRENCY")
#     return result
#
# @app.get("/currency/<currency_UPS>/raiting")#Рейтинг валюти
# def currency_rating():
#     request_data = request.get_json()
#     comment = request_data['comment']
#     raiting = request_data['raiting']
#     get_data(f"INSERT INTO Raiting (currency_name, raiting, comment) VALUES('{carrency_UPS}', '{raiting}', '{comment}'")
#     return "ok"
#
# @app.route("/currency/<currency_name>")#Історія курсу
# def currency_history(currency_name):
#
#     return f"Currency: {currency_name}"
#
# @app.post("/currency/<currency_name>")#Операція обміну
# def currency_exchange(currency_name):
#
#     return f"Currency: {currency_name}"
#
# @app.get("/user/balance/<user_id>")#Баланс користувача
# def user_balance(user_id):
#     result = get_data(f"select user_id, currency_id, balance from Account where user_id='{user_id}'")
#     return result
#
# @app.post("/user/transfer/<currency_name>")#Переказ
# def user_transfer(currency_name):
#
#     return f"Currency: {currency_name}"
#
# @app.get("/user/history/<currency_name>")#Історія користувача
# def user_history(currency_name):
#
#     return f"Currency: {currency_name}"
#
# @app.get("/user/deposit/<currency_name>")#Відображати депозити юзера
# def user_deposit_1(currency_name):
#
#     return f"Currency: {currency_name}"
#
# @app.post("/user/deposit/<currency_UPS>")#Створюваємо новий депозит
# def user_deposit(currency_UPS):
#     request_data = request.get_json()
#     user_id = request_data['user_id']
#     date_of_issue = request_data['date_of_issue']
#     date_of_ixpiry = request_data['date_of_ixpiry']
#     balance = request_data['balance']
#     interest_rate = request_data['interest_rate']
#     strorage_condition = request_data['strorage_condition']
#
#     get_data(f"""INSERT INTO Deposits (user_id, date_of_issue, date_of_ixpiry,
#     balance, currency_name, interest_rate, strorage_condition) VALUES(
#     '{user_id}', '{date_of_issue}', '{date_of_ixpiry}', '{balance}',
#     "{currency_UPS}', '{interest_rate}', '{strorage_condition}')""")
#
#     return "ok"
#
# @app.route("/user/deposit/<deposit_id>")#Депозити юзера
# def user_deposit_id(deposit_id):
#     result = get_data(f"SELECT * from DEPOSITS")
#     """пока отображается вся таблица, надо переделать под конкретного юзера"""
#     return result
#
#
# @app.route("/deposit/<currency_name>")#Депозитні ставки та терміни
# def deposit_reviews(currency_name):
#     result = get_data(f"SELECT interest_rate, storage_condition from DEPOSITS")
#     return result

if __name__ == '__main__':
    app.run(debug=True)
