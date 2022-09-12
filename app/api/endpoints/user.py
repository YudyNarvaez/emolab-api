from app.models.result import Result
from app.schemas.requests import AnalysisResult
from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.responses import UserResponse
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
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


@router.post("/save-result/", status_code=200)
async def save_result(
    *,
    session: AsyncSession = Depends(deps.get_session),
    current_user: User = Depends(deps.get_current_user),
    kid_id: int = Body(embed=True),
    text: str = Body(embed=True),
    analysis: AnalysisResult
    ):
    try:
        result = Result(kid_id=kid_id, text=text, analysis=analysis.dict())
        session.add(result)
        await session.commit()
        return JSONResponse(content={'detail':'Resultado guardado con éxito'})
    except Exception:
        raise HTTPException(
            status_code=400,
            detail='No se pudo guardar el resultado'
        )