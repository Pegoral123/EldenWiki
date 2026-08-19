import requests
from fastapi import HTTPException

from app.core.config import settings
from app.core.firebase import create_user, init_firebase

init_firebase()


class AuthService:
    def __init__(self):
        self.api_key = settings.FIREBASE_API_KEY
        self.base_url = "https://identitytoolkit.googleapis.com/v1"

    def register(self, email: str, password: str, name: str):
        try:
            user = create_user(
                email=email,
                display_name=name,
                password=password,
            )
            login_url = (
                f"{self.base_url}/accounts:signInWithPassword"
                f"?key={self.api_key}"
            )
            login_body = {
                "email": email,
                "password": password,
                "returnSecureToken": True,
            }
            login_resp = requests.post(login_url, json=login_body, timeout=10)

            if login_resp.status_code != 200:
                raise HTTPException(status_code=401, detail=login_resp.json())

            token_data = login_resp.json()
            return {
                "uid": user.uid,
                "email": user.email,
                "name": user.display_name,
                "idToken": token_data.get("idToken"),
                "refreshToken": token_data.get("refreshToken"),
                "expiresIn": token_data.get("expiresIn"),
            }
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    def login(self, email: str, password: str):
        if not self.api_key:
            raise HTTPException(
                status_code=500,
                detail="FIREBASE_API_KEY não configurada",
            )
        url = (
            f"{self.base_url}/accounts:signInWithPassword?key={self.api_key}"
        )
        body = {
            "email": email,
            "password": password,
            "returnSecureToken": True,
        }
        resp = requests.post(url, json=body, timeout=10)
        if resp.status_code != 200:
            raise HTTPException(status_code=401, detail=resp.json())
        # Contem idToken, refreshToken, expiresIn e localId (uid).
        return resp.json()


auth_service = AuthService()