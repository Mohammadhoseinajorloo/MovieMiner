from extraction.film import FilmExtract
import jdatetime

FILM_URL = 'https://golchindls.ir/movie_cats/film/'

def main():
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
    
if __name__ == "__main__":
    main()
