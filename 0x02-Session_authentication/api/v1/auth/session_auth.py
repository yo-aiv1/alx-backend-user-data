#!/usr/bin/env python3

"""Session Auth"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session Auth Class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create User's Session"""
        if user_id is None or not isinstance(user_id, str):
            return None

        SessionId = str(uuid.uuid4())
        self.user_id_by_session_id[SessionId] = user_id
        return SessionId

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get User ID based on session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """get user instance"""
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user
