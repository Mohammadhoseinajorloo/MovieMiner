class Article:

    def __init__(
            self,
            page_link,
            title,
            image,
            imdb_rate,
            vote_rate,
            user_satisfaction_rate,
            metacritic_rate,
            geners,
            year_realese,
            movie_time,
            quality,
            product,
            language,
            director,
            stars,
            update_time, 
            discription, 
            like, 
            dislike
            ):
        
       self.page_link = page_link
       self.title = title
       self.image = image
       self.imdb_rate = imdb_rate
       self.vote_rate = vote_rate
       self.user_satisfaction_rate = user_satisfaction_rate
       self.metacritic_rate = metacritic_rate
       self.geners = geners
       self.year_realese = year_realese
       self.movie_time = movie_time
       self.quality = quality
       self.product = product
       self.language = language
       self.director = director
       self.stars = stars
       self.update_time = update_time
       self.discription = discription 
       self.like = like
       self.dislike = dislike

    def __str__(self):
        string = ""
        string += f"Page_Link: {self.page_link}\n"
        string += f"Tite: {self.title}\n"
        string += f"Image: {self.image}\n"
        string += f"Imdb: {self.imdb_rate}\n"
        string += f"Vote: {self.vote_rate}\n"
        string += f"User_satisfaction: {self.user_satisfaction_rate}\n"
        string += f"Metacritic: {self.metacritic_rate}\n"
        string += f"Gener: {self.geners}\n"
        string += f"Year_realese: {self.year_realese}\n"
        string += f"Movie_time: {self.movie_time}\n"
        string += f"Quality: {self.quality}\n"
        string += f"Product: {self.product}\n"
        string += f"Language: {self.language}\n"
        string += f"Director: {self.director}\n"
        string += f"Stars: {self.stars}\n"
        string += f"Update_time: {self.update_time.year}/{self.update_time.month}/{self.update_time.day}\n"
        string += f"Discription: {self.discription}\n"
        string += f"Like: {self.like}\n"
        string += f"Dislike: {self.dislike}\n"
        string += "###################################################"
        return string
