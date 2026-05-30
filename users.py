from aiogram import Router, F
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from database import load_movies, save_movies

router = Router()

@router.message(
    F.text &
    ~F.text.startswith("edit") &
    (F.text != "royhat")
)
async def send_movie(message: Message):

    movies = load_movies()

    code = message.text

    if code not in movies:
        await message.answer("❌ Bunday kino topilmadi.")
        return

    movie = movies[code]

    movie["views"] = movie.get("views", 0) + 1

    save_movies(movies)

    text = (
        f"🎬 Nomi: {movie['name']}\n\n"
        f"🌐 Tili: {movie['language']}\n\n"
        f"🎭 Janri: {movie['genre']}\n\n"
        f"🆔 Kodi: {code}"
    )

    # INLINE BUTTON
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Asosiy kanal",
                    url="https://t.me/kino_izlaydi"
                )
            ]
        ]
    )

    try:

        if movie["type"] == "video":

            await message.answer_video(
                video=movie["video"],
                caption=text,
                reply_markup=keyboard
            )

        else:

            await message.answer_document(
                document=movie["video"],
                caption=text,
                reply_markup=keyboard
            )

    except:

        await message.answer(
            "❌ Kino yuborishda xatolik."
        )