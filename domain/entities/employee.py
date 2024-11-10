from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: Decimal = Field(max_digits=10, decimal_places=2)
    birth_date: date

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
        json_encoders = {
            date: lambda v: v.strftime("%d-%m-%Y")
        }


class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    department: str | None = None
    salary: Decimal | None = Field(None, max_digits=10, decimal_places=2)
    birth_date: date | None = None

class SalaryReport(BaseModel):
    lowest: Employee
    highest: Employee
    average: Decimal = Field(max_digits=10, decimal_places=2)

class AgeReport(BaseModel):
    younger: Employee
    older: Employee
    average: Decimal = Field(max_digits=10, decimal_places=2)