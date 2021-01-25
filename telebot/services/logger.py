from telebot.config import DEBUG
from telebot.model.loglevel import LogLevel
from typing import NoReturn

def log(message: str, level : LogLevel = LogLevel.INFO) -> NoReturn:
    if (not DEBUG) and (level < LogLevel.ERROR):
        return
    print(message)