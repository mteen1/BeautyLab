import jwt.exceptions
from ninja import Router, Body
from django.contrib.auth import authenticate
from .customjwt import TokenService
from .schemas import AuthToken, LoginSchema
import jwt

router = Router()


@router.post("token/", response=AuthToken)
def create_token(request, payload: LoginSchema):
    """generates a pair of access and refresh tokens"""
    user = authenticate(username=payload.username, password=payload.password)
    if not user:
        return router.api.create_response(request, {"detail": "Invalid credentials"})

    token_data = TokenService.create_token(user.id)  # Get the dictionary
    access_token = token_data["access_token"]  # Extract the access token string
    refresh_token = token_data["refresh_token"]
    return AuthToken(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )


@router.post("refresh/", response=AuthToken)
def refreshes_token(request, body: Body[dict] ):
    """refreshes access token using a refresh token"""

    refresh_token = body.get("refresh_token")

    try:
        if not refresh_token or not TokenService.verify_token(
            refresh_token, is_refresh=True
        ):
            return router.api.create_response(request, data={"detail": "Invalid refresh token"},status=401)
    except jwt.exceptions.DecodeError:
        return router.api.create_response(request, data={"detail": "Invalid refresh token"},status=401)
    # No need to call authenticate since refresh token verifies identity
    user_id = request.user.id
    access_token = TokenService.create_access_token(user_id=user_id) 

    # Return the new refresh token (optional)

    return AuthToken(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
