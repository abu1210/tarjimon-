from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from googletrans.client import LANGUAGES


LANGUAGES = {
    "en": "English 🇺🇸",
    "ru": "Russian 🇷🇺",
    "uz": "O'zbek 🇺🇿",
    "fr": "French 🇫🇷"
}


ALL_LANGS = {
    "abk": "Abkhaz 🇬🇪",
    "ace": "Acehnese 🇮🇩",
    "ach": "Acholi 🇺🇬",
    "aar": "Afar 🇪🇹",
    "af": "Afrikaans 🇿🇦",
    "sq": "Albanian 🇦🇱",
    "am": "Amharic 🇪🇹",
    "ar": "Arabic 🇸🇦",
    "hy": "Armenian 🇦🇲",
    "as": "Assamese 🇮🇳",
    "az": "Azerbaijani 🇦🇿",
    "bn": "Bengali 🇧🇩",
    "bs": "Bosnian 🇧🇦",
    "bg": "Bulgarian 🇧🇬",
    "yue": "Cantonese 🇭🇰",
    "ca": "Catalan 🇪🇸",
    "zh": "Chinese 🇨🇳",
    "zh-cn": "Chinese (Simplified) 🇨🇳",
    "zh-tw": "Chinese (Traditional) 🇹🇼",
    "hr": "Croatian 🇭🇷",
    "cs": "Czech 🇨🇿",
    "da": "Danish 🇩🇰",
    "nl": "Dutch 🇳🇱",
    "en": "English 🇬🇧",
    "et": "Estonian 🇪🇪",
    "fi": "Finnish 🇫🇮",
    "fr": "French 🇫🇷",
    "ka": "Georgian 🇬🇪",
    "de": "German 🇩🇪",
    "el": "Greek 🇬🇷",
    "gu": "Gujarati 🇮🇳",
    "he": "Hebrew 🇮🇱",
    "hi": "Hindi 🇮🇳",
    "hu": "Hungarian 🇭🇺",
    "is": "Icelandic 🇮🇸",
    "id": "Indonesian 🇮🇩",
    "ga": "Irish 🇮🇪",
    "it": "Italian 🇮🇹",
    "ja": "Japanese 🇯🇵",
    "kk": "Kazakh 🇰🇿",
    "ko": "Korean 🇰🇷",
    "ky": "Kyrgyz 🇰🇬",
    "lo": "Lao 🇱🇦",
    "lv": "Latvian 🇱🇻",
    "lt": "Lithuanian 🇱🇹",
    "mk": "Macedonian 🇲🇰",
    "ms": "Malay 🇲🇾",
    "mn": "Mongolian 🇲🇳",
    "ne": "Nepali 🇳🇵",
    "no": "Norwegian 🇳🇴",
    "fa": "Persian 🇮🇷",
    "pl": "Polish 🇵🇱",
    "pt": "Portuguese 🇵🇹",
    "pa": "Punjabi 🇵🇰",
    "ro": "Romanian 🇷🇴",
    "ru": "Russian 🇷🇺",
    "sr": "Serbian 🇷🇸",
    "sk": "Slovak 🇸🇰",
    "sl": "Slovenian 🇸🇮",
    "es": "Spanish 🇪🇸",
    "sv": "Swedish 🇸🇪",
    "tg": "Tajik 🇹🇯",
    "ta": "Tamil 🇮🇳",
    "te": "Telugu 🇮🇳",
    "th": "Thai 🇹🇭",
    "tr": "Turkish 🇹🇷",
    "tk": "Turkmen 🇹🇲",
    "uk": "Ukrainian 🇺🇦",
    "ur": "Urdu 🇵🇰",
    "uz": "Uzbek 🇺🇿",
    "vi": "Vietnamese 🇻🇳",
    "cy": "Welsh 🏴",
    "yo": "Yoruba 🇳🇬",
    "zu": "Zulu 🇿🇦"
}

def get_lang_buttons(page=0, per_page=4):
    """Inline tugmalar uchun pagination"""
    all_items = list(LANGUAGES.items())
    start = page * per_page
    end = start + per_page
    buttons = []

    row = []
    for code, name in all_items[start:end]:
        row.append(InlineKeyboardButton(text=name, callback_data=code))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"page_{page-1}"))
    if end < len(all_items):
        nav_buttons.append(InlineKeyboardButton(text="➡️ Oldinga", callback_data=f"page_{page+1}"))
    if nav_buttons:
        buttons.append(nav_buttons)

    
    buttons.append([InlineKeyboardButton(text=f"Sahifa {page+1}/{(len(all_items)-1)//per_page+1}", callback_data="noop")])

    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_admin_lang_buttons(page=0, per_page=4):
    """Admin uchun qo‘shilishi mumkin bo‘lgan tillar"""
    all_items = list(ALL_LANGS.items())
    start = page * per_page
    end = start + per_page
    buttons = []

    
    row = []
    for code, name in all_items[start:end]:
        row.append(InlineKeyboardButton(text=name, callback_data=f"add_{code}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    
    nav_buttons = []
    if page > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"admin_page_{page-1}"))
    if end < len(all_items):
        nav_buttons.append(InlineKeyboardButton(text="➡️ Oldinga", callback_data=f"admin_page_{page+1}"))
    if nav_buttons:
        buttons.append(nav_buttons)

    
    buttons.append([InlineKeyboardButton(text=f"Sahifa {page+1}/{(len(all_items)-1)//per_page+1}", callback_data="noop")])

    return InlineKeyboardMarkup(inline_keyboard=buttons)



