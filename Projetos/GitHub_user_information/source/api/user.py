from requests import get

class RequestUser():
    def __init__(self, username) -> None:
        self.username = username

    def get_user(self) -> dict:
        """
        Get user information from GitHub API.
        """
        return get(f'https://api.github.com/users/{self.username}').json()

if __name__ == '__main__':
    user = RequestUser('johndoe')
    print(user.get_user())