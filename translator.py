from googletrans import Translator

async def tarjima(user_text: str, lang: str) -> str:
    translator = Translator()
    try:
        natija = await translator.translate(user_text, dest=lang)
        return natija.text
    except Exception as e:
        print("Tarjima xatosi:", e)
        return "Tarjima qilib bo‘lmadi ❌"
