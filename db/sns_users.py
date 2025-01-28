import sqlite3
import re

conn = sqlite3.connect("db/sns_users.db", check_same_thread=False)
cur = conn.cursor()

#Проверка юзера на наличие в бд
def check_user(user_id):
    cur.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    user = cur.fetchone()
    if user:
        return True
    else:
        return False
    
#_________________________________________________________________________________#
    
#Добавление юзера в бд
def add_user(user_id: int, username: str, user_name: str, ref_link: str):
    cur.execute(f"INSERT INTO users (user_id, username, user_name, referal_link) VALUES (?, ?, ?, ?)", (user_id, username, user_name, ref_link))
    conn.commit()

#Добавление stat_ref
def add_stat_ref(user_id, stat):
    cur.execute(f"UPDATE users SET stat_ref = {stat} WHERE user_id = {user_id}")
    conn.commit()

#Добавление кол-ва рефералов
def add_referals(user_id):
    cur.execute(f"UPDATE users SET referals = referals + {1} WHERE user_id = {user_id}")
    conn.commit()

def add_referals_username(user_id):
    cur.execute(f"UPDATE users SET referals = referals + {1} WHERE username = '{user_id}'")
    conn.commit()

#Добавление скидки
def add_discount(user_id, discount):
    cur.execute(f"UPDATE users SET discount = {discount} WHERE user_id = {user_id}")
    conn.commit()

#Добавление корзины
def add_basket(user_id, item):
    cur.execute(f"UPDATE users SET basket = ? WHERE user_id = ?", (f"{item}", user_id))
    conn.commit()

#Добавить id заказов
def add_orders_in_users(user_id, orders):
    cur.execute(f"UPDATE users SET orders = ? WHERE user_id = ?", (f"{orders}", user_id))
    conn.commit()

#Добавить кол-во заказов
def add_order_check(user_id, stat):
    cur.execute(f"UPDATE users SET order_check = ? WHERE user_id = ?", (f"{stat}", user_id))
    conn.commit()

#_________________________________________________________________________________#

#Вытащить user_id
def take_user_id(user_id):
    cur.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
    user_id = cur.fetchone()[0]
    return user_id

#Вытащить username
def take_username(user_id):
    cur.execute(f"SELECT username FROM users WHERE user_id = {user_id}")
    username = cur.fetchone()[0]
    return username

#Вытащить user_name
def take_user_name(user_id):
    cur.execute(f"SELECT user_name FROM users WHERE user_id = {user_id}")
    user_name = cur.fetchone()[0]
    return user_name

#Вытащить рефку
def take_ref_link(user_id):
    cur.execute(f"SELECT referal_link FROM users WHERE user_id = {user_id}")
    ref_link = cur.fetchone()[0]
    return ref_link

#Вытащить stat_ref
def take_stat_ref(user_id):
    cur.execute(f"SELECT stat_ref FROM users WHERE user_id = {user_id}")
    stat = cur.fetchone()[0]
    return stat

#Вытащить кол-во рефералов
def take_referals(user_id):
    cur.execute(f"SELECT referals FROM users WHERE user_id = {user_id}")
    referals = cur.fetchone()[0]
    return referals

#Вытащить скидку
def take_discount(user_id):
    cur.execute(f"SELECT discount FROM users WHERE user_id = {user_id}")
    discount = cur.fetchone()[0]
    return discount

#Вытащить корзину
def take_basket(user_id):
    cur.execute(f"SELECT basket FROM users WHERE user_id = {user_id}")
    basket = cur.fetchone()[0]
    fin_list = []
    basket_list = re.split(r"['\s]", basket[1:-1])
    if basket == "None":
        return None
    else:
        for item in basket_list:
            punctuation = r"[,\s]"
            if item not in punctuation:
                fin_list.append(item)
        return fin_list
    
#Вытащить сумму корзины
def take_sum(user_id):
    cur.execute(f"SELECT sum FROM users WHERE user_id = {user_id}")
    sum = cur.fetchone()[0]
    return sum

#Вытащить адрес
def take_address(user_id):
    cur.execute(f"SELECT address FROM users WHERE user_id = {user_id}")
    address = cur.fetchone()[0]
    return address

#Вытащить id заказов
def take_id_orders(user_id):
    cur.execute(f"SELECT orders FROM users WHERE user_id = {user_id}")
    orders = cur.fetchone()[0]
    fin_list = []
    orders_list = re.split(r"['\s]", orders[1:-1])
    if orders == "None":
        return None
    else:
        for item in orders_list:
            punctuation = r"[,\s]"
            if item not in punctuation:
                fin_list.append(item)
        return fin_list
    
#Вытащить инфу о заказах
def take_order_check(user_id):
    cur.execute(f"SELECT order_check FROm users WHERE user_id = {user_id}")
    check = cur.fetchone()[0]
    return check

#_________________________________________________________________________________#

#Удалить корзину
def clean_basket(user_id):
    cur.execute(f"UPDATE users SET basket = '{None}' WHERE user_id = {user_id}")
    conn.commit()

#Удалить сумму
def clean_sum(user_id):
    cur.execute(f"UPDATE users SET sum = {0} WHERE user_id = {user_id}")
    conn.commit()