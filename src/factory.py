from fastapi import FastAPI
from src.routers.github import github_router
from src.routers.health import health_router
from starlette.middleware.cors import CORSMiddleware

from config.settings import ServerConfig


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
        allow_origins=[str(origin) for origin in ServerConfig.CORS_ORIGINS],
    )
    app.include_router(health_router, prefix="/health")
    app.include_router(github_router, prefix="/webhook/github")

    return app
