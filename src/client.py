from discord import Client


class GitHubClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
