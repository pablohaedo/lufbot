import os
from dotenv import load_dotenv

load_dotenv()

MY_ENV_VAR = os.getenv('MY_ENV_VAR')

BOT_TOKEN = os.getenv('BOT_TOKEN') 
BOT_USERNAME = os.getenv('BOT_USERNAME')
CALLBACK_URL = os.getenv('CALLBACK_URL')