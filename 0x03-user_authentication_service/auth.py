#!/usr/bin/env python3

""" Auth class for managing user's credentials """


import bcrypt


def _hash_password(password: str) -> str:
    """ Takes in a password and returns a salted hash.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
