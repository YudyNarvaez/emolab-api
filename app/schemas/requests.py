import datetime
from typing import Dict, Union
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: str
    nit: Union[str, None] = None
    address: Union[str, None] = None
    contact: Union[str, None] = None
    is_parent: Union[bool, None] = True
    is_health_professional: Union[bool, None] = False


class KidCreate(BaseModel):
    name: str
    last_name: str
    birthday: datetime.date
    has_asperger: bool = False
    gender: str = 'M'

class AnalysisResult(BaseModel):
    emocion: str
    probs: Dict