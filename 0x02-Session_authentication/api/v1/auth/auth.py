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
        if path is None or not excluded_paths:
            return True
        path2 = path[:]
        if path2[-1] != '/':
            path2 += '/'
        for path in excluded_paths:
            if path[-1] == '*':
                temp_path = path[:-1]
                if path2.startswith(temp_path):
                    return False
            else:
                if path == path2:
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
