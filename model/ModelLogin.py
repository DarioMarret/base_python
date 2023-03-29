from pydantic import BaseModel
from typing import Optional, List, Dict
from enum import Enum



class LoginModel(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    message: str
    status: int
    data: Optional[Dict[str, str]] = None