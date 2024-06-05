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

        SessionId = uuid.uuid4()
        self.user_id_by_session_id[user_id] = str(SessionId)
        return str(SessionId)