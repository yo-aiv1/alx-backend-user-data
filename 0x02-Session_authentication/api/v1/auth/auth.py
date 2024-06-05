#!/usr/bin/env python3
""" Module of Authentication """

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, ExcludedPaths: List[str]) -> bool:
        """
        require auth function
        """
        if path is not None and not path.endswith("/"):
            path = path + '/'

        if path is None or ExcludedPaths is None or path not in ExcludedPaths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header function
        """
        if request is None or "Authorization" not in request.headers:
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user function
        """
        return None

    def session_cookie(self, request=None) -> str:
        """get cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
