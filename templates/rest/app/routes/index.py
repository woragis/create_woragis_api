from fastapi import APIRouter
from app.routes.user import router as user_router
from app.routes.admin.user import router as admin_router
from app.routes.password_reset import router as password_reset_router
from app.routes.kafka import router as kafka_router

router = APIRouter()
router.include_router(user_router)
router.include_router(admin_router)
router.include_router(password_reset_router)
router.include_router(kafka_router)
