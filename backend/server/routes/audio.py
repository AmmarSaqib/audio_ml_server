"""
main routes file
"""


from typing import Optional
from fastapi import APIRouter

router = APIRouter(prefix="/audio", tags=["audio"])


@router.get("/")
def read_root():
    """
    Testing this shit
    """
    return {"Hello": "World"}
