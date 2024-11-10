from fastapi import Depends
from domain.interfaces.user_repository import UserRepository
from domain.interfaces.employee_repository import EmployeeRepository
from application.services.user_service import UserService
from application.services.employee_service import EmployeeService
from application.services.auth_service import AuthService
from application.services.employee_reports_service import EmployeeReportsService
from .repositories import get_user_repository, get_employee_repository

async def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(user_repository)

async def get_employee_service(
    employee_repository: EmployeeRepository = Depends(get_employee_repository)
) -> EmployeeService:
    return EmployeeService(employee_repository)

async def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository)
) -> AuthService:
    return AuthService(user_repository)

async def get_employee_reports_service(
    employee_repository: EmployeeRepository = Depends(get_employee_repository)
) -> EmployeeReportsService:
    return EmployeeReportsService(employee_repository)