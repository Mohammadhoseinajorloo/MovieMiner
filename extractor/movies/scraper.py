from ..httprequest import RequestHandler
from ..article import Article
from .detils import MovieDetailsExtractor
from core.config import setting
from logger import LoggerDecorators
import datetime
import jdatetime


class MovieScraper:
    """Main class to handle movie extraction process."""

    @LoggerDecorators.log_to_file
    def __init__(self, url):
        self.url = url
        self.request_handler = RequestHandler()


    @LoggerDecorators.log_to_file
    def scrape(self):
        soup = self.request_handler.fetch_page(self.url)
        if not soup:
            return []

        articles = soup.select("div.rt-posts section.rt div.rt article")
        movies = []

        today = datetime.datetime.now()
        shamsi_date = jdatetime.date.fromgregorian(date=today)
        shamsi_day = shamsi_date.day

        for article in articles:
            movie_data = MovieDetailsExtractor.extract_movie_details(article)
            updatetime = MovieDetailsExtractor.extract_update_time(article)
            imdb_rate, vote_rate, user_satisfaction_rate, metacritic_rate = MovieDetailsExtractor.extract_rates(article)

            #if shamsi_day == int(updatetime.day) and imdb_rate >= int(setting.RATE_CONDITION):
            if shamsi_day - 1 == int(updatetime.day) and imdb_rate >= int(setting.RATE_CONDITION):
                movie = Article(
                    page_link=MovieDetailsExtractor.extract_page_link(article),
                    title=MovieDetailsExtractor.extract_title(article),
                    image=MovieDetailsExtractor.extract_image(article),
                    description=MovieDetailsExtractor.extract_description(article),
                    like=MovieDetailsExtractor.extract_like(article),
                    dislike=MovieDetailsExtractor.extract_dislike(article),
                    imdb_rate=imdb_rate,
                    vote_rate=vote_rate,
                    user_satisfaction_rate=user_satisfaction_rate,
                    metacritic_rate=metacritic_rate,
                    geners=movie_data["genres"],
                    year_realese=int(movie_data["release_year"]),
                    movie_time=movie_data["runtime"],
                    quality=movie_data["quality"],
                    product=movie_data["product"],
                    language=movie_data["language"],
                    director=movie_data["director"],
                    stars=movie_data["stars"],
                    update_year=updatetime.year,
                    update_month=updatetime.month,
                    update_day=updatetime.day,
                )
                movies.append(movie)

        return movies
