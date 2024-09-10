from peewee import IntegerField, CharField, TextField

from app.models.base_model import BaseModel


class Chat(BaseModel):
    class Meta:
        table_name = 'user_chat'

    chat_id = IntegerField(primary_key=True)
    conversation_id = IntegerField()
    user_id = IntegerField()
    role = CharField()
    content = TextField()
