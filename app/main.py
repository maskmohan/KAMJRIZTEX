from fastapi import FastAPI
from app.routers import scrape, data

app = FastAPI()

# Include routers
app.include_router(scrape.router, prefix="/scrape", tags=["Scraping"])
app.include_router(data.router, prefix="/data", tags=["Data Retrieval"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI scraping application!"}

