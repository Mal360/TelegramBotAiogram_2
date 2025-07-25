import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import router as handlers_router

bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(handlers_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
