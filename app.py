# import everything
from flask import Flask, request
import telegram
import re
from time import sleep
from telebot.config import BOT_TOKEN, BOT_USERNAME, CALLBACK_URL, DATABASE_URL
import psycopg2

global bot
global TOKEN

TOKEN = BOT_TOKEN
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)



@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       PH237, HOLA LUJAN
       """
       # send the welcoming message
       
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

   else:
       try:
           # clear the message we got from any non alphabets
           text = re.sub(r"W", "_", text)
           # create the api link for the avatar based on http://avatars.adorable.io/
           url = "Lujaaan, no me escribas {}".format(text.strip())
           # reply with a photo to the name the user sent,
           # note that you can send photos by url and telegram will fetch it for you
           if text == 'GOLPEAR':
               url='Golpear no esta bien'
           bot.sendChatAction(chat_id=chat_id, action="typing")
           if text == 'ABRAZAR':
               url='Love is love'
           sleep(1.5)
           keyboard=[['GOLPEAR','ABRAZAR']]
           reply_markup = telegram.ReplyKeyboardMarkup(keyboard,
                one_time_keyboard=True,
                resize_keyboard=True)
           bot.send_message(chat_id=chat_id, reply_to_message_id=msg_id, text=url, reply_markup=reply_markup)
           #bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
       except Exception as error:
           # if things went wrong
           bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)
           print(error)

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

@app.route('/db')
def index():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        res = cur.execute("""create database bot;""")
        return res
    except Exception as error:
        return error
    


if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)