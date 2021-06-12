from src.client import GitHubClient

from config import settings


if __name__ == "__main__":
    settings.setup_logging()

    GitHubClient().run(settings.DISCORD_BOT_TOKEN)
