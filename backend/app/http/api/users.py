from fastapi import APIRouter, Depends

from app.http import deps
from app.http.deps import get_db
from app.models.user import User
from app.schemas.user import UserDetail, UserPassword,UserPasswordModify
from app.services.users.user_manager import CreateUser, ModifyUser

router = APIRouter(
    prefix="/users"
)


@router.get("/me", response_model=UserDetail, dependencies=[Depends(get_db)])
def me(auth_user: User = Depends(deps.get_auth_user)):
    """
    当前登录用户信息
    """
    return auth_user

@router.post("/create_user", response_model=UserDetail, dependencies=[Depends(get_db)])
def create_user(request_data: UserPassword):
    return CreateUser(request_data).respond()

@router.post("/modify_password", response_model=UserDetail, dependencies=[Depends(get_db)])
def modify_password(request_data: UserPasswordModify):
    return ModifyUser(request_data).respond()
