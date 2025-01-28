import sqlite3
import re

conn = sqlite3.connect("db/orders.db", check_same_thread=False)
cur = conn.cursor()

#Чек наличия юзера в бд
def check_user_in_orders(user_id):
    cur.execute(f"SELECT * FROM orders WHERE user_id = {user_id}")
    user = cur.fetchall()
    if user:
        return True
    else:
        return False

#_________________________________________________________________________________#

#Добавить user_id + username покупателя
def add_user_id_orders(user_id: int, username: str, order_id: str, time: str):
    cur.execute(f"INSERT INTO orders (user_id, username, order_id, time) VALUES (?, ?, ?, ?)", (user_id, username, order_id, time))
    conn.commit()

#Добавить корзину пользователя
def add_basket_in_orders(order_id, basket):
    cur.execute(f"UPDATE orders SET basket = ? WHERE order_id = ?", (f"{basket}", order_id))
    conn.commit()

#Добавить сумму заказа
def add_sum_in_orders(order_id, sum):
    cur.execute(f"UPDATE orders SET sum = sum + {sum} WHERE order_id = '{order_id}'")
    conn.commit()

#Добавление адреса пользователя
def add_adress_in_orders(order_id, adress):
    cur.execute(f"UPDATE orders SET adress = '{adress}' WHERE order_id = '{order_id}'")
    conn.commit()

#Добавление order_id
def add_order_id_in_orders(user_id, order_id):
    cur.execute(f"UPDATE orders SET order_id = '{order_id}' WHERE user_id = {user_id}")
    conn.commit()

#Добавление номер телефона
def add_phone_in_orders(order_id, phone):
    cur.execute(f"UPDATE orders SET phone_num = '{phone}' WHERE order_id = '{order_id}'")
    conn.commit()

#Добавление статуса заказа
def add_stat_in_orders(order_id, stat):
    cur.execute(f"UPDATE orders SET stat = '{stat}' WHERE order_id = '{order_id}'")
    conn.commit()

#_________________________________________________________________________________#

#Вытащить user_id покупателя
def take_user_id_from_orders(user_id):
    cur.execute(f"SELECT user_id FROM orders WHERE user_id = {user_id}")
    user_id = cur.fetchone()[0]
    return user_id

#Вытащить username покупателя
def take_username_from_orders(order_id):
    cur.execute(f"SELECT username FROM orders WHERE order_id = '{order_id}'")
    username = cur.fetchone()[0]
    return username

#Вытащить статус заказа
def take_stat_from_orders(order_id):
    cur.execute(f"SELECT stat FROM orders WHERE order_id = '{order_id}'")
    stat = cur.fetchone()[0]
    return stat

def take_username_from_orders_by_uid(user_id):
    cur.execute(f"SELECT username FROM orders WHERE user_id = {user_id}")
    username = cur.fetchone()[0]
    return username

#Вытащить корзину покупателя
def take_basket_from_orders(order_id):
    cur.execute(f"SELECT basket FROM orders WHERE order_id = '{order_id}'")
    basket = cur.fetchone()[0]
    fin_list = []
    basket_list = re.split(r"['\s]", basket[1:-1])
    if basket_list == "None":
        return None
    else:
        for item in basket_list:
            punctuation = r"[,\s]"
            if item not in punctuation:
                fin_list.append(item)
        return fin_list
    
#Вытащить сумму заказ покупателя
def take_sum_from_orders(order_id):
    cur.execute(f"SELECT sum FROM orders WHERE order_id = '{order_id}'")
    sum = cur.fetchone()[0]
    return sum

#Вытщаить адрес покупателя
def take_adress_from_orders(order_id):
    cur.execute(f"SELECT adress FROM orders WHERE order_id = '{order_id}'")
    adress = cur.fetchone()[0]
    return adress

#Вытащить order_id покупателя
def take_order_id_from_orders(user_id):
    cur.execute(f"SELECT order_id FROM orders WHERE user_id = {user_id}")
    order_id = cur.fetchone()[0]
    return order_id

#Вытащить номер телефона
def take_phone_from_orders(order_id):
    cur.execute(f"SELECT phone_num FROM orders WHERE order_id = '{order_id}'")
    phone_num = cur.fetchone()[0]
    return phone_num

#Вытащить время заказа
def take_time_of_order(order_id):
    cur.execute(f"SELECT time FROM orders WHERE order_id = '{order_id}'")
    time = cur.fetchone()[0]
    return time

#_________________________________________________________________________________#

#Удалить завершенный заказ
def clean_order(order_id):
    cur.execute(f"DELETE FROM orders WHERE order_id = '{order_id}'")
    conn.commit()

#Достать все заказы
def take_all_orders():
    cur.execute(f"SELECT user_id FROM orders")
    orders_list = cur.fetchall()
    fin_list = []
    for i in orders_list:
        fin_list.append(i[0])
    return fin_list

#Достать все заказы
def take_all_orders_by_user_id(user_id):
    cur.execute(f"SELECT order_id FROM orders WHERE user_id = {user_id}")
    orders_list = cur.fetchall()
    fin_list = []
    for i in orders_list:
        fin_list.append(i[0])
    return fin_list
