from typing import List

from app.decorator.response_decorator import response_wrapper
from app.models.chat import Chat
from app.models.conversation import Conversation
from app.models.user import User
from app.providers.chat_client import client
from app.schemas.conversation import ChatBase


class ConversationList:

    def __init__(self, user: User):
        self.user = user

    @response_wrapper
    def respond(self):
        conversations = Conversation.select().where(Conversation.user_id == self.user.id,
                                                    Conversation.delete_flag == 0).order_by(
            Conversation.conversation_id)[:]

        return conversations


class ConversationDetail:

    def __init__(self, conversation_id: int, user: User):
        self.conversation_id = conversation_id
        self.user = user

    @response_wrapper
    def respond(self):
        chats = Chat.select().where(Chat.conversation_id == self.conversation_id,
                                    Chat.user_id == self.user.id).order_by(Chat.created_at, Chat.chat_id)[:]

        return chats


class ConversationCreator:

    def __init__(self, user: User):
        self.user = user

    @response_wrapper
    def respond(self):
        conversation = Conversation.create(user_id=self.user.id, title="")

        return conversation


class SendMessage:

    def __init__(self, chat: ChatBase, user: User):
        self.chat = chat
        self.user = user

    def _get_history(self):
        chats = Chat.select().where(Chat.conversation_id == self.chat.conversation_id,
                                    Chat.user_id == self.user.id).order_by(
            Chat.created_at, Chat.chat_id)[:]

        return chats

    def _update_conversation_title(self):
        pass

    @response_wrapper
    def respond(self):
        chats: List[Chat] = self._get_history()
        his_message = [{"role": c.role, "content": c.content} for c in chats]
        if not his_message:
            self._update_conversation_title()
        messages = his_message + [{"role": "user", "content": self.chat.content}]

        completion = client.chat.completions.create(model=self.chat.model, messages=messages)

        Chat.create(conversation_id=self.chat.conversation_id, user_id=self.user.id, content=self.chat.content,
                    role="user")
        chat_reply = Chat.create(conversation_id=self.chat.conversation_id, user_id=self.user.id,
                                 content=completion.choices[0].message.content, role="assistant")

        return chat_reply
