from extraction.film import FilmExtract
import jdatetime
import sqlite3

FILM_URL = 'https://golchindls.ir/movie_cats/film/'
DATABASE_ADDRESS = "movies.db"


class DataBaseHandler:

    def __init__(self, db_address):
        try:
            self.connection = sqlite3.connect(db_address)
            self.cursor = self.connection.cursor()
            print(f"SQLITE Connection Established!!!")
            self.cursor.close()
        except sqlite3.Error as error:
            print(f"Error while connection to sqlite", error)
        finally:
            if (self.connection):
                self.connection.close()
                print("connection closed...")

    def create_table(self, tabel_name):
        pass
    


def main():
    db = DataBaseHandler(DATABASE_ADDRESS)
    """
    page = 0
    while True:
        url = FILM_URL+"page/"+str(page)+"/" 
        moviextraction = FilmExtract(url)
        movies = moviextraction.scrape()
        if len(movies) == 0:
            break
        print(f"Scrape page number {page}")
        for index, movie in enumerate(movies):
            print(f"Movie number {index}")
            print(movie)
        print("_______________________________________________________________")
        page += 1
    """

if __name__ == "__main__":
    main()
