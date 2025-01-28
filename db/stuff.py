import sqlite3

conn = sqlite3.connect("db/stuff.db", check_same_thread=False)
cur = conn.cursor()

#Добавить num
def add_num_in_stuff(num_stuff: int, stuff_id: str):
    cur.execute("INSERT INTO stuff (num, stuff_id) VALUES (?, ?)", (num_stuff, stuff_id))
    conn.commit()

#Добавить имя товара
def add_category_name_in_stuff(num, category):
    cur.execute(f"UPDATE stuff SET category_name = ? WHERE num = ?", (f"{category}", num))
    conn.commit()

#Добавить имя товара
def add_name_in_stuff(num, name):
    cur.execute(f"UPDATE stuff SET stuff_name = ? WHERE num = ?", (f"{name}", num))
    conn.commit()

#Добавить цену товара
def add_price_in_stuff(num, price):
    cur.execute(f"UPDATE stuff SET price = ? WHERE num = ?", (f"{price}", num))
    conn.commit()

#Добавить id товара
def add_stuff_id_in_stuff(num, stuff_id):
    cur.execute(f"UPDATE stuff SET stuff_id = ? WHERE num = ?", (f"{stuff_id}", num))
    conn.commit()

#Добавить наличие товара
def add_in_stock_in_stuff(num, in_stock):
    cur.execute(f"UPDATE stuff SET in_stock = ? WHERE num = ?", (f"{in_stock}", num))
    conn.commit()

def add_in_stock_in_stuff_by_id(id, in_stock):
    cur.execute(f"UPDATE stuff SET in_stock = ? WHERE stuff_id = ?", (f"{in_stock}", id))
    conn.commit()

#Добавить крепость товара

def add_mg_in_stuff_by_num(num, mg):
    cur.execute(f"UPDATE stuff SET mg = ? WHERE num = ?", (f"{mg}", num))
    conn.commit()

#_________________________________________________________________________________#

#Вытащить номер товара
def take_num_from_stuff(num):
    cur.execute(f"SELECT num FROM stuff WHERE num = {num}")
    num = cur.fetchone()[0]
    return num

def take_num_from_stuff_by_stuff_id(id):
    cur.execute(f"SELECT num FROM stuff WHERE stuff_id = '{id}'")
    num = cur.fetchone()[0]
    return num

#Вытащить имя товара
def take_name_from_stuff(num):
    cur.execute(f"SELECT stuff_name FROM stuff WHERE num = {num}")
    name = cur.fetchone()[0]
    return name

def take_stuff_name_from_stuff(id):
    cur.execute(f"SELECT stuff_name FROM stuff WHERE stuff_id = '{id}'")
    stuff_name = cur.fetchone()[0]
    return stuff_name

def take_stuff_name_from_stuff_by_mg(name, mg):
    cur.execute(f"SELECT stuff_name FROM stuff WHERE category_name = '{name}' AND mg = '{mg}'")
    stuff_name = cur.fetchone()[0]
    return stuff_name

#Вытщаить цену товара
def take_price_from_stuff(num):
    cur.execute(f"SELECT price FROM stuff WHERE num = {num}")
    price = cur.fetchone()[0]
    return price

def take_price_from_stuff_by_stuff_id(id):
    cur.execute(f"SELECT price FROM stuff WHERE stuff_id = '{id}'")
    price = cur.fetchone()[0]
    return price

#Вытщаить id товара
def take_stuff_id_from_stuff(num):
    cur.execute(f"SELECT stuff_id FROM stuff WHERE num = {num}")
    stuff_id = cur.fetchone()[0]
    return stuff_id

def take_stuff_id_from_stuff_by_name(name):
    cur.execute(f"SELECT stuff_id FROM stuff WHERE category_name = '{name}'")
    stuff_id = cur.fetchone()[0]
    return stuff_id

def take_stuff_id_from_stuff_by_name_mg(name, mg):
    cur.execute(f"SELECT stuff_id FROM stuff WHERE category_name = '{name}' AND mg = {mg}")
    stuff_id = cur.fetchone()[0]
    return stuff_id

def take_all_stuff_id_from_stuff(category_name):
    cur.execute(f"SELECT stuff_id FROM stuff WHERE category_name = '{category_name}'")
    fin_list = []
    stuff_id_list = cur.fetchall()
    for i in stuff_id_list:
        fin_list.append(i[0])
    return fin_list

def take_all_stuff_id_from_stuff_by_mg(category_name, mg):
    cur.execute(f"SELECT stuff_id FROM stuff WHERE category_name = '{category_name}' AND mg = '{mg}'")
    fin_list = []
    stuff_id_list = cur.fetchall()
    for i in stuff_id_list:
        fin_list.append(i[0])
    return fin_list
    
#Вытщить имя категории
def take_cat_name_from_stuff(num):
    cur.execute(f"SELECT category_name FROM stuff WHERE num = {num}")
    category_name = cur.fetchone()[0]
    return category_name

def take_cat_name_from_stuff_by_mg(name, mg):
    cur.execute(f"SELECT category_name FROM stuff WHERE category_name = '{name}' AND mg = {mg}")
    category_name = cur.fetchone()[0]
    return category_name

def take_cat_name_from_stuff_by_id(id):
    cur.execute(f"SELECT category_name FROM stuff WHERE stuff_id = '{id}'")
    category_name = cur.fetchone()[0]
    return category_name

#Вытщить наличие товара
def take_in_stock_from_stuff(id):
    cur.execute(f"SELECT in_stock FROM stuff WHERE stuff_id = '{id}'")
    in_stock = cur.fetchone()[0]
    return in_stock

#Вытащить крепость позиции
def take_mg_from_stuff_by_id(id):
    cur.execute(f"SELECT mg FROM stuff WHERE stuff_id = '{id}'")
    mg = cur.fetchone()[0]
    return mg

def take_mg_by_name_by_mg(name, mg):
    cur.execute(f"SELECT mg FROM stuff WHERE category_name = '{name}' AND mg = '{mg}'")
    mg = cur.fetchone()[0]
    return mg

#_________________________________________________________________________________#

#Удалить товар
def delete_stuff(stuff_id):
    cur.execute(f"DELETE FROM stuff WHERE stuff_id = '{stuff_id}'")
    conn.commit()

#_________________________________________________________________________________#

#Все товары
def take_all_stuff(name):
    cur.execute(f"SELECT COUNT(*) FROM stuff WHERE category_name = {name}")
    stuff = cur.fetchone()[0]
    return stuff