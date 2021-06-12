import logging

from discord import Client


class GitHubClient(Client):
    """Client for GitHub related interactions"""

    async def on_ready(self):
        logging.warn(f"Logged in as {self.user}")
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$test"):
            await message.channel.send("Hello, world!")
