import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import router as keyboards_router

bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(keyboards_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
