import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def frase_livro():
    titulo = "A última canção de amor"
    categoria = "Romance"
    valor = "23,97"
    preco_original = "79,90"
    nota = 0 

    return f"""🔥 Oferta Amazon!!!
    
📖 {titulo} [{categoria}]
🛒 R${valor} (preço original: {preco_original})

⭐ {nota} / 5
"""