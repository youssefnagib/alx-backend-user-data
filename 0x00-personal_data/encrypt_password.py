#!/usr/bin/env python3
""" encryption """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hash a password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if the password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
