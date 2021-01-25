from telebot.config import DEBUG
from telebot.model.loglevel import LogLevel

def log(message, level = LogLevel.INFO):
    if (not DEBUG) and (level < LogLevel.ERROR):
        return
    print(message)