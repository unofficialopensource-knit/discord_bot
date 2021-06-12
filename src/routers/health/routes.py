from typing import Dict

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def health_check() -> Dict[str, str]:
    """Health check route to see if the server is up and healthy"""
    return {"status": "ok"}
