from datetime import datetime

from pydantic import BaseModel, Field


class ConversationBase(BaseModel):
    conversation_id: int = Field(description="会话id")
    title: str = Field(None, description="标题")
    create_at: datetime = Field(None, description="创建时间")
    update_at: datetime = Field(None, description="更新时间")

    class Config:
        orm_mode = True


class ChatBase(BaseModel):
    conversation_id: int = Field(description="会话id")
    content: str = Field(description="讯息")
    model: str = Field("gpt-4o-mini", description="模型")


class ChatResponse(BaseModel):
    conversation_id: int = Field(description="会话id")
    content: str = Field(description="讯息")
    role: str = Field(description="角色")
    created_at: datetime = Field(description="创建时间")

    class Config:
        orm_mode = True
