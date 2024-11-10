from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from core.di.services import get_employee_service
from application.services.employee_service import EmployeeService
from api.middlewares.auth_middleware import get_current_user
from domain.entities.user import User 
from domain.entities.employee import (
    Employee,
    EmployeeCreate,
    EmployeeUpdate,
    SalaryReport,
    AgeReport
)

router = APIRouter(prefix="/employees", tags=["employees"])

@router.get("/", response_model=List[Employee])
async def list_employees(
    service: EmployeeService = Depends(get_employee_service),
    current_user: User = Depends(get_current_user)
):
    all_employees = await service.get_all_employees()
    return all_employees

@router.post("/", response_model=Employee, status_code=status.HTTP_201_CREATED)
async def create_employee(
    employee: EmployeeCreate,
    service: EmployeeService = Depends(get_employee_service),
    current_user: User = Depends(get_current_user)
):
    created_employee = await service.create_employee(employee)
    return created_employee

@router.get("/{employee_id}", response_model=Employee)
async def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
    current_user: User = Depends(get_current_user)
):
    employee = await service.get_employee(employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return employee

@router.put("/{employee_id}", response_model=Employee)
async def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    service: EmployeeService = Depends(get_employee_service),
    current_user: User = Depends(get_current_user)
):
    updated_employee = await service.update_employee(employee_id, employee)
    if not updated_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return updated_employee

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
    current_user: User = Depends(get_current_user)
):
    deleted_employee = await service.delete_employee(employee_id)
    if not deleted_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )