from fastapi import APIRouter, Depends
from app.schemas.responses import UserResponse
from app.models.user import User
from app.api import deps
router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def read_current_user(
    current_user: User = Depends(
        deps.get_current_user
    )
):
    """Get current user"""
    return current_user