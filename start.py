from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from database import (
    load_groups,
    load_users,
    save_users
)
from database import load_groups

from inline import subscribe_button
from config import CHANNEL_USERNAME

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    users = load_users()

    user_data = {
        "id": message.from_user.id,
        "name": message.from_user.full_name
    }

# USER BOR-YO'QLIGINI TEKSHIRISH
    exists = False

    for user in users:

        if user["id"] == message.from_user.id:
            exists = True
            break

        if not exists:

            users.append(user_data)

        save_users(
            message.from_user.id,
            message.from_user.full_name
        )

    groups = load_groups()

    buttons = [
        [
            InlineKeyboardButton(
                text="📢 Kanalga obuna bo'lish",
                url="https://t.me/kino_izlaydi"
            )
        ]
    ]

    # DYNAMIC GROUPS
    for group in groups:

        buttons.append(
            [
                InlineKeyboardButton(
                    text=group["name"],
                    url=group["url"]
                )
            ]
        )

    buttons.append(
        [
            InlineKeyboardButton(
                text="✅ Tekshirish",
                callback_data="check_sub"
            )
        ]
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )

    await message.answer(
        "📢 Botdan foydalanish uchun obuna bo'ling.",
        reply_markup=keyboard
    )

@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):

    member = await callback.bot.get_chat_member(
        chat_id=CHANNEL_USERNAME,
        user_id=callback.from_user.id
    )

    if member.status in ["member", "administrator", "creator"]:

        await callback.message.answer(
            "✅ Obuna tasdiqlandi.\n🎥Kino kodini kiriting"
        )

    else:

        await callback.message.answer(
            "❌ Avval obuna bo'ling."
        )

    await callback.answer()

