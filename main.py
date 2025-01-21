from extraction.film import FilmExtract
from core.config import setting
from db.database_manager import DatabaseManager 

import jdatetime
import sqlite3
import logging

from logging.handlers import TimedRotatingFileHandler
from logging import (
    INFO,
    DEBUG,
    StreamHandler,
    Formatter,
    getLogger,
)
from sys import (
    stdout,
)

LOGGING_FORMAT = '[%(levelname)s] %(asctime)s - (%(name)s/%(filename)s/%(funcName)s/%(lineno)d) - %(message)s'
LOGGING_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
today = jdatetime.date.today()
current_month = f"{today.year}-{today.month:02d}"
LOG_FILE = f'logs_{current_month}.log'
LOGGER_NAME = "DownloaderLogger"

logger = getLogger(LOGGER_NAME)
logger.setLevel(INFO)
formatter = Formatter(LOGGING_FORMAT, LOGGING_TIME_FORMAT)

file_handler = TimedRotatingFileHandler(
    LOG_FILE,
    when="midnight",
    interval=30,
    backupCount=12,
)
file_handler.setLevel(DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Function for scraping website
def scraping_website(
        page: int
):
    url = f"{setting.FILM_URL}/page/{str(page)}/"

    try:
        logger.info(f"Starting scraping page number {page} process...")
        moviextraction = FilmExtract(url)
        movies = moviextraction.scrape()
        logger.info(f"Scrape page number {page}")
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
            today = jdatetime.date.today()
            logger.warning(f"There is no movie for today({today})")
            break
        # strorge moive information in database
        Storage_info_in_db(movies)
        page += 1

if __name__ == "__main__":
    main()
