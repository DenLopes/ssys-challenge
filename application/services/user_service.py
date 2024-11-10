from typing import List, Optional
from domain.interfaces.user_repository import UserRepository
from domain.entities.user import User, UserCreate, UserUpdate

class UserService:
    _user_repo: UserRepository

    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    async def create_user(self, user: UserCreate) -> User:
        return await self._user_repo.create(user)

    async def get_user(self, id: int) -> Optional[User]:
        return await self._user_repo.get_by_id(id)

    async def get_all_users(self) -> List[User]:
        return await self._user_repo.get_all()
    
    async def update_user(self, id: int, user: UserUpdate) -> Optional[User]:
        return await self._user_repo.update(id, user)
    
    async def delete_user(self, id: int) -> bool:
        return await self._user_repo.delete(id)