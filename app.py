import asyncio from aiogram import Bot, Dispatcher from aiogram.filters import CommandStart from aiogram.types import Message async def main(): print(«Бот запущен») if name == «main»: asyncio.run(main())
dp = Dispatcher

@ dp.message(CommandStart), async def start_message с параметром message, и await message.answer с текстом: «Привет! Я бот для записи на вождение».
