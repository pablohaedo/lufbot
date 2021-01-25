from telebot.base import Base
from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

class Message(Base):
    __tablename__ = 'message'

    message_id = Column(Integer)
    date = Column(TIMESTAMP)

    chat_id = Column(Integer, ForeignKey('chat.id'))
    chat = relationship("Chat", backref="messages")

    text = Column(String)
    
    delete_chat_photo = Column(Boolean)
    group_chat_created = Column(Boolean)
    supergroup_chat_created = Column(Boolean)
    channel_chat_created = Column(Boolean)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref="messages")

    def __init__():
        self.message_id = 999
        self.text = 'wowowowowo'