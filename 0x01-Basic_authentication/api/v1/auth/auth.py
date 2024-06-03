#!/usr/bin/env python3
""" Module of Authentication """

from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth function
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header function
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user function
        """
        return None
