from dataclasses import dataclass
from os import getenv


@dataclass
class ServerConfig:
    CORS_ORIGINS = getenv("CORS_ORIGINS", "*").split(",")
