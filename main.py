import telebot, requests, json, threading, time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.function_comandos_disponiveis import comandos_disponiveis
from functions.function_frase_livro import frase_livro
from functions.function_capa_livro import capa_livro
from functions.function_link_livro import link_livro

canal_pomodoro = -1002810977719

chave = ""
dono = ""
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

bot.polling()