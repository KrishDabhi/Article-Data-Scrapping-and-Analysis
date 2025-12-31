# scraper.py
import os
import requests
from bs4 import BeautifulSoup

def scrape_article(url: str, output_path: str) -> None:
    """Scrape visible text from URL and save to .txt file."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts, styles, navigation, footer, etc.
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        # Extract main content
        main_content = soup.find("article") or soup.find("main") or soup
        text = main_content.get_text(separator=" ", strip=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ Scraped: {os.path.basename(output_path)}")
    except Exception as e:
        print(f"❌ Failed to scrape {url}: {e}")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("")