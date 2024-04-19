from datetime import datetime, timedelta
from django.conf import settings
from django.http import HttpRequest
import jwt
from ninja.security import HttpBearer
from .models import CustomUser


class TokenService:
    """contains methods for creating & verifying tokens"""
    @staticmethod
    def create_access_token(user_id: int):
        payload = {"user_id": user_id, "exp": datetime.utcnow() + timedelta(hours=24)}
        token = jwt.encode(payload, settings.ACCESS_TOKEN_SECRET_KEY, algorithm="HS256")
        return token

    @staticmethod
    def create_refresh_token(user_id: int):
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(days=7),
        }  # Set longer expiration for refresh token
        refresh_token = jwt.encode(
            payload, settings.REFRESH_TOKEN_SECRET_KEY, algorithm="HS256"
        )
        return refresh_token

    @staticmethod
    def create_token(user_id: int):
        access_token = TokenService.create_access_token(user_id)
        refresh_token = TokenService.create_refresh_token(user_id)
        return {"access_token": access_token, "refresh_token": refresh_token}

    @staticmethod
    def verify_token(token: str, is_refresh=False) -> dict | None:
        """Verifies the tokens according to the flag"""
        secret_key = (
            settings.ACCESS_TOKEN_SECRET_KEY
            if not is_refresh
            else settings.REFRESH_TOKEN_SECRET_KEY
        )
        print(f"verifying the token  {token}")
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256",])
            return payload
        except jwt.exceptions.ExpiredSignatureError:
            return None


class JWTAuth(HttpBearer):
    """a https bearer subclass to use with api endpoints authentication"""  
    # TODO: understand some of the layers

    def authenticate(self, request: HttpRequest, token: str):
        payload = TokenService.verify_token(token)
        if payload:
            user_id = payload.get("user_id")
            try:
                return CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                return None
        return None
