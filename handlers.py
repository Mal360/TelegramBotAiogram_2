from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
import keyboards as kb
from config import telegram_bot_owner
from google_sheets import add_data_table

router = Router()


class BotStates(StatesGroup):
    entering_name = State()
    entering_contact = State()
    entering_text = State()


class User:
    name = None
    contact = None
    text = None


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(None)
    await message.answer(text='Главное меню', reply_markup=kb.build_kb_menu())


@router.callback_query(F.data == 'menu_command_0')
async def menu_command_0(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='''
Мы разрабатываем чат-ботов для бизнеса: Telegram, WhatsApp, CRM, AI, сайт
Список направлений:
    - Боты для продаж
    - Поддержка клиентов
    - Автоматизация HR и обучения
    - Игровые боты (геймификация)
    - AI-боты (Dialogflow, ChatGPT API)''')


@router.callback_query(F.data == 'menu_command_1')
async def menu_command_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='''
Презентация 3 пакетов (Базовый, Оптимум, Премиум) с ценами
Примеры кейсов (текстом или ссылками)''')


@router.callback_query(F.data == 'menu_command_2')
async def menu_command_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(BotStates.entering_name)
    await callback.answer()
    await callback.message.answer(text='Введите ваше имя')


@router.message(StateFilter(BotStates.entering_name))
async def reg_name(message: Message, state: FSMContext):
    await state.set_state(BotStates.entering_contact)
    User.name = message.text
    await message.answer(text='Введите ваш телефон или @username')


@router.message(StateFilter(BotStates.entering_contact))
async def reg_contact(message: Message, state: FSMContext):
    await state.set_state(BotStates.entering_text)
    User.contact = message.text
    await message.answer(text='Опишите задачу / что нужно')


@router.message(StateFilter(BotStates.entering_text))
async def reg_contact(message: Message, state: FSMContext):
    bot_msg = await message.answer(text='Отправляем данные')
    await state.set_state(None)
    User.text = message.text
    data = [User.name, User.contact, User.text, message.from_user.first_name,
            message.from_user.last_name, f'@{message.from_user.username}']
    text = f'''
Имя: {data[0]}
Контакт: {data[1]}
Запрос: {data[2]}
Telegram данные:
{data[3]}
{data[4]}
{data[5]}'''
    await message.bot.send_message(chat_id=telegram_bot_owner, text=text)
    add_data_table(data)
    await bot_msg.edit_text(text='Спасибо! Мы свяжемся в течение 1 рабочего дня')


@router.callback_query(F.data == 'menu_command_3')
async def menu_command_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='Часто задаваемые вопросы', reply_markup=kb.build_kb_faq())


@router.callback_query(F.data == 'menu_command_4')
async def menu_command_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='''
Менеджер: @yourmanager
Почта: bots@example.com''')


@router.callback_query(F.data == 'FAQ_command_0')
async def faq_command_0(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='Бот стоит 999')


@router.callback_query(F.data == 'FAQ_command_1')
async def faq_command_1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='На создание бота требуется 1 неделя')


@router.callback_query(F.data == 'FAQ_command_2')
async def faq_command_2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='''
Используемые технологии:
Python, aiogram, tgbotapi, Node.js, Telegraf, Go, ManyChat, Tidio''')


@router.callback_query(F.data == 'FAQ_command_3')
async def faq_command_3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='Под ключ?')


@router.callback_query(F.data == 'FAQ_command_4')
async def faq_command_4(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text='Работа с юридическим лицом')
