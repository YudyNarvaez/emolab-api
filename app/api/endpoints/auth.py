from typing import List, Union
from app.schemas.requests import KidCreate, UserCreate
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import deps
from app.core import security
from app.models import Kid, User
from app.schemas.responses import AccessTokenResponse, UserResponse

router = APIRouter()


@router.post("/access-token", response_model=AccessTokenResponse)
async def login_access_token(
    session: AsyncSession = Depends(deps.get_session),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """OAuth2 compatible token, get an access token for future requests using username and password"""

    result = await session.execute(select(User).where(User.email == form_data.username))
    user: Union[User, None] = result.scalars().first()

    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    if not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return security.generate_access_token_response(user.id)


@router.post("/registration", response_model=UserResponse)
async def registration(
    new_user: UserCreate,
    session: AsyncSession = Depends(deps.get_session),
):
    
    exists_user = await session.execute(
        select(User).where(User.email == new_user.email)
    )

    if exists_user.scalars().first() is not None:
        raise HTTPException(status_code=400, detail='ya existe un usuario con ese email')

    user = User(
        name=new_user.name,
        last_name=new_user.last_name,
        email=new_user.email,
        hashed_password=security.get_password_hash(new_user.password),
        nit=new_user.nit,
        contact=new_user.contact,
        address=new_user.address,
        is_parent=new_user.is_parent,
        is_health_professional=new_user.is_health_professional
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

@router.post("/kids-registration", status_code=200)
async def kids_registration(
    kids: List[KidCreate],
    user_id: int = Body(embed=True),
    session: AsyncSession = Depends(deps.get_session),
):
    
    exists_user = await session.execute(
        select(User).where(User.id == user_id)
    )

    if exists_user.scalars().first() is None:
        raise HTTPException(status_code=400, detail='El usuario no existe')

    kids_models = [Kid(**kid.dict(), user_id=user_id) for kid in kids]
    session.add_all(kids_models)
    await session.commit()
    return JSONResponse(content={'detail':'Niños registrados con éxito'})

