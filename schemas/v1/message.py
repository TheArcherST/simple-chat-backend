from pydantic import BaseModel


class Message(BaseModel):
    id: int
    from_user_id: int
    chat_id: int
    text: str


class MessageList(BaseModel):
    __root__: list[Message]
