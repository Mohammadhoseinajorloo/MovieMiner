from abc import ABC, abstractmethod
from extractor import MovieScraper
from core.config import setting
from db.action import ActionDB
from apscheduler.schedulers.blocking import BlockingScheduler
from logger import LoggerDecorators, file_logger, consol_logger
import jdatetime
import sqlite3


# Abstract Scraper Strategy
class ScraperStrategy(ABC):
    @abstractmethod
    def scrap(self, page:int):
        pass


# Concrete Scraper
class MovieScraperStrategy(ScraperStrategy):

    def scrap(self, page:int):
        url = f"{setting.FILM_URL}/page/{str(page)}/"

        while True:
            try:
                consol_logger.info(f"Starting page {page}")
                scraper = MovieScraper(url)
                movies = scraper.scrape()
                consol_logger.info(f"Successfully scraped page {page}.")
                return movies
            except Exception as e:
                consol_logger.error(f"Error while scraping page {page}: {e}")
                return []


# Function for storaging information in database
@LoggerDecorators.log_to_file
def Storage_info_in_db(
    movies: list,
    db: ActionDB = ActionDB (
        mode =setting.STATUS_PROJECT,
    ),
):
    for movie in movies:
        try:
            db.create_table("films", movie)
            db.insert("films", movie)
            consol_logger.info(f"Saveing {movie.filds['title']} movie in db")
        except Exception as e :
            consol_logger.error(f"Database error on  movie {movie.filds['title']} : {e}")
            continue


# Starting scheduler for run all app
@LoggerDecorators.log_to_file
def start_scheduler(
        h_schedule: int,
        m_schedule: int
):
    scheduler = BlockingScheduler()
    scheduler.add_job(main, "cron", hour=h_schedule, minute=m_schedule)
    try:
        consol_logger.info("Starting scheduler ....")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        consol_logger.error("End ...")


@LoggerDecorators.log_to_file
def main(schedule: bool=False):
    # This condition for test in docker
    if schedule:
        consol_logger.info('With schedule')
        start_scheduler(int(setting.HOUR_SCHEDUL), int(setting.MINUTE_SCHEDUL))

    else:
        consol_logger.info("Without schedule")
        page = 1
        while True:
            # scrap website
            scraper = MovieScraperStrategy()
            movies = scraper.scrap(page)
            # if empty movies list break app
            if not movies:
                consol_logger.warning(f"There is no movie for today")
                break
            # strorge moive information in database
            Storage_info_in_db(movies)
            page += 1


if __name__ == "__main__":
    if setting.STATUS_PROJECT == "Production":
        main(schedule=True) # with schedule
    elif setting.STATUS_PROJECT == "Testing":
        main() # without schedule
