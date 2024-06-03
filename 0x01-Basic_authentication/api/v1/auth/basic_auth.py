#!/usr/bin/env python3


"""Basic Auth"""

from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(self, AuthHeader: str) -> str:
        """
        Extract Base64 part of the Authorization header
        """
        IsString = isinstance(AuthHeader, str)
        if AuthHeader is None or not IsString or AuthHeader[:6] != "Basic ":
            return None
        return AuthHeader[6:]

    def decode_base64_authorization_header(self, Base64AuthData: str) -> str:
        """
        decode base64 part of the Authorization header
        """
        if Base64AuthData is None or not isinstance(Base64AuthData, str):
            return None

        try:
            return base64.b64decode(Base64AuthData).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self, Base64AuthData: str) -> Tuple[str, str]:
        """
        extract user credentials
        """
        if Base64AuthData is None or not isinstance(Base64AuthData, str):
            return None, None
        Data = Base64AuthData.split(":")
        if len(Data) != 2:
            return None, None

        return tuple(Data)
