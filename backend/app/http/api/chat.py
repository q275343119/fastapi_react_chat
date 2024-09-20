from typing import List

from fastapi import APIRouter, Depends

from app.http import deps
from app.models.user import User
from app.schemas.base import ResultModel
from app.schemas.conversation import ConversationBase, ChatBase, ChatResponse
from app.services.chat.conversation import ConversationList, ConversationDetail, ConversationCreator, SendMessage

router = APIRouter(
    prefix="/chat"
)


@router.post("/getConversationList", response_model=ResultModel[List[ConversationBase]])
def get_conversation_list(user: User = Depends(deps.get_auth_user)):
    conversation_list = ConversationList(user)
    return conversation_list.respond()


@router.get("/getConversationDetail", response_model=ResultModel[List[ChatResponse]])
def get_conversation_detail(conversation_id: int, user: User = Depends(deps.get_auth_user)):
    chats = ConversationDetail(conversation_id, user)
    return chats.respond()


@router.post("/createConversation", response_model=ConversationBase)
def create_conversation(user: User = Depends(deps.get_auth_user)):
    conversation = ConversationCreator(user)

    return conversation.respond()


@router.post("/sendMessage", response_model=ChatResponse)
def send_message(chat: ChatBase, user: User = Depends(deps.get_auth_user)):
    send_msg = SendMessage(chat, user)

    return send_msg.respond()
