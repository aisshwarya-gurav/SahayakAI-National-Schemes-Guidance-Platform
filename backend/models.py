from pydantic import BaseModel

class UserProfile(BaseModel):
    age: int
    gender: str
    state: str
    occupation: str
    annual_income: int
    category: str


class ChatRequest(BaseModel):
    message: str