from fastapi import APIRouter
from api.routes import parking

router = APIRouter()
router.include_router(parking.router, tags=["parking"], prefix="/v1")
