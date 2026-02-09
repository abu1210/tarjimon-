from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.session.aiohttp import AiohttpSession


import asyncio
import logging
from gtts import gTTS
import os

from inline import LANGUAGES, ALL_LANGS, get_admin_lang_buttons, get_lang_buttons
from translator import tarjima  


logging.basicConfig(level=logging.INFO)



TOKEN = "7931118218:AAFzu-5fAnXVQoQGwBGT7tgdsgZ8K_S9hJo"
ADMIN_ID = 2001870098

bot = Bot(token=TOKEN,)
dp = Dispatcher()

user_data = {}

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        f"Assalomu aleykum {message.from_user.full_name} 👋\n\n"
        "Tarjimon botga xush kelibsiz!\n"
        "Tarjima qilmoqchi bo‘lgan matningizni yuboring 📝"
    )

@dp.message(Command("admin"))
async def admin_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return
    await message.answer(
        "Qaysi tilni qo‘shmoqchisiz? 🌍",
        reply_markup=get_admin_lang_buttons(page=0)
    )



@dp.callback_query(F.data.startswith("admin_page_"))
async def admin_page_callback(callback: types.CallbackQuery):
    page = int(callback.data.split("_")[-1])
    await callback.message.edit_reply_markup(reply_markup=get_admin_lang_buttons(page=page))



@dp.callback_query(F.data.startswith("add_"))
async def add_language(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Ruxsat yo‘q", show_alert=True)
        return

    code = callback.data.replace("add_", "")
    LANGUAGES[code] = ALL_LANGS[code]

    await callback.message.edit_text(
        f"✅ {ALL_LANGS[code]} tili qo‘shildi"
    )

admin_pages = {}  

@dp.callback_query(F.data.startswith("add_"))
async def add_language(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Ruxsat yo‘q", show_alert=True)
        return
    code = callback.data.replace("add_", "")
    LANGUAGES[code] = ALL_LANGS[code]
    await callback.message.edit_text(f"✅ {ALL_LANGS[code]} tili qo‘shildi")



@dp.callback_query(F.data.startswith("page_"))
async def page_handler(callback: types.CallbackQuery):
    page = int(callback.data.split("_")[1])
    admin_pages[callback.from_user.id] = page
    await callback.message.edit_reply_markup(reply_markup=get_lang_buttons(page=page))


@dp.message(F.text)
async def text_handler(message: types.Message):
    user_data[message.from_user.id] = message.text
    await message.answer(
        "Tarjima qilmoqchi bo‘lgan tilni tanlang 🌍",
        reply_markup=get_lang_buttons()
    )

@dp.callback_query(F.data.in_(LANGUAGES.keys()))
async def translate_handler(callback: types.CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id
    lang = callback.data
    user_text = user_data.get(user_id)

    if not user_text:
        await callback.message.answer("❗ Avval matn yuboring!")
        return

    tarjima_matn = await tarjima(user_text, lang)

    await callback.message.answer(f"📤 Tarjima:\n{tarjima_matn}")

    try:
        file_name = f"voice_{user_id}.mp3"
        tts = gTTS(text=tarjima_matn, lang=lang)
        tts.save(file_name)

        voice = FSInputFile(file_name)
        await callback.message.answer_voice(
            voice=voice,
            caption=tarjima_matn
        )
        os.remove(file_name)
    except:
        await callback.message.answer(f"📤 Tarjima:\n{tarjima_matn}")
        await callback.message.answer("Uzur ovoz qilib bo'lmadi")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
