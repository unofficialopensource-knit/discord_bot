from logging import Formatter
from logging import StreamHandler
from logging import getLogger
from os import getenv


DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")


def setup_logging():
    formatter = Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")

    handler = StreamHandler()
    handler.setFormatter(formatter)

    logger = getLogger("discord")
    logger.setLevel(getenv("LOG_LEVEL"))
    logger.addHandler(handler)
