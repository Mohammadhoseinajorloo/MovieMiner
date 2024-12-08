from extraction.film import FilmExtract
from core.config import setting

import jdatetime
import sqlite3


def main():
    page = 1 
    while True:
        url = setting.FILM_URL+"page/"+str(page)+"/" 
        moviextraction = FilmExtract(url)
        movies = moviextraction.scrape()
        if len(movies) == 0:
            break
        print(f"Scrape page number {page}")
        for index, movie in enumerate(movies):
            print(f"Movie number {index+1}")
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(movie)
        print("_______________________________________________________________")
        page += 1

if __name__ == "__main__":
    main()
