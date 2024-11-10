from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    is_active: bool = True
    is_superuser: bool = False

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str
    is_active: bool = True
    is_superuser: bool = False

class UserInDB(User):
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    full_name: str | None = None
    password: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None

    class Config:
        from_attributes = True