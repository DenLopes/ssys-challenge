from fastapi import APIRouter, Depends, HTTPException, status
from core.di.services import get_auth_service
from application.services.auth_service import AuthService
from domain.entities.auth import LoginRequest, TokenResponse  # You'll need to create these

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
async def login(
    login_data: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
):	
    token = await auth_service.login(login_data.username, login_data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token