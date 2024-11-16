import requests
from bs4 import BeautifulSoup

def scrape_phones():
    """
    Scrapes phone data from the given website.
    Returns a list of dictionaries with title, price, and description.
    """
    url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch the URL: {url}")

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    # Extract product details
    items = soup.select(".thumbnail")
    for item in items:
        title = item.select_one(".title").text.strip()
        price = item.select_one(".price").text.strip()
        description = item.select_one(".description").text.strip()

        products.append({
            "title": title,
            "price": price,
            "description": description
        })

    return products

