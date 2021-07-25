from typing import Dict

from fastapi import APIRouter


router = APIRouter()


@router.post("/")
async def webhook() -> Dict[str, str]:
    """Webhook for GitHub endpoint"""
    return {"status": "ok"}
