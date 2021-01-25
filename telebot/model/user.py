from telebot.base import Base
from sqlalchemy import Column, String, Integer, Boolean

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    language_code = Column(String)
    is_bot = Column(Boolean)

    def __init__(self):
        self.id = 999
        self.first_name = 'ph'
        self.last_name = 'test'