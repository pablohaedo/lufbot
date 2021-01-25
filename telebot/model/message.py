from telebot.base import Base
from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, ForeignKey, Sequence
from sqlalchemy.orm import relationship

MESSAGE_ID = Sequence('message_id_seq', start=1000)

class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, MESSAGE_ID, primary_key= True, server_default=MESSAGE_ID.next_value())
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

    def __init__(self):
        self.message_id = 999
        self.text = 'wowowowowo'