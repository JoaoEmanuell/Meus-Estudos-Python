from requests import get
from functools import lru_cache

class GetRepositorys():
    def __init__(self, user : dict) -> None:
        self.user = user

    @lru_cache
    def get_user_repos(self) -> dict: 
        return get(self.user['repos_url']).json()