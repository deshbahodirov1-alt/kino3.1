import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import TOKEN

from start import router as start_router
from admin import router as admin_router
from users import router as users_router


bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(admin_router)
dp.include_router(users_router)


async def main(): 

    print("Bot ishga tushdi ✅")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())