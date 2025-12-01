import telebot, requests, json, threading, time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.function_comandos_disponiveis import comandos_disponiveis
from functions.function_frase_livro import frase_livro
from functions.function_capa_livro import capa_livro
from functions.function_link_livro import link_livro
from info import *

canal_pomodoro = canal()
chave = chave()
dono = dono()
bot = telebot.TeleBot(chave)

@bot.message_handler(commands=["start"])
def responder_start(mensagem):
    bot.send_message(dono, "bot funcionando!")
    bot.send_message(mensagem.chat.id, "Botões disponiveis:", reply_markup=comandos_disponiveis())

@bot.callback_query_handler(func=lambda call:True)
def callback_handler(call):
    if call.data == "publicar livro":
        with open(capa_livro(), "rb") as capa:
            bot.send_photo(canal_pomodoro, capa, caption=frase_livro(), reply_markup=link_livro())
    
    if call.data == "api":
        url = "http://127.0.0.1:5000/api/book"
        livros = requests.get(url)
        livros = livros.json()

        for book in livros:
            if book["id"] == 1:
                if isinstance(book["link"], str) and book["link"].startswith(("http://", "https://")):
                    keyboard = InlineKeyboardMarkup()
                    keyboard.add(InlineKeyboardButton("Comprar Livro", url=book["link"]))
                    
                    caminho_da_imagem = book["capa"]
                    with open(caminho_da_imagem, "rb") as capa:
                        bot.send_photo(canal_pomodoro, capa, caption=book["texto"], reply_markup=keyboard)

bot.polling()