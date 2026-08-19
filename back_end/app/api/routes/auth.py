from fastapi import APIRouter, HTTPException, Request

from app.core.firebase import verify_id_token
from app.schemas.auth import LoginModel, RegisterModel
from app.services.auth_service import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(payload: RegisterModel):
    return auth_service.register(
        email=payload.email,
        password=payload.password,
        name=payload.name,
    )


@router.post("/login")
def login(payload: LoginModel):
    return auth_service.login(
        email=payload.email,
        password=payload.password,
    )


@router.post("/verify_token")
async def verify_token(request: Request):
    body = await request.json()
    id_token = body.get("idToken")
    if not id_token:
        raise HTTPException(status_code=400, detail="idToken ausente")
    try:
        decoded = verify_id_token(id_token)
        return {"uid": decoded.get("uid"), "email": decoded.get("email")}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e)) from e