from aiogram import F, Router

from aiogram.filters import Command, StateFilter, CommandObject
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.deep_linking import create_start_link, decode_payload

from bot import bot
from kb.kb import main_menu_kb
from kb.ikb import sub_ikb, start_ikb, start_ikb_admin, basket_btn, back_btn_menu, market_category_ikb, make_order
from db.sns_users import check_user, add_user, take_username, add_stat_ref, add_referals, add_discount, take_referals, take_discount, take_stat_ref, take_ref_link, take_basket, take_id_orders
from db.stuff import take_cat_name_from_stuff_by_id, take_stuff_name_from_stuff
from db.category import take_price_from_category_by_name
from db.orders import take_time_of_order, take_basket_from_orders, take_sum_from_orders, take_stat_from_orders, take_adress_from_orders
from admin.admin_id import admin_id

router = Router()

#Команда /start
@router.message(Command("start"))
async def start(message: Message, command: CommandObject):
    disc_1 = 0.05
    dics_2 = 0.1
    disc_3 = 0.2
    if check_user(message.from_user.id) == True:
        if take_referals(message.from_user.id) >= 250:
            add_discount(message.from_user.id, disc_3)
        elif take_referals(message.from_user.id) >= 50:
            add_discount(message.from_user.id, dics_2)
        elif take_referals(message.from_user.id) >= 5:
            add_discount(message.from_user.id, disc_1)
    link = await create_start_link(bot, str(message.from_user.id), encode=True)
    payload = command.args
    ref_id = decode_payload(payload) if payload else None
    if message.from_user.id == admin_id:
        if check_user(message.from_user.id) == False:
                add_user(user_id=message.from_user.id, username=message.from_user.username, user_name=message.from_user.full_name, ref_link=link)
        await message.answer(
            f"<b>{message.from_user.full_name}</b>, привет!",
            reply_markup=main_menu_kb(),
            parse_mode=ParseMode.HTML
        )
        await message.answer(
            f"💎Добро пожаловать в админ-панель💎\n\nЗдесь ты сможешь <b>обновить ассортимент</b> и <b>обработать заказы пользователей</b>😉",
            reply_markup = start_ikb_admin(),
            parse_mode = ParseMode.HTML
        )
    else:
        user = await bot.get_chat_member(chat_id=-1002305724083, user_id=message.from_user.id)
        if user.status == "left":
            if ref_id:
                await message.answer(
                    f"🥳Вы зашли по реферальной ссылке <code>@{take_username(str(ref_id))}</code>",
                    parse_mode=ParseMode.HTML
                    )
                add_user(user_id=message.from_user.id, username=message.from_user.username, user_name=message.from_user.full_name, ref_link=link)
                add_stat_ref(message.from_user.id, str(ref_id))
            await message.answer(
                f"❗️Что бы использовать бота необходимо подписаться на наш канал: https://t.me/snyspavlodar",
                reply_markup=sub_ikb()
            )
        else:
            if check_user(message.from_user.id) == False:
                if ref_id:
                    await message.answer(
                        f"🥳Вы зашли по реферальной ссылке <code>@{take_username(str(ref_id))}</code>",
                        parse_mode=ParseMode.HTML
                        )
                    add_user(user_id=message.from_user.id, username=message.from_user.username, user_name=message.from_user.full_name, ref_link=link)
                    add_stat_ref(message.from_user.id, str(ref_id))
                else:
                    add_user(user_id=message.from_user.id, username=message.from_user.username, user_name=message.from_user.full_name, ref_link=link)
            await message.answer(
                f"Привет <b>{message.from_user.full_name}</b>👋",
                reply_markup=main_menu_kb(),
                parse_mode=ParseMode.HTML
            )
            await message.answer(
                f"Поиграем в хоккей?😉🏒\n\nИспользуй реферальную ссылку по команде /ref, и закидывай шайбы в свою корзину как Иртыш! Но даже у них нет таких <b>скидок как у нас</b>\n\n<b>График работы: 11:00-23:00</b>😎🤙\n\nПриятных покупок😁",
                reply_markup = start_ikb(),
                parse_mode = ParseMode.HTML
            )

@router.message(Command("profile"))
async def cmd_profile(message: Message):
    disc_1 = 0.05
    dics_2 = 0.1
    disc_3 = 0.2
    if check_user(message.from_user.id) == True:
        if take_referals(message.from_user.id) >= 250:
            add_discount(message.from_user.id, disc_3)
        elif take_referals(message.from_user.id) >= 50:
            add_discount(message.from_user.id, dics_2)
        elif take_referals(message.from_user.id) >= 5:
            add_discount(message.from_user.id, disc_1)
    user = await bot.get_chat_member(chat_id=-1002305724083, user_id=message.from_user.id)
    if user.status == "left":
        await message.answer(
            f"❗️Что бы использовать бота необходимо подписаться на наш канал: https://t.me/snyspavlodar",
            reply_markup=sub_ikb()
        )
    else:
        if take_stat_ref(message.from_user.id) != "None":
            await message.answer(
                f"Добро пожаловать в ваш профиль!\n\n👤<b>{message.from_user.full_name}</b>\n├Ваш юзернейм: <code>@{message.from_user.username}</code>\n├Ваш id: <code>{message.from_user.id}</code>\n├Количество реффералов: <b>{take_referals(message.from_user.id)}</b>\n├Ваша скидка: <b>{int(take_discount(message.from_user.id) * 100)}%</b>\n├Вы реферал пользователя: <code>@{take_username(take_stat_ref(message.from_user.id))}</code>\n└Ваша реферальная ссылка: <code>{take_ref_link(message.from_user.id)}</code>",
                parse_mode = ParseMode.HTML,
                reply_markup=basket_btn()
            )
        else:
            await message.answer(
                f"Добро пожаловать в ваш профиль!\n\n👤<b>{message.from_user.full_name}</b>\n├Ваш юзернейм: <code>@{message.from_user.username}</code>\n├Ваш id: <code>{message.from_user.id}</code>\n├Количество реффералов: <b>{take_referals(message.from_user.id)}</b>\n├Ваша скидка: <b>{int(take_discount(message.from_user.id) * 100)}%</b>\n├Вы реферал пользователя: <code>{take_stat_ref(message.from_user.id)}</code>\n└Ваша реферальная ссылка: <code>{take_ref_link(message.from_user.id)}</code>",
                parse_mode = ParseMode.HTML,
                reply_markup=basket_btn()
            )

@router.message(Command("ref"))
async def cnd_ref(message: Message):
    user = await bot.get_chat_member(chat_id=-1002305724083, user_id=message.from_user.id)
    if user.status == "left":
        await message.answer(
            f"❗️Что бы использовать бота необходимо подписаться на наш канал: https://t.me/snyspavlodar",
            reply_markup=sub_ikb()
        )
    else:
        await message.answer(
            f"💸Условия нашей реферальной системы\n\n🫵<b>💵<b>5%</b> - за 5 приглашенных и сделавших заказ друзей\n💰<b>10%</b> - за 50 приглашенных друзей\n💎<b>20%</b> - за 250 приглашенных друзей\n\n🔥<b>Скидка действует пожизненно на все заказы</b>🔥\n\n🗣Скорей начинай делиться своей рефералкой: <code>{take_ref_link(message.from_user.id)}</code>",
            parse_mode=ParseMode.HTML,
            reply_markup = back_btn_menu()
        )

#Клаваитура

@router.message(F.text.lower() == "🏠")
async def show_menu(message: Message):
    disc_1 = 0.05
    dics_2 = 0.1
    disc_3 = 0.2
    if check_user(message.from_user.id) == True:
        if take_referals(message.from_user.id) >= 250:
            add_discount(message.from_user.id, disc_3)
        elif take_referals(message.from_user.id) >= 50:
            add_discount(message.from_user.id, dics_2)
        elif take_referals(message.from_user.id) >= 5:
            add_discount(message.from_user.id, disc_1)
    await message.answer(
        f"Поиграем в хоккей?😉🏒\n\nИспользуй реферальную ссылку по команде /ref, и закидывай шайбы в свою корзину как Иртыш! Но даже у них нет таких <b>скидок как у нас</b>😎🤙\n\nПриятных покупок😁",
        reply_markup = start_ikb(),
        parse_mode = ParseMode.HTML
        )
    
@router.message(F.text.lower() == "🛍")
async def show_shop(message: Message):
    disc_1 = 0.05
    dics_2 = 0.1
    disc_3 = 0.2
    if check_user(message.from_user.id) == True:
        if take_referals(message.from_user.id) >= 250:
            add_discount(message.from_user.id, disc_3)
        elif take_referals(message.from_user.id) >= 50:
            add_discount(message.from_user.id, dics_2)
        elif take_referals(message.from_user.id) >= 5:
            add_discount(message.from_user.id, disc_1)
    await message.answer(
        "Добро пожаловать в магазин🎉",
        reply_markup=market_category_ikb()
    )

@router.message(F.text.lower() == "🛒")
async def show_basket(message: Message):
    disc_1 = 0.05
    dics_2 = 0.1
    disc_3 = 0.2
    if check_user(message.from_user.id) == True:
        if take_referals(message.from_user.id) >= 250:
            add_discount(message.from_user.id, disc_3)
        elif take_referals(message.from_user.id) >= 50:
            add_discount(message.from_user.id, dics_2)
        elif take_referals(message.from_user.id) >= 5:
            add_discount(message.from_user.id, disc_1)
    uid = message.from_user.id
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
        await message.answer(
            f"{fin_string}",
            parse_mode=ParseMode.HTML,
            reply_markup=make_order()
        )
    else:
        await message.answer(
            "Ваша корзина пуста☹️",
            reply_markup=make_order()
        )

@router.message(F.text.lower() == "🗂")
async def cmd_orders(message: Message):
    uid = message.from_user.id
    orders = take_id_orders(uid)
    try:
        for id in orders:
            print(id)
            item_list = []
            fin_user = f"ID вашего заказа: <code>{id}</code>\n\nВремя оформления вашего заказа: <code>{take_time_of_order(id)}</code>\n\nАдрес для доставки: <b>{take_adress_from_orders(id)}</b>\n\nСтатус заказа: <b>{take_stat_from_orders(id)}</b>\n\n<b>Оплата заказа будет при получении наличными/картой</b>🤝\n\nВремя ожидания заказа: <b>1-2 часа</b>\n\n"
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
            await message.answer(
                f"{fin_user_string}",
                parse_mode=ParseMode.HTML,
                reply_markup=back_btn_menu()
            )
    except:
        await message.answer(
            "У вас пока что нет заказов"
        )