import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def link_livro():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    plataforma_sorteada = "https://amzn.to/4hSSaoo"
    markup.add(
        InlineKeyboardButton("🔥Compre Agora📚", url=plataforma_sorteada)
    )
    return markup