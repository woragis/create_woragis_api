from fastapi import APIRouter
from routes.user import router as user_router
from routes.admin.user import router as admin_router

router = APIRouter()
router.include_router(user_router)
router.include_router(admin_router)
