from extraction.film import FilmExtract
from core.config import setting
from db.database_manager import DatabaseManager 
from logger import logger
import sqlite3


# Function for scraping website
def scraping_website(
        page: int
):
    url = f"{setting.FILM_URL}/page/{str(page)}/"

    try:
        logger.info(f"Starting scraping page number {page} process...")
        moviextraction = FilmExtract(url)
        movies = moviextraction.scrape()
        logger.info(f"Scraped page number {page}")
        return movies

    except Exception as e:
        logger.error(f"Error while scraping page {page}: {e}")
        raise


# Function for storaging information in database
def Storage_info_in_db(
    movies: list,
    db: DatabaseManager = DatabaseManager(setting.DATABASE_ADDRESS),
):
    for movie in movies:
        try:
            db.create_table("films", movie)
            db.insert("films", movie)
            logger.info(f"Saveing {movie.filds['title']} movie in db")
        except Exception as e :
            logger.error(f"Database error on  movie {movie.filds['title']} : {e}")
            continue


def main():
    page = 1
    while True:
        # scrap website
        movies = scraping_website(page)
        # if empty movies list break app
        if not movies:
            logger.warning(f"There is no movie for today")
            break
        # strorge moive information in database
        Storage_info_in_db(movies)
        page += 1


if __name__ == "__main__":
    main()
