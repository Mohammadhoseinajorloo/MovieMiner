from extraction.film import FilmExtract
from core.config import setting
from db.database_manager import DatabaseManager 

import jdatetime
import sqlite3


def main():
    page = 1
    db = DatabaseManager(setting.DATABASE_ADDRESS)
    while True:
        url = f"{setting.FILM_URL}page/{str(page)}/"
        moviextraction = FilmExtract(url)
        movies = moviextraction.scrape()
        if len(movies) == 0:
            break
        print(f"Scrape page number {page}")
        for index, movie in enumerate(movies):
            db.create_table("films", movie)
            db.insert("films", movie)
            print(f"Movie number {index+1}")
            print(movie)
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("_______________________________________________________________")
        page += 1

if __name__ == "__main__":
    main()
