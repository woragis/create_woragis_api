from fastapi import APIRouter
from routes.user import router as user_router
from routes.admin.user import router as admin_router
from routes.password_reset import router as password_reset_router

router = APIRouter()
router.include_router(user_router)
router.include_router(admin_router)
router.include_router(password_reset_router)
