from discord import Client


class GitHubClient(Client):
    """Client for GitHub related interactions"""

    async def on_message(self, message):
        """
        Event handler for on_message event.
        This is triggered whenever a message is sent ojn any channel in the server.
        """
        if message.author == self.user:
            return

        if message.content.startswith("$test"):
            await message.channel.send("Hello, world!")
