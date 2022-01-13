from requests import get

class RequestUser():
    def __init__(self, username) -> None:
        self.username = username

    def get_user(self) -> dict:
        """
        Get user information from GitHub API.
        """
        response = get(f'https://api.github.com/users/{self.username}').json()

        if response.get('message') == 'Not Found': return {'message': 'Not Found'}
        return response

if __name__ == '__main__':
    user = RequestUser('JoaoEmanuell')
    #user = RequestUser('weiqwe32qie3213')
    print(user.get_user())