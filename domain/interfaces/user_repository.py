from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.user import User, UserCreate, UserUpdate

class UserRepository(ABC):
	@abstractmethod
	async def create(self, user: UserCreate) -> User:
		pass

	@abstractmethod
	async def update(self, id: int, user: UserUpdate) -> Optional[User]:
		pass

	@abstractmethod
	async def delete(self, id: int) -> bool:
		pass

	@abstractmethod
	async def get_by_id(self, id: int) -> Optional[User]:
		pass

	@abstractmethod
	async def get_by_email(self, email: str) -> Optional[User]:
		pass

	@abstractmethod
	async def get_by_username(self, username: str) -> Optional[User]:
		pass

	@abstractmethod
	async def get_all(self) -> List[User]:
		pass