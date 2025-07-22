import os
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import setup_application
from aiohttp import web

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("👋 Вітаємо! Це бот для обліку пайовиків.")

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

app = web.Application()
app.on_startup.append(on_startup)
setup_application(app, dp, bot=bot)
web.run_app(app, port=8000)
