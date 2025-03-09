from bs4 import BeautifulSoup
from logger import log_execution
from core.config import setting
from ..article import Article
from ..updatetime import UpdateTime
import jdatetime


class MovieDetailsExtractor:
    """Extracts movie details from a BeautifulSoup object."""

    @staticmethod
    @log_execution
    def extract_page_link(soup: BeautifulSoup) -> str:
        return soup.select_one("div.titr h2.title a")["href"]


    @staticmethod
    @log_execution
    def extract_image(soup: BeautifulSoup) -> str:
        return soup.select_one("a.photo img.owl-lazy")["data-src"]


    @staticmethod
    @log_execution
    def extract_title(soup: BeautifulSoup) -> str:
        raw_title = soup.select_one("div.titr h2.title").text
        title_parts = raw_title.split(" ")[2:]
        return " ".join([word for word in title_parts if not word.isdigit()])


    @staticmethod
    @log_execution
    def extract_rates(soup: BeautifulSoup) -> tuple:
        """Extracts IMDb rating, vote count, user satisfaction, and Metacritic score."""
        try:
            imdb_tag = soup.select_one("span.val-imdb")
            imdb = float(imdb_tag.text.split("/")[1]) if imdb_tag else 0.0  # Default IMDb rating to 0.0 if missing
        except:
            imdb = 0.0

        try:
            vote_tag = soup.select_one("span.val")
            vote = int(vote_tag.text.replace("," , "").split(" ")[0]) if vote_tag else 0  # Default votes to 0 if missing
        except:
            vote = 0

        try:
            user_satisfaction_tag = soup.select_one("span.isx_green")
            user_satisfaction = float(user_satisfaction_tag.text.strip("%")) if user_satisfaction_tag else 0
        except:
            user_satisfaction = 0

        try:
            metacritic_tag = soup.select("div.rt span.val-imdb")
            metacritic = int(metacritic_tag[1].text) if len(metacritic_tag) > 2 else 0 # Ensure correct selection for Metacritic
        except:
            metacritic = 0

        return imdb, vote, user_satisfaction, metacritic


    @staticmethod
    @log_execution
    def extract_movie_details(soup: BeautifulSoup) -> dict:
        details = {}
        info_blocks = soup.select("ul.info li.rt")
        keys = ["genres", "release_year", "runtime", "quality", "product", "language", "director", "stars"]

        for key, block in zip(keys, info_blocks):
            details[key] = block.select_one("span.value").text if block else None

        return details


    @staticmethod
    @log_execution
    def extract_update_time(soup: BeautifulSoup) -> str:
        """Extracts the last update time of the movie."""
        try:
            info_blocks = soup.select("ul.info li.rt")
            update_time_part = info_blocks[-1].select_one("span.value").text
            return UpdateTime(update_time_part)
        except (AttributeError, IndexError):
            return None


    @staticmethod
    @log_execution
    def extract_description(soup: BeautifulSoup) -> str:
        """Extracts the movie description."""
        try:
            return soup.select_one("div.text.rt p").text
        except AttributeError:
            return "No description available."


    @staticmethod
    @log_execution
    def extract_like(soup: BeautifulSoup) -> int:
        """Extracts the number of likes."""
        try:
            return int(soup.select_one("div.like-dis div.mi-like span.count").text)
        except (AttributeError, ValueError):
            return 0


    @staticmethod
    @log_execution
    def extract_dislike(soup: BeautifulSoup) -> int:
        """Extracts the number of dislikes."""
        try:
            return int(soup.select_one("div.mi-dislike span.count").text)
        except (AttributeError, ValueError):
            return 0
