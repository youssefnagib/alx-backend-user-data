#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication class for API endpoints
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if the current request requires authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current authenticated user from the request
        """
        return None
