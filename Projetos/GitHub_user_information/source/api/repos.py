from requests import get
from functools import lru_cache

class RequestRepositories():
    def __init__(self, user : dict) -> None:
        self.user = user

    @lru_cache
    def get_user_repos(self): 
        repos = get(self.user['repos_url']).json()
        if len(repos) == 0:
            return 'The desired profile has no accessible repositories!'
        else :
            return repos