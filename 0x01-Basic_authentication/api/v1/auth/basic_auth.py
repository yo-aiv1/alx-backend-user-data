#!/usr/bin/env python3


"""Basic Auth"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(self, AuthHeader: str) -> str:
        IsString = isinstance(AuthHeader, str)
        if AuthHeader is None or not IsString or AuthHeader[:6] != "Basic ":
            return None
        return AuthHeader[6:]
