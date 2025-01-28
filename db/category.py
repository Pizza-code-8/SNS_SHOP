import sqlite3

conn = sqlite3.connect("db/category.db", check_same_thread=False)
cur = conn.cursor()

#Добавить num_category
def add_num_category(num_category: int):
    cur.execute("INSERT INTO category (num_category) VALUES (?)", (num_category))
    conn.commit()

#Добавить имя категории
def add_name_in_category(id, name):
    cur.execute(f"UPDATE category SET name = ? WHERE num_category = ?", (f"{name}", id))
    conn.commit()

#Добавить цену категории
def add_price_in_category(id, price):
    cur.execute(f"UPDATE category SET price = {price} WHERE num_category = {id}")
    conn.commit()

#Добавить картинку категории
def add_pic_in_category(id, pic):
    cur.execute(f"UPDATE category SET pic = {pic} WHERE num_category = {id}")
    conn.commit()


#Добавть вес категории
def add_weight_category(id, mg):
    cur.execute(f"UPDATE category SET weight = {mg} WHERE num_category = {id}")
    conn.commit()


#Добавть порции категории
def add_portions_category(id, mg):
    cur.execute(f"UPDATE category SET portions = {mg} WHERE num_category = {id}")
    conn.commit()

#_________________________________________________________________________________#

#Вытащить номер категории
def take_num_category_from_category(id):
    cur.execute(f"SELECT num_category FROM category WHERE num_category = {id}")
    num_category = cur.fetchone()[0]
    return num_category

#Вытащить имя категории
def take_name_category_from_category(id):
    cur.execute(f"SELECT name FROM category WHERE num_category = {id}")
    name_category = cur.fetchone()[0]
    return name_category

def take_name_category_from_category_by_name(name):
    cur.execute(f"SELECT name FROM category WHERE name = {name}")
    name_category = cur.fetchone()[0]
    return name_category

#Вытащить цену категории
def take_price_from_category(id):
    cur.execute(f"SELECT price FROM category WHERE num_category = {id}")
    price = cur.fetchone()[0]
    return price

def take_price_from_category_by_name(name):
    cur.execute(f"SELECT price FROM category WHERE name = '{name}'")
    price = cur.fetchone()[0]
    return price

#Вытащить картинку категории
def take_pic_from_category(id):
    cur.execute(f"SELECT pic FROM category WHERE num_category = {id}")
    pic = cur.fetchone()[0]
    return pic

def take_pic_from_category_by_name(name):
    cur.execute(f"SELECT pic FROM category WHERE name = '{name}'")
    pic = cur.fetchone()[0]
    return pic

#Вытащить вес категории
def take_weight_from_category(id):
    cur.execute(f"SELECT weight FROM category WHERE num_category = {id}")
    weight = cur.fetchone()[0]
    return weight

def take_weight_from_category_by_name(name):
    cur.execute(f"SELECT weight FROM category WHERE name = '{name}'")
    weight = cur.fetchone()[0]
    return weight

#Вытащить порции категории
def take_portions_from_category(id):
    cur.execute(f"SELECT portions FROM category WHERE num_category = {id}")
    portions = cur.fetchone()[0]
    return portions

def take_portions_from_category_by_name(name):
    cur.execute(f"SELECT portions FROM category WHERE name = '{name}'")
    portions = cur.fetchone()[0]
    return portions


#_________________________________________________________________________________#

#Удалить категорию
def delete_category(num):
    cur.execute(f"DELETE FROM category WHERE num_category = {num}")
    conn.commit()

#_________________________________________________________________________________#

#Все категории
def take_all_category():
    cur.execute(f"SELECT num_category FROM category")
    category_list = cur.fetchall()
    fin_list = []
    for i in category_list:
        fin_list.append(i[0])
    return fin_list