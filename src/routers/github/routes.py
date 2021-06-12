from typing import Dict

from fastapi import APIRouter


router = APIRouter()


@router.post("/")
async def webhook() -> Dict[str, str]:
    """WebHook for GitHub endpoint"""
    return {"status": "ok"}
