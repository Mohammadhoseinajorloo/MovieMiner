from bs4 import BeautifulSoup
from logger import LoggerDecorators, consol_logger
import requests


class RequestHandler:
    """Handles HTTP requests with session and headers to avoid blocking."""

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    @LoggerDecorators.log_to_file
    def __init__(self):
        self.session = requests.Session()

    @LoggerDecorators.log_to_file
    def fetch_page(self, url: str) -> BeautifulSoup:
        """Fetches and parses HTML content from the given URL."""
        try:
            response = self.session.get(url, headers=self.HEADERS, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            consol_logger.error(f"Request failed: {e}")
            return None
