#!/usr/bin/env python3

"""Session Auth"""

from api.v1.auth.auth import Auth
import uuid


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
        """Create User's Session"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
