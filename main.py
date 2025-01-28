import asyncio
import logging

from aiogram import Dispatcher, Router, F

from bot import bot
from handlers_callbacks import handlers, callbacks

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
router = Router()

async def main():

    dp.include_routers(handlers.router, callbacks.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())