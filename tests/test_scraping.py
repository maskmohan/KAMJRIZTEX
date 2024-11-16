from scraper.scrape import scrape_and_save_data

def test_scraping():
    assert scrape_and_save_data() is None  # No errors
