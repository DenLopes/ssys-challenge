from typing import List
from datetime import date
from statistics import mean
from math import floor
from domain.interfaces.employee_repository import EmployeeRepository
from domain.entities.employee import Employee, SalaryReport, AgeReport

class EmployeeReportsService:
    def __init__(self, employee_repository: EmployeeRepository) -> None:
        self._repository = employee_repository

    async def get_salary_report(self) -> SalaryReport:
        employees = await self._repository.get_all()
        if not employees:
            return None

        sorted_by_salary = sorted(employees, key=lambda x: x.salary)
        lowest = sorted_by_salary[0]
        highest = sorted_by_salary[-1]
        average = round(mean([emp.salary for emp in employees]), 2)

        return SalaryReport(
            lowest=lowest,
            highest=highest,
            average=average
        )

    async def get_age_report(self) -> AgeReport:
        employees = await self._repository.get_all()
        if not employees:
            return None

        today = date.today()
        employee_ages = [
            (emp, (today - emp.birth_date).days / 365.25)
            for emp in employees
        ]
        sorted_by_age = sorted(employee_ages, key=lambda x: x[1])

        younger = sorted_by_age[0][0]  
        older = sorted_by_age[-1][0] 
        average_age = floor(mean([age for _, age in employee_ages]))

        return AgeReport(
            younger=younger,
            older=older,
            average=average_age
        )