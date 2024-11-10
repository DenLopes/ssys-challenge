from typing import List, Optional
from datetime import date
from statistics import mean
from domain.interfaces.employee_repository import EmployeeRepository
from domain.entities.employee import (
    Employee, EmployeeCreate, EmployeeUpdate,
    SalaryReport, AgeReport
)

class EmployeeService:
    _repository: EmployeeRepository

    def __init__(self, repository: EmployeeRepository) -> None:
        self._repository = repository

    async def create_employee(self, employee: EmployeeCreate) -> Employee:
        return await self._repository.create(employee)

    async def update_employee(
        self, id: int, employee: EmployeeUpdate
    ) -> Optional[Employee]:
        return await self._repository.update(id, employee)

    async def delete_employee(self, id: int) -> bool:
        return await self._repository.delete(id)

    async def get_employee(self, id: int) -> Optional[Employee]:
        return await self._repository.get_by_id(id)

    async def get_all_employees(self) -> List[Employee]:
        return await self._repository.get_all()