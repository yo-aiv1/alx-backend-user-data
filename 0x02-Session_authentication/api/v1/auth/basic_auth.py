#!/usr/bin/env python3


"""Basic Auth"""

from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


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

    def user_object_from_credentials(self, UserEmail: str,
                                     UserPwd: str) -> TypeVar('User'):
        """
        get user object
        """
        if UserEmail is None or not isinstance(UserEmail, str):
            return None
        if UserPwd is None or not isinstance(UserPwd, str):
            return None
        try:
            AuthUser = User.search({'email': UserEmail})
        except Exception:
            return None

        assert not len(AuthUser) > 1
        if len(AuthUser) == 0:
            return None

        AuthUser = AuthUser[0]
        if not AuthUser.is_valid_password(UserPwd):
            return None
        return AuthUser

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current authenticated user"""
        base64_credential = self.extract_base64_authorization_header(
            request.headers.get('Authorization'))
        credentials = self.decode_base64_authorization_header(
            base64_credential)
        email, password = self.extract_user_credentials(credentials)
        return self.user_object_from_credentials(UserEmail=email,
                                                 UserPwd=password)
