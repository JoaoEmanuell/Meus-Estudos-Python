from requests import get

class RequestLicense():
    def __init__(self, repo) -> None:
        self.repo = repo
    
    def get_license(self) -> dict:
        """
        Get license information from GitHub API.
        """
        response = get(self.repo['license']['url']).json()
        return response["html_url"]