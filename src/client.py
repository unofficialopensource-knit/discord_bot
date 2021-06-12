from discord import Client


class GitHubClient(Client):
    """Client for GitHub related interactions"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
