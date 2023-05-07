from pydantic import BaseModel


class Message(BaseModel):
    id: int
    from_user: str
    chat: str
    text: str


class MessageList(BaseModel):
    __root__: list[Message]
