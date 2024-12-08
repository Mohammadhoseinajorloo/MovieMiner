from extraction.film import FilmExtract
import jdatetime
import sqlite3


FILM_URL = 'https://golchindls.ir/movie_cats/film/'
DATABASE_ADDRESS = "movies.db"


class DataBaseHandler:

    def __init__(self, db_address: str):
        try:
            self.connection = sqlite3.connect(db_address)
            self.cursor = self.connection.cursor()
            print(f"SQLITE Connection Established!!!")
        except sqlite3.Error as error:
            print(f"Error while connection to sqlite", error)

    def __exit__(self):
        return self.cursor.close()

    def create_table(self, tabel_name: str, columns: dict):
        columns = str(columns).replace(":", " ").replace("'", "").replace("{", "").replace("}", "")
        query = f""" CREATE TABLE IF NOT EXISTS {tabel_name} ({columns});"""
        return self.cursor.execute(query)
    


def main():
    columns_name = ["id", "firstname", "lastname"]
    columns_data_type = ["INTEGER", "VARCHAR", "VARCHAR"]
    columns = {key:value for (key,value) in zip(columns_name, columns_data_type)}
    tabel_name = "films"
    db = DataBaseHandler(DATABASE_ADDRESS)
    db.create_table(tabel_name, columns)
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
