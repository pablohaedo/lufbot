import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN') 
BOT_USERNAME = os.getenv('BOT_USERNAME')
CALLBACK_URL = os.getenv('CALLBACK_URL')
DATABASE_URL = os.getenv('DATABASE_URL')
DEBUG = os.getenv('DEBUG', False) in ['true' , 'True', True]