import os
from dotenv import load_dotenv

load_dotenv()

class Settting:
    FILM_URL = os.getenv('FILM_URL')
    DATABASE_ADDRESS = os.getenv('DATABASE_ADDRESS')
    DATABASE_TEST_ADDRESS = os.getenv('DATABASE_TEST_ADDRESS')
    STATUS_PROJECT = os.getenv('STATUS_PROJECT')
    RATE_CONDITION = os.getenv("RATE_CONDITION")
    HOUR_SCHEDUL = os.getenv("HOUR_SCHEDUL")
    MINUTE_SCHEDUL = os.getenv("MINUTE_SCHEDUL")

setting = Settting()
