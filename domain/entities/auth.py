from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str = "admin"
    password: str = "admin"

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int