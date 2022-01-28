from api.user import RequestUser
from essential import Essential

class user_name_informations_control(Essential):
    def __init__(self, username : str) -> None:
        self.username = username.lower().strip()
        self.user_informations = self.load_ui('user_informations')

    def get_user_information(self):
        self.user = RequestUser(self.username).get_user()
        if self.user.get('message') == 'Not Found':
            return 'User not found'
        elif self.user.get("documentation_url") == "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting":
            return 'You have exceeded the rate limit'
        else:
            self.user_informations.show()
            return self.user
            