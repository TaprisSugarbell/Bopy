import random
import string
from telegram import ChatAction, ParseMode
from telegram.ext import ConversationHandler

# VARIABLES
INPUTNUM = 0

# Password
def pswcommand(update, context):
    text = update.message.text
    pfaw = text.split()
    try:
        pfa = int(pfaw[1:])
        password = pfa
    except:
        pfa = 0
    if pfa[1] <= 0:
        update.message.reply_text('Parámetros\n1. Alfabeto\n2. Mayúsculas\n3. Minúsculas\n4. Números\n5. Alfanumérico\n6. Alfanumérico y Símbolos\nIngresa el número de tu elección y/o la longitud,\npor defecto "8"\nPor ejemplo 5 20, crea una contraseña alfanumérica de 20 caracteres.')
    elif pfa[2] <= 8:
        update.message.reply_text('Parámetros\n1. Alfabeto\n2. Mayúsculas\n3. Minúsculas\n4. Números\n5. Alfanumérico\n6. Alfanumérico y Símbolos\nIngresa el número de tu elección y/o la longitud,\npor defecto "8"\nPor ejemplo 5 20, crea una contraseña alfanumérica de 20 caracteres.')
    else:
        pass
    return INPUTNUM, password


def password_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text='Parámetros\n1. Alfabeto\n2. Mayúsculas\n3. Minúsculas\n4. Números\n5. Alfanumérico\n6. Alfanumérico y Símbolos\nIngresa el número de tu elección y/o la longitud,\npor defecto "8"\nPor ejemplo 5 20, crea una contraseña alfanumérica de 20 caracteres.')
    return INPUTNUM


def input_password(update, context):
    password = update.message.text
    chat = update.message.chat
    s = ''
    afn = password.split()
    m = int(afn[0])
    try:
        n = int(afn[1])
    except IndexError:
        n = 8

    if m == 1:
        c = list(string.ascii_letters)
    elif m == 2:
        c = list(string.ascii_uppercase)
    elif m == 3:
        c = list(string.ascii_lowercase)
    elif m == 4:
        c = list(string.digits)
    elif m == 5:
        c = list(string.hexdigits)
    elif m == 6:   
        c = list(string.printable)
        c = c[:-6]

    for i in range(n):
        s += random.choice(c)

    #asdfghjk = s.format(parsemode=parsemode.ParseMode.MARKDOWN)
    #print(asdfghjk)
    chat.send_action(
        action=ChatAction.TYPING,
        timeout=None
        )
    chat.send_message(
        text=f"Tu contraseña es: `{s}`", parse_mode=ParseMode.MARKDOWN,
    )
    return ConversationHandler.END