from db.category import take_price_from_category_by_name, take_all_category
from db.stuff import take_all_stuff_id_from_stuff, take_stuff_id_from_stuff_by_name, take_stuff_name_from_stuff_by_mg
from db.sns_users import take_basket, take_id_orders
from db.orders import take_all_orders, take_basket_from_orders, take_all_orders_by_user_id, take_all_orders_by_user_id, take_stat_from_orders, add_stat_in_orders, take_time_of_order
import datetime

uid = 1911402590

id = "aL1PaT9PFKp30ec"
mg = 150

n = 0

close= datetime.time(23,30,00)
open = datetime.time(11,00,00)

t_now = datetime.datetime.now().time()

if open < t_now < close:
    print(True)