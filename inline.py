from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


subscribe_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Kanalga obuna bo'lish",
                url="https://t.me/kino_izlaydi"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Guruhga qo'shilish",
                url="https://t.me/+iMbK1gP6FvI4N2My"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Tekshirish",
                callback_data="check_sub"
            )
        ]
    ]
)