from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.employee import Employee, EmployeeCreate, EmployeeUpdate

class EmployeeRepository(ABC):
    @abstractmethod
    async def create(self, employee: EmployeeCreate) -> Employee:
        pass
    
    @abstractmethod
    async def update(self, id: int, employee: EmployeeUpdate) -> Optional[Employee]:
        pass
    
    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass
    
    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[Employee]:
        pass
    
    @abstractmethod
    async def get_all(self) -> List[Employee]:
        pass