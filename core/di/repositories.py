from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.employee_repository import EmployeeRepository
from infrastructure.repositories.user_repository import SQLAlchemyUserRepository
from infrastructure.repositories.employee_repository import SQLAlchemyEmployeeRepository
from .database import get_db

async def get_user_repository(
    session: AsyncSession = Depends(get_db)
) -> UserRepository:
    return SQLAlchemyUserRepository(session)

async def get_employee_repository(
    session: AsyncSession = Depends(get_db)
) -> EmployeeRepository: 
    return SQLAlchemyEmployeeRepository(session) 