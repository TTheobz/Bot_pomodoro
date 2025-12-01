import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def comandos_disponiveis():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Promoção Livros", callback_data="publicar livro"),
        InlineKeyboardButton("Teste de api", callback_data="api")
    )
    return markup