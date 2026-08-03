from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.dependencies import current_user
from app.schemas.user import UserResponse
from app.models.user import User
router = APIRouter(
    prefix="/users",
    tags=["Users"],
)
@router.get(
    "/me",
    response_model=UserResponse
    )
def get_me(
    current_user: User = Depends(current_user),
):
    return current_user

