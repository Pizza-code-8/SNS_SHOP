from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from bot_settings import config

bot=Bot(
    token = config.bot_token.get_secret_value(),
    default=DefaultBotProperties()
)