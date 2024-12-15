import os
from dotenv import load_dotenv

load_dotenv()

class Settting:
    FILM_URL = os.getenv('FILM_URL')
    DATABASE_ADDRESS = os.getenv('DATABASE_ADDRESS')


setting = Settting()
