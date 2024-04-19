from django.test import TestCase
from .customjwt import TokenService
import jwt

# Replace with your actual access token (avoid hardcoding sensitive data)
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNCwiZXhwIjoxNzEzNTUyODgxfQ.GJyhnujh4r7jEMukdMvDSveNu-E4_kTooWEze4SFao4"
refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNCwiZXhwIjoxNzE0MDcxMjgxfQ.tBWG-YUezcnnWylyroTF_BIsGKNDXKohXMfkgUbyvi8"
token_type = "bearer"


class TestTokenService(TestCase):

    def test_verify_token_valid(self):
        """Tests successful verification of a valid access token"""
        payload = TokenService.verify_token(access_token)
        self.assertIsNotNone(payload)  # Assert payload is not None

    def test_verify_token_invalid(self):
        """Tests unsuccessful verification of an invalid token"""
        invalid_token = "invalid_token_string"  # Example of an invalid token
        with self.assertRaises(jwt.exceptions.DecodeError):
            TokenService.verify_token(invalid_token)
