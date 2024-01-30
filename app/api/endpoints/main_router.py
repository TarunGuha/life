from fastapi import APIRouter
from api.endpoints.tracker import router as tracker_router

router = APIRouter()


@router.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome To Life!"}


@router.get("/health", tags=["Health Check"])
async def health():
    return {"status": "ok"}


router.include_router(router=tracker_router)
