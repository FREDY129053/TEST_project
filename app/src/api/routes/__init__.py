from app.src.api.routes.user_router import user_router
from app.src.api.routes.company_router import company_router

from fastapi import APIRouter

group_router = APIRouter()

group_router.include_router(company_router)
group_router.include_router(user_router)