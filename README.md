# FastAPI Scraping Project

## Setup
1. Clone the repository.
2. Start the server: `uvicorn app.main:app --reload`.

## Usage
- `GET /scrape`: Initiates scraping and stores data in the database.
- `GET /data`: Retrieves the scraped data.

## Docker Setup
Build and run the Docker container:
```bash
docker build -t fastapi-scraper .
docker run -d -p 8000:8000 fastapi-scraper

###  Running the Application
Run the app locally with:
```bash
uvicorn app.main:app --reload
