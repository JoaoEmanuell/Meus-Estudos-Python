from requests import get
from functools import lru_cache

class RequestUser():
    def __init__(self, username) -> None:
        self.username = username
    
    @lru_cache
    def get_user(self) -> dict:
        """
        Get user information from GitHub API.
        """
        response = get(f'https://api.github.com/users/{self.username}').json()

        if response.get('message') == 'Not Found': return {'message': 'Not Found'}
        return response