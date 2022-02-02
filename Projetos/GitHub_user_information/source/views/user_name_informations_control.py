from source.api.user import RequestUser

class UserNameInformationsControl():
    def __init__(self, username : str) -> None:
        self.username = username.lower().strip()

    def get_user_information(self):
        self.user = RequestUser(self.username).get_user()
        if self.user.get('message') == 'Not Found':
            return 'User not found'
        elif self.user.get("documentation_url") == "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting":
            return 'You have exceeded the rate limit'
        else:
            return self.user
            