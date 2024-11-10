from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from core.di.services import get_user_service
from application.services.user_service import UserService
from api.middlewares.auth_middleware import get_current_user
from domain.entities.user import UserCreate, User, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(
	user_data: UserCreate,
	user_service: UserService = Depends(get_user_service),
	current_user: User = Depends(get_current_user)
):
	created_user = await user_service.create_user(user_data)
	return created_user

@router.get("/{user_id}", response_model=User)
async def get_user(
	user_id: int,
	user_service: UserService = Depends(get_user_service),
	current_user: User = Depends(get_current_user)
):
	user = await user_service.get_user(user_id)
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
	return user

@router.get("/", response_model=List[User])
async def list_users(
	user_service: UserService = Depends(get_user_service),
	current_user: User = Depends(get_current_user)
):
	all_users = await user_service.get_all_users()
	return all_users

@router.put("/{user_id}", response_model=User)
async def update_user(
	user_id: int,
	user_data: UserUpdate,
	user_service: UserService = Depends(get_user_service),
	current_user: User = Depends(get_current_user)
):
	user = await user_service.update_user(user_id, user_data)
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
	return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
	user_id: int,
	user_service: UserService = Depends(get_user_service),
	current_user: User = Depends(get_current_user)
):
	user_deleted = await user_service.delete_user(user_id)
	if not user_deleted:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
	return {"message": "User deleted successfully"}