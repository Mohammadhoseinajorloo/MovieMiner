from bs4 import BeautifulSoup
import requests


class RequestHandler:
    """Handles HTTP requests with session and headers to avoid blocking."""

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    def __init__(self):
        self.session = requests.Session()

    def fetch_page(self, url: str) -> BeautifulSoup:
        """Fetches and parses HTML content from the given URL."""
        try:
            response = self.session.get(url, headers=self.HEADERS, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None
