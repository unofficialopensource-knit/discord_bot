from src.client import GitHubClient

from config.settings import Config


if __name__ == "__main__":
    Config.setup_logging()

    GitHubClient().run(Config.DISCORD_BOT_TOKEN)
