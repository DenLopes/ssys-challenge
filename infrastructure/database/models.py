from sqlalchemy import Column, Integer, String, DECIMAL, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmployeeModel(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(DECIMAL(10, 2), nullable=False)
    birth_date = Column(Date, nullable=False)

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)