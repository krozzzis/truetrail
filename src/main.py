from fastapi import FastAPI

from routes.activities import router as activities_router
from routes.users import router as users_router

app = FastAPI(title="TrueTrail")

app.include_router(activities_router)
app.include_router(users_router)
