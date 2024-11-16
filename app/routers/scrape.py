from fastapi import APIRouter
from scraper.scrape import scrape_phones
from database.models import save_to_db

router = APIRouter()

@router.get("/")
async def scrape():
    """
    Scrapes data and saves it to the database.
    """
    data = scrape_phones()
    save_to_db(data)
    return {"status": "Scraping completed and data saved!"}

