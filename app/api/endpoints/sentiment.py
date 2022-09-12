from app.api import deps
from app.models.user import User
from fastapi import APIRouter, Body, HTTPException, Depends
from pysentimiento.analyzer import AnalyzerOutput, AnalyzerForSequenceClassification
from dependency_injector.wiring import Provide, inject
from app.containers import Container

router = APIRouter()

@router.post("/sentimiento/")
@inject
def obtener_sentimiento(
    *,
    current_user: User = Depends(deps.get_current_user),
    sentencia: str = Body(embed=True),
    analyzer: AnalyzerForSequenceClassification = Depends(Provide[Container.analizer])
    ):
    try:
        emotions: AnalyzerOutput = analyzer.predict(sentencia)
        return {"emocion": emotions.output, "probs": emotions.probas}
    except Exception:
        raise HTTPException(
            status_code=400,
            detail='No se pudo analizar el sentimiento'
        )