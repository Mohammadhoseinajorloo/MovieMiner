from extractor import MovieScraper
from core.config import setting
from db.action import ActionDB 
from apscheduler.schedulers.blocking import BlockingScheduler
from logger import LoggerDecorators, FileLogger, ConsolLogger
import jdatetime
import sqlite3


file_logger = FileLogger().get_logger()
consol_logger = ConsolLogger().get_logger()

# Function for scraping website
@LoggerDecorators.log_to_consol
def scraping_website(
        page: int
):
    url = f"{setting.FILM_URL}/page/{str(page)}/"

    try:
        consol_logger.info(f"Starting scraping page number {page} process...")
        moviextraction = MovieScraper(url)
        movies = moviextraction.scrape()
        consol_logger.info(f"Scraped page number {page}")
        return movies

    except Exception as e:
        file_logger.error(f"Error while scraping page {page}: {e}")
        raise


# Function for storaging information in database
@LoggerDecorators.log_to_consol
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
            file_logger.error(f"Database error on  movie {movie.filds['title']} : {e}")
            continue


# Starting scheduler for run all app
@LoggerDecorators.log_to_consol
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
        file_logger.error("End ...")


@LoggerDecorators.log_to_consol
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
                consol_logger.warning(f"There is no movie for today")
                file_logger.warning(f"There is no movie for today")
                break
            # strorge moive information in database
            Storage_info_in_db(movies)
            page += 1


if __name__ == "__main__":
    if setting.STATUS_PROJECT == "Production":
        main(schedule=True) # with schedule
    elif setting.STATUS_PROJECT == "Testing":
        main() # without schedule
