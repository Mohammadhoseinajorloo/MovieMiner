from extractor import MovieScraper
from core.config import setting
from db.action import ActionDB 
from apscheduler.schedulers.blocking import BlockingScheduler
import jdatetime
import sqlite3
from logger import (
    logger,
)

#BUG: Not run app after connected to database !!!!!

# Function for scraping website
def scraping_website(
        page: int
):
    url = f"{setting.FILM_URL}/page/{str(page)}/"

    try:
        logger.info(f"Starting scraping page number {page} process...")
        moviextraction = MovieScraper(url)
        movies = moviextraction.scrape()
        logger.info(f"Scraped page number {page}")
        return movies

    except Exception as e:
        logger.error(f"Error while scraping page {page}: {e}")
        raise


# Function for storaging information in database
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
            logger.info(f"Saveing {movie.filds['title']} movie in db")
        except Exception as e :
            logger.error(f"Database error on  movie {movie.filds['title']} : {e}")
            continue


# Starting scheduler for run all app
def start_scheduler(
        h_schedule: int,
        m_schedule: int
):
    scheduler = BlockingScheduler()
    scheduler.add_job(main, "cron", hour=h_schedule, minute=m_schedule)
    try:
        logger.info("Starting scheduler ....")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.error("End ...")


def main(schedule: bool=False):
    # This condition for test in docker
    if schedule:
        print('With schedule')
        start_scheduler(int(setting.HOUR_SCHEDUL), int(setting.MINUTE_SCHEDUL))

    else:
        print("Without schedule")
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
    if setting.STATUS_PROJECT == "product":
        main(schedule=True) # with schedule
    elif setting.STATUS_PROJECT == "test":
        main() # without schedule
