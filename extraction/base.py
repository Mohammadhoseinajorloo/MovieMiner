import os
import sys
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)

from article import Article
from core.config import setting

from bs4 import BeautifulSoup
import requests
import datetime
import jdatetime


class BaseExtract:
    def __init__(self, url):
        self.url = url

    def parse_url (self, url: str) -> str:
        res = requests.get(url)
        return res.text

    def fetch_url(self, html: str) -> BeautifulSoup:
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def extract_articles(self, soup: BeautifulSoup) -> list:
        articels_post_box = soup.find("div", class_="rt-posts right is-archive list-mode")
        section_rt = articels_post_box.find("section", class_="rt") 
        div_rt = section_rt.find_all("div", class_="rt")[1]
        articels = div_rt.find_all("article")
        return articels

    def extract_info_articel(self, articels: list):
        articles_list = []
        today = datetime.datetime.now()
        shamsi_date = shamsi_date = jdatetime.date.fromgregorian(date=today)
        shamsi_day = shamsi_date.day
        for article in articels:
            update_time = self.extract_update_time(article)
            update_time_year = update_time.year
            update_time_month = update_time.month
            update_time_day = update_time.day
            imdb_rate, vote_rate, user_satisfaction_rate, metacritic_rate = self.extracte_rates(article)

            # condition imdb rate and update_time for limit films
            if (shamsi_day == update_time_day) and (imdb_rate > 7):
                page_link = self.extracte_page_link(article)
                title = self.extracte_title(article)
                image = self.extracte_image(article) 
                geners = self.extract_geners(article)
                year_realese = self.extract_year_realese(article)
                movie_time = self.extract_movie_time(article)
                quality = self.extract_quality(article)
                product = self.extract_product(article)
                language = self.extract_language(article)
                director = self.extract_director(article)
                stars = self.extract_stars(article)
                discription = self.extract_discription(article)
                like = self.extract_like(article)
                dislike = self.extract_dislike(article)
                article_obj = Article(
                        page_link=page_link,
                        title=title,
                        image=image,
                        imdb_rate=imdb_rate,
                        vote_rate=vote_rate,
                        user_satisfaction_rate=user_satisfaction_rate,
                        metacritic_rate=metacritic_rate,
                        geners=geners,
                        year_realese=year_realese,
                        movie_time=movie_time,
                        quality=quality,
                        product=product,
                        language=language,
                        director=director,
                        stars=stars,
                        update_time_year=update_time_year,
                        update_time_month=update_time_month,
                        update_time_day = update_time_day,
                        discription=discription,
                        like=like,
                        dislike=dislike
                        )

                articles_list.append(article_obj) 
            else:
                continue

        return articles_list

    def scrape(self):
        html = self.parse_url (self.url)
        soup = self.fetch_url(html)
        movies_list = self.extract_articles(soup)
        movies_info = self.extract_info_articel(movies_list)
        return movies_info
