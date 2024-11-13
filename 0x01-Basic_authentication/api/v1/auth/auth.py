#!/usr/bin/env python3
''' This function is used to generate the output'''
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
        if path is None:
            return True

        if not excluded_paths:
            return True

        path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += '/'
            if excluded_path.endswith("*"):
                if path.startswith(excluded_path[:-1]):
                    return False
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieve the authorization header from the request
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        else:
            return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current authenticated user from the request
        """
        return None
