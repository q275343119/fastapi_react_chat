from peewee import IntegerField, CharField

from app.models.base_model import BaseModel


class Conversation(BaseModel):
    class Meta:
        table_name = 'user_conversation'

    conversation_id = IntegerField(primary_key=True)
    user_id = IntegerField()
    title = CharField()
    delete_flag = IntegerField()

    def is_enabled(self):
        return self.delete_flag == 0
