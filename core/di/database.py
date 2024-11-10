from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.connection import get_session

get_db = get_session