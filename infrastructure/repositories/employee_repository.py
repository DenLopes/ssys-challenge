from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from domain.interfaces.employee_repository import EmployeeRepository
from domain.entities.employee import Employee, EmployeeCreate, EmployeeUpdate
from infrastructure.database.models import EmployeeModel

class SQLAlchemyEmployeeRepository(EmployeeRepository):
    _session: AsyncSession
    
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, employee: EmployeeCreate) -> Employee:
        db_employee = EmployeeModel(
            name=employee.name,
            email=employee.email,
            department=employee.department,
            salary=employee.salary,
            birth_date=employee.birth_date
        )
        self._session.add(db_employee)
        await self._session.commit()
        await self._session.refresh(db_employee)
        return Employee.model_validate(db_employee)

    async def update(self, id: int, employee: EmployeeUpdate) -> Optional[Employee]:
        query = select(EmployeeModel).where(EmployeeModel.id == id)
        result = await self._session.execute(query)
        db_employee = result.scalar_one_or_none()
        
        if not db_employee:
            return None

        update_data = employee.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_employee, key, value)

        await self._session.commit()
        await self._session.refresh(db_employee)
        
        return Employee.model_validate(db_employee)

    async def delete(self, id: int) -> bool:
        query = select(EmployeeModel).where(EmployeeModel.id == id)
        result = await self._session.execute(query)
        db_employee = result.scalar_one_or_none()
        
        if not db_employee:
            return False

        await self._session.delete(db_employee)
        await self._session.commit()
        return True

    async def get_by_id(self, id: int) -> Optional[Employee]:
        query = select(EmployeeModel).where(EmployeeModel.id == id)
        result = await self._session.execute(query)
        db_employee = result.scalar_one_or_none()
        
        if not db_employee:
            return None

        return Employee.model_validate(db_employee)

    async def get_all(self) -> List[Employee]:
        query = select(EmployeeModel)
        result = await self._session.execute(query)
        db_employees = result.scalars().all()

        return [Employee.model_validate(emp) for emp in db_employees]