from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def build_kb_menu():
    buttons_menu = ('Что мы делаем',
                    'Тарифы и кейсы',
                    'Оставить заявку',
                    'Частые вопросы',
                    'Связаться с нами')
    main = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, callback_data=f'menu_command_{i}')] for i, text in enumerate(buttons_menu)
    ])
    return main

def build_kb_faq():
    buttons_FAQ = ('Сколько стоит бот?',
                   'За сколько вы сделаете?',
                   'Какие технологии используете?',
                   'Можете ли сделать под ключ?',
                   'Работаете с юр. лицами?')
    FAQ = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, callback_data=f'FAQ_command_{i}')] for i, text in enumerate(buttons_FAQ)
    ])
    return FAQ
