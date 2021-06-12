from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import settings


def create_app() -> FastAPI:
    """
    App factory for the fastapi app.
    The fastapi object is instantiated and configured inside this funciton,
    to provide a unified and better interface for testing and deploying.
    You don't need to call this function directly, rather pass this callable
    to the gunicorn process.
    """
    app = FastAPI(title="DiscordBot", redoc_url=None)

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=["*"],
        allow_methods=["*"],
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
    )

    return app
