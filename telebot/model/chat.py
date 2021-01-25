from telebot.base import Base
from sqlalchemy import Column, String, Integer, Boolean

class Chat(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key = True)
    type = Column(String)
    title = Column(String)
    all_members_are_administrators = Column(Boolean)

    def __init__():
        self.id = 999
        self.type = 'ph'
        self.all_members_are_administrators = True