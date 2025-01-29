from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class CategoryFactory(CallbackData, prefix="category"):
    num: str

class StuffFactory(CallbackData, prefix="stuff"):
    num: str

class CategoryFactory_client(CallbackData, prefix="category_client"):
    num: str

class StuffFactory_client(CallbackData, prefix="stuff_client"):
    num: str

class Orders(CallbackData, prefix="orders"):
    user_id: str

class MgFactory(CallbackData, prefix="mg"):
    mg: str

class MgFactory_client(CallbackData, prefix="mg_client"):
    mg: str

class User_Orders(CallbackData, prefix="orders_from_user"):
    id: str

class Order_finish(CallbackData, prefix="finish"):
    id: str

class Order_finish_1(CallbackData, prefix="finish_1"):
    id: str

class Axcept_Order(CallbackData, prefix="axcept"):
    id: str

from db.category import take_all_category, take_name_category_from_category, take_price_from_category
from db.stuff import take_all_stuff, take_name_from_stuff, take_all_stuff_id_from_stuff, take_num_from_stuff_by_stuff_id, take_stuff_name_from_stuff, take_mg_from_stuff_by_id, take_all_stuff_id_from_stuff_by_mg
from db.orders import take_all_orders, take_username_from_orders_by_uid, take_all_orders_by_user_id, take_username_from_orders

#Я подписался - ikb

def sub_ikb():

    ikb = [
        [
            InlineKeyboardButton(text="✅Я подписался", callback_data="sub")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Стартовая ikb

#def start_ikb():
#
#    ikb = [
#        [
#            InlineKeyboardButton(text="👤Профиль", callback_data="profile")
#        ],
#        [
#            InlineKeyboardButton(text="🤝Поддержка", url="https://t.me/xxwwalter")
#        ],
#        [
#            InlineKeyboardButton(text="🚀Условия реферальной системы", callback_data="ref_list")
#        ],
#        [
#        InlineKeyboardButton(text="🛍Магазин", callback_data="shop"),
#        InlineKeyboardButton(text="🛒Корзина", callback_data = "show_basket"),
#        InlineKeyboardButton(text="🗂Мои заказы", callback_data = "show_orders")
#        ]
#    ]

def start_ikb():

    ikb = [
        [
            InlineKeyboardButton(text="🛍Магазин", callback_data="shop")
        ],
        [
            InlineKeyboardButton(text="🛒Корзина", callback_data = "show_basket")
        ],
        [
            InlineKeyboardButton(text="🚀Условия реферальной системы", callback_data="ref_list")
        ],
        [
        InlineKeyboardButton(text="👤Профиль", callback_data="profile"),
        InlineKeyboardButton(text="🤝Поддержка", url="https://t.me/xxwwalter"),
        InlineKeyboardButton(text="🗂Мои заказы", callback_data = "show_orders")
        ]
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

#Стартовая ikb для админа

def start_ikb_admin():

    ikb = [
        [
            InlineKeyboardButton(text="👑АДМИН-ПАНЕЛЬ👑", callback_data="admin_desk")
        ],
        [
            InlineKeyboardButton(text="🛍Магазин", callback_data="shop")
        ],
        [
            InlineKeyboardButton(text="🛒Корзина", callback_data = "show_basket")
        ],
        [
            InlineKeyboardButton(text="🚀Условия реферальной системы", callback_data="ref_list")
        ],
        [
        InlineKeyboardButton(text="👤Профиль", callback_data="profile"),
        InlineKeyboardButton(text="🤝Поддержка", url="https://t.me/xxwwalter"),
        InlineKeyboardButton(text="🗂Мои заказы", callback_data = "show_orders")
        ]
    ]

    keybaord = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keybaord

def market_category_ikb():

    builder = InlineKeyboardBuilder()
    total_category = take_all_category()
    for i in total_category:
        try:
            builder.add(InlineKeyboardButton(text=f"{str(i)}•{take_name_category_from_category(i)}•{take_price_from_category(i)}тг", callback_data=CategoryFactory_client(num = str(i)).pack()))
        except:
            continue
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Назад🔙", callback_data = "back_menu"))

    return builder.as_markup()

def market_stuff(name, mg):

    builder = InlineKeyboardBuilder()
    total_stuff = take_all_stuff_id_from_stuff_by_mg(name, mg)
    for i in total_stuff:
        try:
            builder.add(InlineKeyboardButton(text=f"№{str(take_num_from_stuff_by_stuff_id(i))}•{take_stuff_name_from_stuff(i)}", callback_data=StuffFactory_client(num = str(take_num_from_stuff_by_stuff_id(i))).pack()))
        except:
            continue
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Добавить в корзину⬇️", callback_data = "add_in_basket"))
    builder.row(InlineKeyboardButton(text="Посмотреть корзину🛒", callback_data = "show_basket"))
    builder.row(InlineKeyboardButton(text="Назад🔙", callback_data = "back"))

    return builder.as_markup()

def basket_btn():

    ikb = [
        [
            InlineKeyboardButton(text="Посмотреть корзину🛒", callback_data = "show_basket")
        ],
        [
            InlineKeyboardButton(text="Назад🔙", callback_data = "back_menu")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def back_btn():

    ikb = [
        [
            InlineKeyboardButton(text="Назад🔙", callback_data = "back")
        ]
    ]

    keyboard = (InlineKeyboardMarkup(inline_keyboard=ikb))

    return keyboard

def back_btn_menu():

    ikb = [
        [
            InlineKeyboardButton(text="Назад🔙", callback_data = "back_menu")
        ]
    ]

    keyboard = (InlineKeyboardMarkup(inline_keyboard=ikb))

    return keyboard

def make_order():
    
    ikb = [
        [
            InlineKeyboardButton(text="Оформить заказ🚗", callback_data="make_order")
        ],
        [
            InlineKeyboardButton(text="Отчистить корзину🗑", callback_data="clean_basket")
        ],
        [
            InlineKeyboardButton(text="Назад🔙", callback_data="back")
        ]
    ]

    keyboard = (InlineKeyboardMarkup(inline_keyboard=ikb))

    return keyboard

def make_order_menu():
    
    ikb = [
        [
            InlineKeyboardButton(text="Оформить заказ🚗", callback_data="make_order")
        ],
        [
            InlineKeyboardButton(text="Отчистить корзину🗑", callback_data="clean_basket")
        ],
        [
            InlineKeyboardButton(text="Назад🔙", callback_data="back_menu")
        ]
    ]

    keyboard = (InlineKeyboardMarkup(inline_keyboard=ikb))

    return keyboard

#Клавиаутра крепости

def mg_ikb_market(name):

    builder = InlineKeyboardBuilder()
    total_stuff = take_all_stuff_id_from_stuff(name)
    fin_list = []
    for i in total_stuff:
        if take_mg_from_stuff_by_id(i) not in fin_list:
            fin_list.append(take_mg_from_stuff_by_id(i))
    for mg in fin_list:
        try:
            builder.add(InlineKeyboardButton(text=f"{str(mg)}мг", callback_data=MgFactory_client(mg = str(mg)).pack()))
        except:
            continue
    builder.adjust(1)

    return builder.as_markup()

#______________________________________________________________________________________________#

#Клаиватура для админа

def admin_ikb():

    ikb = [
        [
            InlineKeyboardButton(text="Обновить ассортимент🛍", callback_data="update_market")
        ],
        [
            InlineKeyboardButton(text="Обработать заказы💸", callback_data="orders")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def order_btn():

    ikb = [
        [
            InlineKeyboardButton(text="Обработать заказы💸", callback_data="orders")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard


#Клаиватура обновления категорий

def add_category_ikb():

    builder = InlineKeyboardBuilder()
    total_category = take_all_category()
    for i in take_all_category():
        try:
            builder.add(InlineKeyboardButton(text=f"{str(i)}•{take_name_category_from_category(i)}•{take_price_from_category(i)}тг", callback_data=CategoryFactory(num = str(i)).pack()))
        except:
            continue
    builder.adjust(1)
    builder.row(InlineKeyboardButton(text="Добавить категорию✅", callback_data = "add_category"))
    builder.row(InlineKeyboardButton(text="Удалить категорию🎯", callback_data="delete_category"))
    builder.row(InlineKeyboardButton(text="Удалить все категории❌", callback_data="clean_category"))

    return builder.as_markup()

def add_category_btn():

    ikb = [
        [
            InlineKeyboardButton(text="Добавить категорию✅", callback_data = "add_category")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

#Клаиватура обновления товара

def add_stuff(name, mg):

    builder = InlineKeyboardBuilder()
    total_stuff = take_all_stuff_id_from_stuff_by_mg(name, mg)
    try:
        for i in total_stuff:
            try:
                builder.add(InlineKeyboardButton(text=f"№{str(take_num_from_stuff_by_stuff_id(i))}•{take_stuff_name_from_stuff(i)}", callback_data=StuffFactory(num = str(take_num_from_stuff_by_stuff_id(i))).pack()))
            except:
                continue
        builder.adjust(1)
        builder.row(InlineKeyboardButton(text="Добавить товар✅", callback_data = "add_stuff"))
        builder.row(InlineKeyboardButton(text="Удалить товар🎯", callback_data="delete_stuff"))
        builder.row(InlineKeyboardButton(text="Удалить все товары❌", callback_data="clean_stuff"))
    except:
        builder.row(InlineKeyboardButton(text="Добавить товар✅", callback_data = "add_stuff"))
        builder.row(InlineKeyboardButton(text="Удалить товар🎯", callback_data="delete_stuff"))
        builder.row(InlineKeyboardButton(text="Удалить все товары❌", callback_data="clean_stuff"))

    return builder.as_markup()

#Клавиаутра крепости

def mg_ikb(name):

    builder = InlineKeyboardBuilder()
    total_stuff = take_all_stuff_id_from_stuff(name)
    fin_list = []
    for i in total_stuff:
        if take_mg_from_stuff_by_id(i) not in fin_list:
            fin_list.append(take_mg_from_stuff_by_id(i))
    try:
        for mg in fin_list:
            try:
                builder.add(InlineKeyboardButton(text=f"{str(mg)}мг", callback_data=MgFactory(mg = str(mg)).pack()))
            except:
                continue
        builder.adjust(1)
        builder.row(InlineKeyboardButton(text="Добавить товар✅", callback_data = "add_stuff"))
    except:
        builder.row(InlineKeyboardButton(text="Добавить товар✅", callback_data = "add_stuff"))

    return builder.as_markup()


#Посмотреть заказы

def orders_ikb():

    builder = InlineKeyboardBuilder()
    total_orders = take_all_orders()
    fin_list = []
    for user_id in total_orders:
        if user_id not in fin_list:
            fin_list.append(user_id)
    for user_id in fin_list:
        try:
            builder.add(InlineKeyboardButton(text=f"@{take_username_from_orders_by_uid(user_id)}", callback_data=Orders(user_id = str(user_id)).pack()))
        except:
            continue
    builder.adjust(1)

    return builder.as_markup()

#Обработать заказы

def work_orders(order_id):

    ikb = [
        [
            InlineKeyboardButton(text="Принять заказ✅", callback_data=Axcept_Order(id = order_id).pack())
        ], 
        [
            InlineKeyboardButton(text="Начал досталвять✅", callback_data=Order_finish_1(id = order_id).pack())
        ],
        [
            InlineKeyboardButton(text="Заказ завершен✅", callback_data=Order_finish(id = order_id).pack())
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=ikb)

    return keyboard

def orders_from_user_ikb(user_id):

    builder = InlineKeyboardBuilder()
    total_user_orders = take_all_orders_by_user_id(user_id)
    n = 0
    for id in total_user_orders:
        n += 1
        builder.add(InlineKeyboardButton(text=f"@{take_username_from_orders(id)}•{n}", callback_data = User_Orders(id = str(id)).pack()))
    builder.adjust(1)

    return builder.as_markup()

#______________________________________________________________________________________________#