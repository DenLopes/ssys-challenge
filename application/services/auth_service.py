from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from domain.interfaces.user_repository import UserRepository
from domain.entities.user import User
from domain.entities.auth import TokenResponse
from core.config.settings import settings
from fastapi import HTTPException, status

class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repo = user_repository

    async def login(self, username: str, password: str) -> Optional[TokenResponse]:
        user = await self._user_repo.get_by_username(username)
        if not user or not self._verify_password(password, user.password):
            return None
            
        try:
            access_token = self._create_access_token(user)
            return TokenResponse(
                access_token=access_token,
                expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not create access token"
            )

    def _create_access_token(self, user: User) -> str:
        try:
            expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            expire = datetime.utcnow() + expires_delta
            
            to_encode = {
                "sub": str(user.id),
                "exp": expire,
                "username": user.username
            }
            
            return jwt.encode(
                to_encode,
                settings.SECRET_KEY,
                algorithm=settings.ALGORITHM
            )
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Token creation failed"
            )

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        from utils.security import verify_password
        return verify_password(plain_password, hashed_password)