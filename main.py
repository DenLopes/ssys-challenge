from fastapi import FastAPI
from api.v1.routes import employee_routes, user_routes, auth_routes, employee_reports_routes
from infrastructure.database.connection import engine
import uvicorn

app = FastAPI(
    title="SSYS Employee Manager",
    version="0.0.1",
    description="Employee Management API",
)

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(employee_routes.router)
app.include_router(employee_reports_routes.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True
    )