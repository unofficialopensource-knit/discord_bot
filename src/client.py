from discord import Client


class GitHubClient(Client):
    """Client for GitHub related interactions"""

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$test"):
            await message.channel.send("Hello, world!")
