from fastapi import APIRouter

from app.services.location_service import (
    get_caelid,
    get_liurnia,
    get_limgrave,
)

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.get("/limgrave")
def limgrave():
    return get_limgrave()


@router.get("/liurnia")
def liurnia():
    return get_liurnia()


@router.get("/caelid")
def caelid():
    return get_caelid()