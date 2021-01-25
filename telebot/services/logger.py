from config import DEBUG
from  ..model.loglevel import LogLevel

def log(message, level = LogLevel.INFO):
    if (not DEBUG) and (level < LogLevel.ERROR):
        return
    print(message)