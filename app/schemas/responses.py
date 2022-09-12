from typing import Dict, List, Union
from pydantic import BaseModel, EmailStr


class AccessTokenResponse(BaseModel):
    token_type: str = None
    access_token: str
    expires_at: int = None
    issued_at: int = None


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    lat_name: Union[str, None] = None
    nit: Union[str, None] = None
    address: Union[str, None] = None
    contact: Union[str, None] = None
    is_parent: bool
    is_health_professional: bool
    kids: Union[List[Dict], None] = None