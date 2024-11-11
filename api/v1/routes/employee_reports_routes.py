from fastapi import APIRouter, Depends, HTTPException, status
from api.middlewares.auth_middleware import get_current_user
from core.di.services import get_employee_reports_service
from application.services.employee_reports_service import EmployeeReportsService
from domain.entities.employee import SalaryReport, AgeReport
from domain.entities.user import User

router = APIRouter(prefix="/reports/employees", tags=["Employee reports"])

@router.get("/salary/", response_model=SalaryReport)
async def get_salary_report(
    current_user: User = Depends(get_current_user),
    reports_service: EmployeeReportsService = Depends(get_employee_reports_service)
):
    report = await reports_service.get_salary_report()
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")
    return report

@router.get("/age/", response_model=AgeReport)
async def get_age_report(
    current_user: User = Depends(get_current_user),
    reports_service: EmployeeReportsService = Depends(get_employee_reports_service)
):
    report = await reports_service.get_age_report()
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")
    return report