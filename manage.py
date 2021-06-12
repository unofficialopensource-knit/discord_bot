from config import settings
from src.client import GitHubClient


if __name__ == "__main__":
    settings.setup_logging()

    GitHubClient().run(settings.DISCORD_BOT_TOKEN)
