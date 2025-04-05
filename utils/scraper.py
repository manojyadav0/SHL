import requests
from bs4 import BeautifulSoup
import json

def scrape_shl_catalog(url="https://www.shl.com/solutions/products/product-catalog/"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", class_="product-tile")  # Adjust based on real class

    data = []
    for item in items:
        try:
            title = item.find("h3").text.strip()
            href = item.find("a")["href"]
            full_url = "https://www.shl.com" + href
            desc = item.find("p").text.strip() if item.find("p") else "No description"

            data.append({
                "name": title,
                "url": full_url,
                "description": desc,
                "remote_support": "Yes",  # Placeholder, update if available
                "adaptive_support": "Yes",
                "duration": "45 mins",
                "test_type": "Cognitive/Personality/Technical"  # Placeholder
            })
        except:
            continue

    with open("backend/shl_data.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    scrape_shl_catalog()
