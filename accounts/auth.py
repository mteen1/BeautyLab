from ninja import Router
from django.contrib.auth import authenticate
from .customjwt import TokenService
from .schemas import AuthToken, LoginSchema

router = Router()


@router.post("token/", response=AuthToken)
def create_token(request, payload: LoginSchema):
    """generates a pair of access and refresh tokens"""
    user = authenticate(username=payload.username, password=payload.password)
    if not user:
        return router.api.create_response(request, {"detail": "Invalid credentials"})

    token = TokenService.create_token(user.id)
    return AuthToken(access_token=token, token_type="bearer")


@router.post("refresh/", response=AuthToken)
def refresh_token(request, payload: LoginSchema):
    """refreshes access token using a refresh token"""
    user = authenticate(username=payload.username, password=payload.password)
    if not user:
        return router.api.create_response(request, {"detail": "Invalid credentials"})

    refresh__token = request.body.get('refresh_token')
    if not refresh__token or not TokenService.verify_token(refresh__token, is_refresh=True):
        return router.api.create_response(request, {"detail": "Invalid refresh token"})

    token = TokenService.create_token(user.id)
    return AuthToken(access_token=token['access_token'], token_type="bearer")
