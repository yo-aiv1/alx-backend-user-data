#!/usr/bin/env python3

"""
User class that creates databse tables
"""

from sqlalchemy import Column, Integer, String


class User():
    """
    User class
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=True)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
