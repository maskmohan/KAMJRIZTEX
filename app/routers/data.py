from fastapi import APIRouter
from database.models import fetch_latest_data

router = APIRouter()

@router.get("/")
async def get_data():
    """
    Fetches and returns the latest data from the database.
    """
    data = fetch_latest_data()
    return {"data": [item.__dict__ for item in data]}

