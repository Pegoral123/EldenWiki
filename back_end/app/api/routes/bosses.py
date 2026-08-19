from fastapi import APIRouter, HTTPException

from app.services.boss_service import (
    get_all_bosses,
    get_caelid_bosses,
    get_limgrave_bosses,
)

router = APIRouter(prefix="/boss", tags=["Bosses"])


@router.get("/")
def get_bosses():
    data = get_all_bosses()
    if data is not None:
        return data
    raise HTTPException(status_code=500, detail="Erro ao buscar os dados dos bosses")  # noqa: E501


@router.get("/limgrave_bosses")
def get_limgrave_boss():
    bosses = get_limgrave_bosses()
    if not bosses:
        raise HTTPException(status_code=404, detail="Nenhum boss encontrado")
    return bosses


@router.get("/caelid_bosses")
def get_caelid_boss():
    bosses = get_caelid_bosses()
    return bosses