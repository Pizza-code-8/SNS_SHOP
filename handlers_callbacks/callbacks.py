import random
import string
import datetime

from aiogram import F, Router

from aiogram.types import CallbackQuery, Message, FSInputFile, InputMediaPhoto
from aiogram.filters import StateFilter, CommandObject

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state

from aiogram.enums.parse_mode import ParseMode

from bot import bot
from admin.admin_id import admin_id
from kb.ikb import sub_ikb, start_ikb, admin_ikb, add_category_ikb, add_stuff, market_category_ikb, market_stuff, make_order, orders_ikb, work_orders, order_btn, basket_btn, mg_ikb, mg_ikb_market, back_btn, orders_from_user_ikb, back_btn_menu, CategoryFactory, StuffFactory, CategoryFactory_client, StuffFactory_client, Orders, MgFactory, MgFactory_client, User_Orders, Order_finish, Order_finish_1
from kb.kb import main_menu_kb
from db.sns_users import take_ref_link, take_referals, take_stat_ref, take_discount, add_basket, take_basket, take_user_id, take_username, clean_basket, take_id_orders, add_orders_in_users, add_user, check_user, take_order_check, add_order_check, add_referals_username
from db.category import add_num_category, add_name_in_category, add_price_in_category, add_pic_in_category, take_all_category, delete_category, add_weight_category, add_portions_category, take_name_category_from_category, take_price_from_category_by_name, take_weight_from_category_by_name, take_portions_from_category_by_name
from db.stuff import add_name_in_stuff, add_category_name_in_stuff, add_num_in_stuff, take_stuff_id_from_stuff, delete_stuff, take_name_from_stuff, take_cat_name_from_stuff, add_in_stock_in_stuff, take_in_stock_from_stuff, take_all_stuff_id_from_stuff, take_cat_name_from_stuff_by_id, take_stuff_name_from_stuff, take_stuff_id_from_stuff_by_name, add_in_stock_in_stuff_by_id, add_mg_in_stuff_by_num, take_mg_by_name_by_mg, take_cat_name_from_stuff_by_mg, take_stuff_name_from_stuff_by_mg, take_stuff_id_from_stuff_by_name_mg
from db.orders import add_user_id_orders, add_adress_in_orders, add_basket_in_orders, add_order_id_in_orders, add_sum_in_orders, take_adress_from_orders, take_sum_from_orders, take_order_id_from_orders, take_user_id_from_orders, take_username_from_orders, take_basket_from_orders, clean_order, add_phone_in_orders, take_phone_from_orders, take_all_orders_by_user_id, take_stat_from_orders, add_stat_in_orders, take_time_of_order, take_username_from_orders_by_uid
from aiogram.utils.deep_linking import create_start_link, decode_payload

router = Router()

class Conditions(StatesGroup):
    add_num_category_state = State()
    add_name_category_state = State()
    add_price_category_state= State()
    add_pic_category_state = State()
    add_mg_state = State()
    add_weight_category_state = State()
    add_portions_category_state = State()
    delete_category = State()
    add_num_stuff_state = State()
    add_name_stuff_state = State()
    add_in_stock_stuff_state = State()
    delete_stuff = State()
    delete_all_stuff = State()
    add_address = State()
    add_phone_num = State()
    state_change = State()
    

cat_num: dict[int, dict[int]] = {}
stuff_name: dict[int, dict[str]] = {}
stuff_id: dict[int, dict[str]] = {}
order_price: dict[int, dict[int]] = {}
user_id_for_order: dict[int, dict[int]] = {}
cat_name: dict[int, dict[int]] = {}
mg_stuff: dict[int, dict[int]] = {}
address: dict[int, dict[str]] = {}

@router.callback_query(F.data == "sub")
async def i_sub(callback: CallbackQuery):
    user = await bot.get_chat_member(chat_id=-1002305724083, user_id=callback.from_user.id)
    if user.status == "left":
        await callback.message.edit_text(
            "Вы по прежнему не полписаны на канал☹️\n\nПодпишитесь по ссылке: https://t.me/snyspavlodar",
            reply_markup=sub_ikb()
        )
    else:
        link = await create_start_link(bot, str(callback.from_user.id), encode=True)
        if check_user(callback.from_user.id) == False:
            add_user(user_id=callback.from_user.id, username=callback.from_user.username, user_name=callback.from_user.full_name, ref_link=link)
        await callback.message.answer(
            f"Привет <b>{callback.from_user.full_name}</b>👋",
            reply_markup=main_menu_kb(),
            parse_mode=ParseMode.HTML
        )
        await callback.message.answer(
            f"Поиграем в хоккей?😉🏒\n\nИспользуй реферальную ссылку по команде /ref, и закидывай шайбы в свою корзину как <b>Иртыш!</b> Но даже у них нет таких <b>скидок как у нас</b>😎🤙\n\n<b>График работы: 11:00-23:30</b>\n\nПриятных покупок😁",
            reply_markup=start_ikb(),
            parse_mode=ParseMode.HTML
        )

@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery, state: FSMContext):
    user = await bot.get_chat_member(chat_id=-1002305724083, user_id=callback.from_user.id)
    if user.status == "left":
        await callback.message.answer(
            f"❗️Что бы использовать бота необходимо подписаться на наш канал: https://t.me/snyspavlodar",
            reply_markup=sub_ikb()
        )
    else:
        if take_stat_ref(callback.from_user.id) != "None":
            await callback.message.edit_text(
                f"Добро пожаловать в ваш профиль!\n\n👤<b>{callback.from_user.full_name}</b>\n├Ваш юзернейм: <code>@{callback.from_user.username}</code>\n├Ваш id: <code>{callback.from_user.id}</code>\n├Количество реффералов: <b>{take_referals(callback.from_user.id)}</b>\n├Ваша скидка: <b>{int(take_discount(callback.from_user.id) * 100)}%</b>\n├Вы реферал пользователя: <code>@{take_username(take_stat_ref(callback.from_user.id))}</code>\n└Ваша реферальная ссылка: <code>{take_ref_link(callback.from_user.id)}</code>",
                parse_mode = ParseMode.HTML,
                reply_markup=basket_btn()
            )
        else:
            await callback.message.edit_text(
                f"Добро пожаловать в ваш профиль!\n\n👤<b>{callback.from_user.full_name}</b>\n├Ваш юзернейм: <code>@{callback.from_user.username}</code>\n├Ваш id: <code>{callback.from_user.id}</code>\n├Количество реффералов: <b>{take_referals(callback.from_user.id)}</b>\n├Ваша скидка: <b>{int(take_discount(callback.from_user.id) * 100)}%</b>\n├Вы реферал пользователя: <code>{take_stat_ref(callback.from_user.id)}</code>\n└Ваша реферальная ссылка: <code>{take_ref_link(callback.from_user.id)}</code>",
                parse_mode = ParseMode.HTML,
                reply_markup=basket_btn()
            )

@router.callback_query(F.data == "back_menu")
async def back_menu(callback: CallbackQuery):
    await callback.message.answer(
        f"Поиграем в хоккей?😉🏒\n\nИспользуй реферальную ссылку по команде /ref, и закидывай шайбы в свою корзину как Иртыш! Но даже у них нет таких <b>скидок как у нас</b>😎🤙\n\nПриятных покупок😁",
        reply_markup = start_ikb(),
        parse_mode = ParseMode.HTML
    )

@router.callback_query(F.data == "ref_list")
async def ref_list(callback: CallbackQuery, state: FSMContext):
    user = await bot.get_chat_member(chat_id=-1002305724083, user_id=callback.from_user.id)
    if user.status == "left":
        await callback.message.answer(
            f"❗️Что бы использовать бота необходимо подписаться на наш канал: https://t.me/snyspavlodar",
            reply_markup=sub_ikb()
        )
    else:
        await callback.message.edit_text(
            f"💸Условия нашей реферальной системы\n\n💵<b>5%</b> - за 5 приглашенных и сделавших заказ друзей друзей\n💰<b>10%</b> - за 50 приглашенных друзей\n💎<b>20%</b> - за 250 приглашенных друзей\n\n🔥<b>Скидка действует пожизненно на все заказы</b>🔥\n\n🗣Скорей начинай делиться своей рефералкой: <code>{take_ref_link(callback.from_user.id)}</code>",
            parse_mode=ParseMode.HTML,
            reply_markup = back_btn_menu()
        )

#______________________________________________________________________________________________#

@router.callback_query(F.data == "shop")
async def shop(callback: CallbackQuery):
    await callback.message.answer(
        "Добро пожаловать в магазин🎉",
        reply_markup=market_category_ikb()
    )

@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.answer(
        "Добро пожаловать в магазин🎉",
        reply_markup=market_category_ikb()
    )

@router.callback_query(CategoryFactory_client.filter())
async def categories(callback: CallbackQuery, callback_data: CategoryFactory, state: FSMContext):
    num = callback_data.num
    await state.update_data(c_name = str(take_name_category_from_category(num)))
    stuff_name[callback.from_user.id] = await state.get_data()
    name = stuff_name[callback.from_user.id]["c_name"]
    await callback.message.edit_text(
        "Выберите крепость",
        reply_markup=mg_ikb_market(name)
    )

@router.callback_query(MgFactory_client.filter())
async def choose_category(callback: CallbackQuery, callback_data: MgFactory_client, state: FSMContext):
    c_name = stuff_name[callback.from_user.id]["c_name"]
    mg = int(callback_data.mg)
    name = take_cat_name_from_stuff_by_mg(c_name, mg)
    await state.update_data(mg = callback_data.mg)
    mg_stuff[callback.from_user.id] = await state.get_data()
    try:
        id = take_stuff_id_from_stuff_by_name_mg(name, mg)
        for_send = FSInputFile(f"/home/sns/SNS_SHOP/category_photo/{id}.jpg")
        await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=for_send,
            caption=f"<b>Выберите товар</b>\n\n🏒Название: <b>{name}</b>\n\n😋Вкус: <b>{take_stuff_name_from_stuff_by_mg(name, mg)}</b>\n\n💪Крепость: <b>{take_mg_by_name_by_mg(name, mg)}мг</b>\n\n💸Цена: <b>{take_price_from_category_by_name(name)}тг</b>\n\n⚖️Вес: <b>{take_weight_from_category_by_name(name)}мг</b>\n\n🍬Кол-во пакетиков: <b>{take_portions_from_category_by_name(name)} штук</b>\n\n💼В наличии: <b>{take_in_stock_from_stuff(id)}шт</b>\n\nID товара: <code>{id}</code>",
            parse_mode=ParseMode.HTML,
            reply_markup=market_stuff(name, mg)
        )
    except Exception as ex:
        print(ex)
        await callback.message.answer(
            "Товар закончился😢",
            reply_markup=market_stuff(name, mg)
        )

@router.callback_query(StuffFactory_client.filter())
async def categories(callback: CallbackQuery, callback_data: StuffFactory_client, state: FSMContext):
    num = callback_data.num
    mg = mg_stuff[callback.from_user.id]["mg"]
    name = str(take_cat_name_from_stuff(num))
    id = take_stuff_id_from_stuff(num)
    await state.update_data(s_id = str(id))
    stuff_id[callback.from_user.id] = await state.get_data()
    for_send = FSInputFile(f"/home/sns/SNS_SHOP/category_photo/{id}.jpg", filename=f"{id}.jpg")
    await callback.message.edit_media(
        InputMediaPhoto(
            media=for_send,
            caption=f"Выбран товар: <b>{name}</b> <b>{take_stuff_name_from_stuff(id)}</b>\n\n🏒Название: <b>{name}</b>\n\n😋Вкус: <b>{take_stuff_name_from_stuff(id)}</b>\n\n💪Крепость: <b>{take_mg_by_name_by_mg(name, mg)}мг</b>\n\n💸Цена: <b>{take_price_from_category_by_name(name)}тг</b>\n\n⚖️Вес: <b>{take_weight_from_category_by_name(name)}мг</b>\n\n🍬Кол-во пакетиков: <b>{take_portions_from_category_by_name(name)} штук</b>\n\n💼В наличии: <b>{take_in_stock_from_stuff(id)}шт</b>\n\nID товара: <code>{id}</code>",
            parse_mode=ParseMode.HTML,
        ),
        reply_markup=market_stuff(name, mg)
    )

@router.callback_query(F.data == "add_in_basket")
async def add_in_basket(callback: CallbackQuery):
    id = stuff_id[callback.from_user.id]["s_id"]
    print(id)
    basket_list = []
    uid = callback.from_user.id
    stock = take_in_stock_from_stuff(id)
    if stock > 0:
        new_stock = int(stock) - 1
        add_in_stock_in_stuff_by_id(id, new_stock)
        if take_basket(uid) == None:
            basket_list.append(id)
            add_basket(uid, basket_list)
        else:
            for item in take_basket(uid):
                basket_list.append(item)
            basket_list.append(id)
            add_basket(uid, basket_list)
        await callback.message.answer(
            f"Товар <b>{take_cat_name_from_stuff_by_id(id)}</b> <b>{take_stuff_name_from_stuff(id)}</b> добавлен в корзину✅",
            parse_mode = ParseMode.HTML
        )
    else:
        await callback.message.answer(
            "Товар закончился",
            parse_mode = ParseMode.HTML,
            reply_markup=back_btn()
        )

@router.callback_query(F.data == "show_basket")
async def show_basket(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    if take_basket(uid) != None:
        price = 0
        for item in take_basket(uid):
            print
            name = take_cat_name_from_stuff_by_id(item)
            price += take_price_from_category_by_name(name)
        if take_discount(uid) != 0:
            new_price = price - (price * take_discount(uid))
        else:
            new_price = price
        await state.update_data(price = new_price)
        order_price[callback.from_user.id] = await state.get_data()
        start_string = "🛒<b>Ваша корзина:</b>\n\n"
        midle_string = ""
        item_list = []
        for item in take_basket(uid):
            if item not in item_list:
                item_list.append(item)
        for item in item_list:
            n = take_basket(uid).count(item)
            name = take_cat_name_from_stuff_by_id(item)
            price += take_price_from_category_by_name(name)
            end_string = f"\n🚀Скидка: <b>{int(take_discount(uid) * 100)}%</b>\n\n💸Общая стоимость чека (c учетом скидки): <b>{new_price}тг</b>"
            new_string = midle_string + f"<b>{name} {take_stuff_name_from_stuff(item)}</b> - <b>{n} штук</b>: <b>{take_price_from_category_by_name(name) * n}тг</b>\n---------------------------\n"
            midle_string = new_string
        fin_string = start_string + new_string + end_string
        await callback.message.answer(
            f"{fin_string}",
            parse_mode=ParseMode.HTML,
            reply_markup=make_order()
        )
    else:
        await callback.message.answer(
            "Ваша корзина пуста☹️",
            reply_markup=make_order()
        )

@router.callback_query(F.data == "clean_basket")
async def clean_basket_user(callback: CallbackQuery):
    uid = callback.from_user.id
    add_basket(uid, None)
    await callback.message.answer(
        "Коризина отчищена❌"
    )

@router.callback_query(F.data == "make_order")
async def do_order(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    close= datetime.time(23,30,00)
    open = datetime.time(11,00,00)
    offset = datetime.timedelta(hours=4)
    tz = datetime.timezone(offset, name='КЗ')
    t_now = datetime.datetime.now(tz=tz).time()
    if open < t_now < close:
        if take_basket(uid) != None:
            await callback.message.answer(
                "Введите адрес для доставки"
            )
            await state.set_state(Conditions.add_address)
        else:
            await callback.message.answer(
                "Добавьте товар, что бы сделать заказ"
            )
    else:
        await callback.message.answer(
            f"Доставка работает с <b>11:00-23:30</b>",
            parse_mode=ParseMode.HTML
        )

@router.message(StateFilter(Conditions.add_address))
async def phone_num(message: Message, state: FSMContext):
    uid = message.from_user.id
    await state.update_data(address = message.text)
    address[message.from_user.id] = await state.get_data()
    await message.answer(
        "Введите свой номер телефона для связи"
    )
    await state.set_state(Conditions.add_phone_num)

@router.message(StateFilter(Conditions.add_phone_num))
async def address_order(message: Message, state: FSMContext):
    #try:
    orders_list = []
    uid = message.from_user.id
    if take_stat_ref(uid) != "None":
        if take_order_check(uid) == "None":
            add_order_check(uid, "+")
            add_referals_username(take_username(take_stat_ref(uid)))
    username = message.from_user.username
    phone_num = message.text
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    basket = take_basket(uid)
    print(basket)
    price = order_price[message.from_user.id]["price"]
    n = address[message.from_user.id]["address"]
    id = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    add_user_id_orders(user_id=uid, username=username, order_id=id, time = now)
    add_adress_in_orders(id, n)
    add_phone_in_orders(id, phone_num)
    add_sum_in_orders(id, price)
    add_basket_in_orders(id, basket)
    if take_id_orders(uid) == None:
        orders_list.append(id)
        add_orders_in_users(uid, orders_list)
    else:
        for pos_id in take_id_orders(uid):
            orders_list.append(pos_id)
        orders_list.append(id)
        add_orders_in_users(uid, orders_list)
    start_string = f"<b>Новый заказ от пользователя</b>🥳\n\nID пользователя: <code>{take_user_id(uid)}</code>\n\nЮзернейм пользователя: <code>@{take_username(uid)}</code>\n\nАдрес доставки: <code>{take_adress_from_orders(id)}</code>\n\nНомер телефона: <code>{take_phone_from_orders(id)}</code>\n\nВремя оформления <code>{take_time_of_order(id)}</code>\n\n"
    midle_string = ""
    fin_user = f"<b>Ваш заказ поступил в обработку🥳\n\nID вашего заказа:</b> <code>{id}</code>\n\nВремя оформления: <code>{take_time_of_order(id)}</code>\n\nАдрес доставки: <b>{take_adress_from_orders(id)}</b>\n\nСтатус заказа: <b>В обработке</b>\n\n<b>Оплата заказа будет при получении наличными/картой</b>🤝\n\nВремя ожидания заказа: <b>1-2 часа</b>\n\n"
    item_list = []
    for item in basket:
        if item not in item_list:
            item_list.append(item)
    for item in item_list:
        n = basket.count(item)
        name = take_cat_name_from_stuff_by_id(item)
        price += take_price_from_category_by_name(name)
        end_string = f"\n🚀Скидка: <b>{int(take_discount(uid) * 100)}%</b>\n\n💸Общая стоимость чека (c учетом скидки): <b>{take_sum_from_orders(id)}тг</b>"
        new_string = midle_string + f"<b>{name} {take_stuff_name_from_stuff(item)}</b> - <b>{n} штук</b>: <b>{take_price_from_category_by_name(name) * n}тг</b>\n---------------------------\n"
        midle_string = new_string
    fin_string = start_string + new_string + end_string
    fin_user_string = fin_user + new_string + end_string
    clean_basket(uid)
    await message.answer(
        f"{fin_user_string}", 
        parse_mode=ParseMode.HTML
    )
    await bot.send_message(
        chat_id=admin_id,
        text = f"{fin_string}",
        parse_mode = ParseMode.HTML,
        reply_markup=order_btn()
    )
    #except:
    #    await message.answer(
    #        "Вы уже сделали заказ. Повторный заказ можно оформить, только после завершения"
    #    )

@router.callback_query(F.data == "show_orders")
async def show_orders(callback: CallbackQuery):
    uid = callback.from_user.id
    orders = take_id_orders(uid)
    try:
        for id in orders:
            print(id)
            item_list = []
            fin_user = f"ID вашего заказа: <code>{id}</code>\n\nВремя оформления вашего заказа: <code>{take_time_of_order(id)}</code>\n\nАдрес доставки: <b>{take_adress_from_orders(id)}</b>\n\nСтатус заказа: <b>{take_stat_from_orders(id)}</b>\n\n<b>Оплата заказа будет при получении наличными/картой</b>🤝\n\nВремя ожидания заказа: <b>1-2 часа</b>\n\n"
            end_string = f"\n🚀Скидка: <b>{int(take_discount(uid) * 100)}%</b>\n\n💸Общая стоимость чека (c учетом скидки): <b>{take_sum_from_orders(id)}тг</b>"
            midle_string = ""
            basket = take_basket_from_orders(id)
            for item in basket:
                if item not in item_list:
                    item_list.append(item)
            for item in item_list:
                n = basket.count(item)
                name = take_cat_name_from_stuff_by_id(item)
                end_string = f"\n🚀Скидка: <b>{int(take_discount(uid) * 100)}%</b>\n\n💸Общая стоимость чека (c учетом скидки): <b>{take_sum_from_orders(id)}тг</b>"
                new_string = midle_string + f"<b>{name} {take_stuff_name_from_stuff(item)}</b> - <b>{n} штук</b>: <b>{take_price_from_category_by_name(name) * n}тг</b>\n---------------------------\n"
                midle_string = new_string
            fin_user_string = fin_user + new_string + end_string
            await callback.message.answer(
                f"{fin_user_string}",
                parse_mode=ParseMode.HTML,
                reply_markup=back_btn_menu()
            )
    except:
        await callback.message.answer(
            "У вас пока что нет заказов"
        )
        
        
#______________________________________________________________________________________________#

@router.callback_query(F.data == "admin_desk")
async def admin_desk(callback: CallbackQuery):
    user_id = callback.from_user.id
    await callback.message.answer(
        "Выбери действие, которое хочешь сделать👀",
        reply_markup=admin_ikb()
    )

@router.callback_query(F.data == "update_market")
async def update_stuff(callback: CallbackQuery):
    await callback.message.answer(
        "Добавь категорию (бренд)",
        reply_markup=add_category_ikb()
    )

@router.callback_query(F.data == "add_category")
async def add_num_cat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Добавтье номер категории (бренда)"
    )
    await state.set_state(Conditions.add_num_category_state)

@router.message(Conditions.add_num_category_state, lambda x: x.text.isdigit())
async def add_category(message: Message, state: FSMContext):
    num = message.text
    print(num)
    try:
        add_num_category(num_category=num)
        await message.answer(
            "Добавтье имя категории (бренда)"
        )
        await state.update_data(number = num)
        cat_num[message.from_user.id] = await state.get_data()
        await state.set_state(Conditions.add_name_category_state)
    except:
        await message.answer(
            f"Категория с номером {num} уже существует!\n\nДобавь категорию с другим номером"
        )
        await state.set_state(Conditions.add_num_category_state)

@router.message(StateFilter(Conditions.add_name_category_state), F.text)
async def add_name_cat(message: Message, state: FSMContext):
    num = int(cat_num[message.from_user.id]["number"])
    await state.update_data(name = message.text)
    cat_name[message.from_user.id] = await state.get_data()
    add_name_in_category(id=num, name=message.text)
    await message.answer(
        "Добавтье цену категории (бренда)"
    )
    await state.set_state(Conditions.add_price_category_state)

@router.message(StateFilter(Conditions.add_price_category_state), lambda x: x.text.isdigit())
async def add_cat_price(message: Message, state: FSMContext):
    num = int(cat_num[message.from_user.id]["number"])
    add_price_in_category(num, int(message.text))
    await message.answer(
        "Добавтье вес банки категории (бренда)"
    )
    await state.set_state(Conditions.add_weight_category_state)

@router.message(StateFilter(Conditions.add_weight_category_state), lambda x: x.text.isdigit())
async def add_weight(message: Message, state: FSMContext):
    num = int(cat_num[message.from_user.id]["number"])
    weight = int(message.text)
    add_weight_category(num, weight)
    await message.answer(
        "Добавьте количество порций в банке категории (бренда)"
    )
    await state.set_state(Conditions.add_portions_category_state)

@router.message(StateFilter(Conditions.add_weight_category_state), lambda x: x.text.isdigit())
async def add_weight(message: Message, state: FSMContext):
    num = int(cat_num[message.from_user.id]["number"])
    weight = int(message.text)
    add_weight_category(num, weight)
    await message.answer(
        "Добавьте количество порций в банке категории (бренда)"
    )
    await state.set_state(Conditions.add_portions_category_state)

@router.message(StateFilter(Conditions.add_portions_category_state), lambda x: x.text.isdigit())
async def add_pic_cat(message: Message, state: FSMContext):
    num = int(cat_num[message.from_user.id]["number"])
    portions = int(message.text)
    add_portions_category(num, portions)
    await message.answer(
        "Категория успешно добавлена✅"
    )
    await state.set_state(default_state)

@router.callback_query(F.data == "delete_category")
async def delete_category_btn(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Введите номер категории, которую хотите удалить"
    )
    await state.set_state(Conditions.delete_category)

@router.message(StateFilter(Conditions.delete_category), lambda x: x.text.isdigit())
async def delete_category_num(message: Message, state: FSMContext):
    num = int(message.text)
    delete_category(num)
    await message.answer(
        "Категория удалена❌"
    )
    await message.answer(
        "Добавь категорию (бренд)",
        reply_markup=add_category_ikb()
    )
    await state.set_state(default_state)

@router.callback_query(F.data == "clean_category")
async def delete_all_category(callback: CallbackQuery):
    all = take_all_category()
    for stuff in all:
        delete_category(stuff)
    await callback.message.answer(
        "Добавь категорию (бренд)",
        reply_markup=add_category_ikb()
    )
    await callback.message.answer(
        "Все категории удалены❌"
    )

@router.callback_query(CategoryFactory.filter())
async def categories(callback: CallbackQuery, callback_data: CategoryFactory, state: FSMContext):
    num = callback_data.num
    await state.update_data(c_name = str(take_name_category_from_category(num)))
    stuff_name[callback.from_user.id] = await state.get_data()
    name = stuff_name[callback.from_user.id]["c_name"]
    await callback.message.edit_text(
        "Выберите крепость",
        reply_markup=mg_ikb(name)
    )

@router.callback_query(F.data=="add_stuff")
async def add_stuff_btn(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Введите номер позиции"
    )
    await state.set_state(Conditions.add_num_stuff_state)

@router.message(StateFilter(Conditions.add_num_stuff_state), lambda x: x.text.isdigit())
async def add_id_for_stuff(message: Message, state: FSMContext):
    num = message.text
    id = "".join(random.choices(string.ascii_letters + string.digits, k=15))
    await state.update_data(s_num = num)
    cat_num[message.from_user.id] = await state.get_data()
    await state.update_data(stuff_id = id)
    stuff_id[message.from_user.id] = await state.get_data()
    try:
        add_num_in_stuff(num_stuff=num, stuff_id=id)
        await message.answer(
            "Добавьте вкус позиции"
        )
        await state.set_state(Conditions.add_name_stuff_state)
        await state.update_data(s_num = num)
        cat_num[message.from_user.id] = await state.get_data()
        print(type(num))
    except Exception as ex:
        print(ex)
        await message.answer(
            "Позиция с данным номер уже сушествует, введите другой номер"
        )
        await state.set_state(Conditions.add_num_stuff_state)

@router.message(StateFilter(Conditions.add_name_stuff_state), F.text)
async def add_id_for_stuff(message: Message, state: FSMContext):
    taste = message.text
    num = cat_num[message.from_user.id]["s_num"]
    name = stuff_name[message.from_user.id]["c_name"]
    add_category_name_in_stuff(num, name)
    add_name_in_stuff(num, taste)
    await message.answer(
        "Введите количество единиц в наличии"
    ) 
    await state.set_state(Conditions.add_in_stock_stuff_state)

@router.message(StateFilter(Conditions.add_in_stock_stuff_state), lambda x: x.text.isdigit())
async def add_in_stock_for_stuff(message: Message, state: FSMContext):
    stock = message.text
    num = cat_num[message.from_user.id]["s_num"]
    name = take_cat_name_from_stuff(num)
    print(num)
    add_in_stock_in_stuff(num, stock)
    await message.answer(
        "Введите крепость позиции"
    )
    await state.set_state(Conditions.add_mg_state)

@router.message(StateFilter(Conditions.add_mg_state), lambda x: x.text.isdigit())
async def add_portions(message: Message, state: FSMContext):
    mg = int(message.text)
    num = cat_num[message.from_user.id]["s_num"]
    add_mg_in_stuff_by_num(num, mg)
    await message.answer(
        "Добавьте картинку позиции"
    )
    await state.set_state(Conditions.add_pic_category_state)

@router.message(StateFilter(Conditions.add_pic_category_state), F.photo)
async def add_mg_for_stuff(message: Message, state: FSMContext):
    id = stuff_id[message.from_user.id]["stuff_id"]
    photo = message.photo[-1]
    await message.bot.download(file=photo, destination=f"/home/sns/SNS_SHOP/category_photo/{id}.jpg")
    await message.answer(
        "Позиция успешно добавлена✅"
    )
    await state.set_state(default_state)

@router.callback_query(F.data == "delete_stuff")
async def delete_one_stuff(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Введите ID товара, который хотите удалить"
    )
    await state.set_state(Conditions.delete_stuff)

@router.message(StateFilter(Conditions.delete_stuff), lambda x: len(x.text) == 15)
async def take_brand_for_delete(message: Message, state: FSMContext):
    id = message.text
    delete_stuff(id)
    await message.answer(
        "Товар удален❌"
    )

@router.callback_query(F.data == "clean_stuff")
async def clean_all_stuff(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Введите имя категории, из которой хотите удлаить товары"
    )
    await state.set_state(Conditions.delete_all_stuff)

@router.message(StateFilter(Conditions.delete_all_stuff), F.text)
async def clean_all_stuff(message: Message, state: FSMContext):
    name = message.text
    for id in take_all_stuff_id_from_stuff(name):
        delete_stuff(id)
    await message.answer(
        "Все товары удалены из категории❌"
    )

@router.callback_query(StuffFactory.filter())
async def categories(callback: CallbackQuery, callback_data: StuffFactory, state: FSMContext):
    num = callback_data.num
    mg = mg_stuff[callback.from_user.id]["mg"]
    name = str(take_cat_name_from_stuff(num))
    id = take_stuff_id_from_stuff(num)
    for_send = FSInputFile(f"/home/sns/SNS_SHOP/category_photo/{id}.jpg", filename=f"{id}.jpg")
    if callback.from_user.id == admin_id:
        await callback.message.edit_media(
            InputMediaPhoto(
                media=for_send,
                caption=f"🏒Название: <b>{name}</b>\n\n😋Вкус: <b>{take_stuff_name_from_stuff(id)}</b>\n\n💪Крепость: <b>{take_mg_by_name_by_mg(name, mg)}мг</b>\n\n💸Цена: <b>{take_price_from_category_by_name(name)}тг</b>\n\n⚖️Вес: <b>{take_weight_from_category_by_name(name)}мг</b>\n\n🍬Кол-во пакетиков: <b>{take_portions_from_category_by_name(name)} штук</b>\n\n💼В наличии: <b>{take_in_stock_from_stuff(id)}шт</b>\n\nID товара: <code>{id}</code>",
                parse_mode=ParseMode.HTML,
            ),
            reply_markup=add_stuff(name, mg)
        )
    await state.update_data(c_name = str(take_cat_name_from_stuff(num)))
    stuff_name[callback.from_user.id] = await state.get_data()

@router.callback_query(F.data == "orders")
async def orders_from_buyers(callback: CallbackQuery):
    await callback.message.answer(
        "ВСЕ ЗАКАЗЫ ОТ ПОЛЬЗОВАТЕЛЕЙ💰",
        reply_markup=orders_ikb()
    )

@router.callback_query(Orders.filter())
async def show_order(callback: CallbackQuery, callback_data: Orders, state: FSMContext):
    user_id = callback_data.user_id
    await state.update_data(id = user_id)
    user_id_for_order[callback.from_user.id] = await state.get_data()
    await callback.message.answer(
        f"Все заказ от пользователя c ID <b>{user_id}</b>",
        reply_markup=orders_from_user_ikb(callback_data.user_id),
        parse_mode=ParseMode.HTML
    )

@router.callback_query(User_Orders.filter())
async def show_user_orders(callback: CallbackQuery, callback_data: User_Orders):
    order_id = callback_data.id
    item_list = []
    user_id = user_id_for_order[callback.from_user.id]["id"]
    username = take_username_from_orders(order_id)
    basket_list = take_basket_from_orders(order_id)
    discount = take_discount(user_id)
    price = take_sum_from_orders(order_id)
    address = take_adress_from_orders(order_id)
    start_string = f"ID заказа: <code>{order_id}</code>\n\nЮзернейм пользователя: <code>@{username}</code>\n\nНомер телефона: <code>{take_phone_from_orders(order_id)}</code>\n\nСтатус заказа: <b>{take_stat_from_orders(order_id)}</b>\n\nВремя оформления: <code>{take_time_of_order(order_id)}</code>\n\n"
    end_string = f"Скидка пользователя: <b>{(discount * 100)}%</b>\n\nСумма заказа (с учетом скидки): <b>{price} тг</b>\n\nАдрес доставки: <code>{address}</code>"
    for item in basket_list:
        if item not in item_list:
            item_list.append(item)
    for item in item_list:
        print(item)
        name = take_cat_name_from_stuff_by_id(item)
        unit = take_basket_from_orders(order_id).count(item)
        new_string = f"<b>{name} {take_stuff_name_from_stuff(item)}</b> - <b>{unit} штук</b>: <b>{take_price_from_category_by_name(name) * unit} тг</b>\n---------------------------\n"

    string_for_send = start_string + new_string + end_string

    await callback.message.answer(
        f"{string_for_send}",
        parse_mode=ParseMode.HTML,
        reply_markup=work_orders(order_id)
    )


@router.callback_query(Order_finish_1.filter())
async def finish_ord(callback: CallbackQuery, callback_data: Order_finish_1):
    order_id = callback_data.id
    user_id = user_id_for_order[callback.from_user.id]["id"]
    add_stat_in_orders(order_id, "Курьер в пути")
    await bot.send_message(
        chat_id=user_id,
        text=f"<b>Ваш заказ доставляется🥳</b>\n\nВремя доставки: <b>1-2 часа</b>\n\n🗣<b>А пока поделитесь ссылкой с друзьями:</b> <code>{take_ref_link(user_id)}</code>",
        parse_mode=ParseMode.HTML
    )
    await callback.message.edit_text(
        f"Вы сменили статус заказа\n\nID заказа: <code>{order_id}</code>\n\nЗаказчик: <code>{take_username_from_orders_by_uid(user_id)}</code>\n\nВремя заказа: <code>{take_time_of_order(order_id)}</code>",
        parse_mode = ParseMode.HTML,
        reply_markup = order_btn()
    )

@router.callback_query(Order_finish.filter())
async def finish_ord(callback: CallbackQuery, callback_data: Order_finish):
    order_id = callback_data.id
    user_id = user_id_for_order[callback.from_user.id]["id"]
    clean_order(order_id)
    list_id = take_id_orders(user_id)
    list_id.remove(str(order_id))
    if len(list_id) != 0:
        add_orders_in_users(user_id, list_id)
    else:
        add_orders_in_users(user_id, None)
    await callback.message.answer(
        "Заказ обработан✅",
        reply_markup=order_btn()
    )
    await bot.send_message(
        chat_id=user_id,
        text=f"<b>Спасибо за покупку!</b>\n\nБудем ждать вас снова😉\n\n🗣<b>Не забудьте поделиться ссылкой с друзьями:</b> <code>{take_ref_link(user_id)}</code>",
        parse_mode=ParseMode.HTML
    )

@router.callback_query(MgFactory.filter())
async def choose_category(callback: CallbackQuery, callback_data: MgFactory, state: FSMContext):
    c_name = stuff_name[callback.from_user.id]["c_name"]
    mg = int(callback_data.mg)
    name = take_cat_name_from_stuff_by_mg(c_name, mg)
    await state.update_data(mg = callback_data.mg)
    mg_stuff[callback.from_user.id] = await state.get_data()
    await state.update_data(c_name = name)
    cat_name[callback.from_user.id] = await state.get_data()
    try:
        id = take_stuff_id_from_stuff_by_name_mg(name, mg)
        for_send = FSInputFile(f"/home/sns/SNS_SHOP/category_photo/{id}.jpg")
        await bot.send_photo(
            chat_id=callback.from_user.id,
            photo=for_send,
            caption=f"🏒Название: <b>{name}</b>\n\n😋Вкус: <b>{take_stuff_name_from_stuff_by_mg(name, mg)}</b>\n\n💪Крепость: <b>{take_mg_by_name_by_mg(name, mg)}мг</b>\n\n💸Цена: <b>{take_price_from_category_by_name(name)}тг</b>\n\n⚖️Вес: <b>{take_weight_from_category_by_name(name)}мг</b>\n\n🍬Кол-во пакетиков: <b>{take_portions_from_category_by_name(name)} штук</b>\n\n💼В наличии: <b>{take_in_stock_from_stuff(id)}шт</b>\n\nID товара: <code>{id}</code>",
            parse_mode=ParseMode.HTML,
            reply_markup=add_stuff(name, mg)
        )
    except Exception as ex:
        print(ex)
        await callback.message.answer(
            "Товар закончился😢",
            reply_markup=add_stuff(name, mg)
        )
#______________________________________________________________________________________________#