# import everything
from flask import Flask, request
import telegram
import re
from time import sleep
from telebot.messages import messageList
from telebot.config import BOT_TOKEN, BOT_USERNAME, CALLBACK_URL, DATABASE_URL
import psycopg2
from telebot.services.logger import log
from telebot.base import Base, Session, engine

global bot
global TOKEN

TOKEN = BOT_TOKEN
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    log(str(update))
    try:
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
    except: 
        return 'ok'

    # Telegram understands UTF-8, so encode text for unicode compatibility    
    try:

        if update.message.text is None:
            log('sale por falta de text???')
            bot.sendMessage(chat_id=chat_id, text='Mh... no me llegó el mensaje', reply_to_message_id=msg_id)
            return 'ok'
        #    chatInfo = bot.getChat(chat_id)
        #    log(chatInfo)
        text = update.message.text.encode('utf-8').decode()
        # for debugging purposes only
        log("got text message : {}".format(text))
        # the first time you chat with the bot AKA the welcoming message

        if text not in messageList:
            text = '/start'

        bot.sendChatAction(chat_id=chat_id, action="typing")
        nodo = messageList[text]
        reply_markup = {}
        if 'keyboard' in nodo:
            reply_markup = telegram.ReplyKeyboardMarkup(nodo['keyboard'],
                one_time_keyboard=True,
                resize_keyboard=True)
        for message in nodo['messages']:
            if message.startswith('IMG:'):
                path = './telebot/resources/imgs/{}'.format(message[4:])
                log('LA IMAGEN ESTA EN {}'.format(path))
                bot.send_photo(chat_id, photo=open(path, 'rb'))
            elif message.startswith('VID:'):
                path = './telebot/resources/videos/{}'.format(message[4:])
                log('EL VIDEO ESTA EN {}'.format(path))
                bot.send_video(chat_id, video=open(path, 'rb'), supports_streaming=True)
            elif message.startswith('FIL:'):
                path = './telebot/resources/docs/{}'.format(message[4:])
                log('EL DOCUMENTO ESTA EN {}'.format(path))
                bot.send_document(chat_id, document=open(path, 'rb'))
            else:
                bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)
    except telegram.error.Unauthorized:
        log('Sale con error unauthorized: {}'.format(update))
        return "ok"
    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=CALLBACK_URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'

@app.route('/migrate', methods=['GET'])
def migrate():
    ses = Session()
    from telebot.model.user import User
    from telebot.model.message import Message
    from telebot.model.chat import Chat

    # Base.metadata.create_all(engine)
    # session = Session()

    # ch = Chat()
    # us = User()
    # ms = Message()
    # ms.user = us
    # ms.chat = ch

    # session.add(ms)
    
    # session.commit()
    # session.close()

    session = Session()
    users = session.query(User).all()
    printList(users)
    users = session.query(Chat).all()
    printList(users)
    users = session.query(Message).all()
    printList(users)
    return 'ok'

def printList(users):
    log('\n### All movies:')
    for movie in users:
        log('{} was released on {}'.format(movie))
    log('')

@app.route('/dbStart', methods=['GET'])
def db():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        # cur.execute("""create database bot;""")
        #cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
        #cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
        c1 = """create table if not exists `chat`  (
    `id` NUMERIC PRIMARY KEY,
    `type` varchar(50) DEFAULT '',
    `title` varchar(255) DEFAULT '',
    `all_members_are_administrators` boolean default false
    );"""

        c2 = """create table if not exists `user` (
    `id` NUMERIC PRIMARY KEY,
    `first_name` VARCHAR(255) default '',
    `last_name` VARCHAR(255) DEFAULT '',
    `language_code` VARCHAR(5) default '',
    `is_bot` boolean defaulr false
);"""

        c3 = """create table if not exists `message` (
    `message_id` NUMERIC not null,
    `date` TIMESTAMP not null,
    `chat_id` NUMERIC NOT NULL REFERENCES `chat` (`id`),
    `text` TEXT DEFAULT '',
    `delete_chat_photo` BOOLEAN default false,
    `group_chat_created` BOOLEAN default false,
    `supergroup_chat_created` BOOLEAN default false,
    `channel_chat_created` BOOLEAN default false,
    `user_id` NUMERIC not null REFERENCES `user` (`id`)
);"""
        log(cur.execute(c1))
        log(c1)
        log(cur.execute(c2))
        log(c2)
        log(cur.execute(c3))
        log(c3)
        cur.close()
        # commit the changes
        conn.commit()
        conn.close()
        return 'ok'
    except Exception as error:
        log('LLEGA ACAAAA')
        log(str(error))
        return '.'

@app.route('/db', methods=['GET'])
def dbSelect():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("SELECT * FROM test;")
        ret = cur.fetchone()
        log(ret)
        cur.close()
        conn.close()
        return ret
    except Exception as error:
        log('LLEGA')
        log(str(error))
        return '.'


if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)