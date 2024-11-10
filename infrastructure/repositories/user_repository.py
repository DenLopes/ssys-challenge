from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from domain.interfaces.user_repository import UserRepository
from domain.entities.user import User, UserCreate, UserUpdate
from infrastructure.database.models import UserModel

class SQLAlchemyUserRepository(UserRepository):
	_session: AsyncSession

	def __init__(self, session: AsyncSession) -> None:
		self._session = session

	async def create(self, user: UserCreate) -> User:
		db_user = UserModel(
			username=user.username,
			email=user.email,
			password=user.password,
			full_name=user.full_name
		)
		self._session.add(db_user)

		await self._session.commit()
		await self._session.refresh(db_user)

		return User.model_validate(db_user)

	async def update(self, id: int, user: UserUpdate) -> Optional[User]:
		query = select(UserModel).where(UserModel.id == id)
		result = await self._session.execute(query)
		db_user = result.scalar_one_or_none()

		if not db_user:
			return None

		user_data = user.model_dump(exclude_unset=True)

		for key, value in user_data.items():
			setattr(db_user, key, value)
		await self._session.commit()
		await self._session.refresh(db_user)

		return User.model_validate(db_user)

	async def delete(self, id: int) -> bool:
		query = select(UserModel).where(UserModel.id == id)
		result = await self._session.execute(query)
		user = result.scalar_one_or_none()

		if not user:
			return False

		await self._session.delete(user)
		await self._session.commit()

		return True

	async def get_by_id(self, id: int) -> Optional[User]:
		query = select(UserModel).where(UserModel.id == id)
		result = await self._session.execute(query)
		user = result.scalar_one_or_none()

		if not user:
			return None

		return User.model_validate(user)

	async def get_by_email(self, email: str) -> Optional[User]:
		query = select(UserModel).where(UserModel.email == email)
		result = await self._session.execute(query)
		user = result.scalar_one_or_none()

		if not user:
			return None

		return User.model_validate(user)

	async def get_by_username(self, username: str) -> Optional[User]:
		query = select(UserModel).where(UserModel.username == username)
		result = await self._session.execute(query)
		user = result.scalar_one_or_none()

		if not user:
			return None

		return User.model_validate(user)

	async def get_all(self) -> List[User]:
		query = select(UserModel)
		result = await self._session.execute(query)
		users = result.scalars().all()

		return [User.model_validate(user) for user in users]