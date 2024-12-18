from .base import BaseExtract
from updatetime import UpdateTime

from bs4 import BeautifulSoup


class FilmExtract(BaseExtract):
    def extracte_page_link(self, soup: BeautifulSoup) -> str: 
        return soup.find("div", class_="titr rt").find("h2", class_="title right rt-18").find("a")["href"]

    def extracte_image(self, soup: BeautifulSoup) -> str: 
        return soup.find("a", class_="right rt-relative photo").find("img", class_="owl-lazy right pic rt-blur rt-10px")["data-src"]
     
    def extracte_title(self, soup: BeautifulSoup) -> str: 
        titles = soup.find("div", class_="titr rt").find("h2", class_="title right rt-18").text
        titles = titles.split(" ")[2:]
        for title in titles:
            if title.isdigit() and int(title) > 1900:
                titles.remove(title)
        return " ".join(titles)

    def extracte_rates(self, soup: BeautifulSoup) -> tuple[int, int, int]:
        imdb = float(soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find("div", class_="emtiazs left rt-absolute rt-15px").find("a", class_="ins rt-ddd rt").find("div", class_="rt").find("span", class_="val-imdb left rt-18 rt-bold rt-dana").text.split("/")[1])
        vote = float(soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find("div", class_="emtiazs left rt-absolute rt-15px").find("a", class_="ins rt-ddd rt").find("span", class_="val left rt-999 rt-bold rt-12").text.split(" ")[0].replace(",", ""))

        try:
            user_satisfaction = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find("div", class_="emtiazs left rt-absolute rt-15px").find("span", class_="val-imdb left rt-18 rt-bold rt-dana isx_green").text
            user_satisfaction = float(user_satisfaction.split('%')[0])
        except:
            user_satisfaction = None

        try:
            metacritic = int(soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find("div", class_="ins rt").find("div", class_="rt").find("span", class_="val-imdb left rt-18 rt-bold rt-dana").text)
        except:
            metacritic = None

        return imdb, vote, user_satisfaction, metacritic

    def extract_geners(self, soup: BeautifulSoup) -> list:
        geners_list = []
        geners_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[0]
        geners = geners_part.find("span", class_="value right rt-fff").find_all("a")
        for gener in geners:
            geners_list.append(gener.text)
        return "-".join(geners_list)

    def extract_year_realese(self, soup: BeautifulSoup) -> int:
        year_realese_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[1]
        year_realese = soup.find_all("span", class_="value right rt-fff")[1].find("a").text
        return int(year_realese)

    def extract_movie_time(self, soup: BeautifulSoup) -> str:
        try:
            movie_time_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[2]
            movie_time = movie_time_part.find("span", class_="value right rt-fff").text
            split_movie_time_list = movie_time.strip() .split(" ")
            houre = int(split_movie_time_list[0])
            minute = int(split_movie_time_list[3])
            movie_time = houre * 60 + minute
        except: 
            movie_time = None
        return movie_time
        
    def extract_quality(self, soup: BeautifulSoup) -> str:
        quality_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[3]
        quality = quality_part.find("span", class_="value right rt-fff").text
        return quality

    def extract_product(self, soup: BeautifulSoup) -> str:
        product_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[4]
        product = product_part.find("span", class_="value right rt-fff").text
        return product

    def extract_language(self, soup: BeautifulSoup) -> str:
        language_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[5]
        language = language_part.find("span", class_="value right rt-fff").text
        return language 

    def extract_director(self, soup: BeautifulSoup) -> str:
        director_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[6]
        director = director_part.find("span", class_="value right rt-fff").text
        return director 

    def extract_stars(self, soup: BeautifulSoup) -> str:
        stars_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[7]
        stars = stars_part.find("span", class_="value right rt-fff").text
        return stars

    def extract_update_time(self, soup: BeautifulSoup) -> UpdateTime:
        try:
            update_time_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[8]
            update_time = update_time_part.find("span", class_="value right rt-fff").text
            return UpdateTime(update_time)
        except:
            update_time_part = soup.find("ul", class_="info left rt-13 rt-relative rt-ddd").find_all("li", class_="rt")[7]
            update_time = update_time_part.find("span", class_="value right rt-fff").text
            return UpdateTime(update_time)

    def extract_discription(self, soup: BeautifulSoup) -> str:
        return soup.find("div", class_="text rt rt-ddd rt-13 rt-10px").find("p").text

    def extract_like(self, soup: BeautifulSoup) -> str:
        return int(soup.find("div", class_="like-dis").find("div", class_="mi-icons mi-like movie-like").find("span", class_="count").text)

    def extract_like(self, soup: BeautifulSoup) -> str:
        return int(soup.find("div", class_="like-dis").find("div", class_="mi-icons mi-like movie-like").find("span", class_="count").text)

    def extract_dislike(self, soup: BeautifulSoup) -> str:
        return int(soup.find("div", class_="mi-icons mi-dislike movie-dislike").find("span", class_="count").text)
