from logging.handlers import TimedRotatingFileHandler
from .base_logger import BaseLogger
import logging
import os


class FileLogger(BaseLogger):

    LOG_FILE = "logger/logs/app.log"

    def __init__(self, log_file=LOG_FILE, log_level=logging.ERROR):
        if not hasattr(self, "initialized"):
            super().__init__(log_level)
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=30)
            file_handler.setLevel(log_level)
            file_handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s"))
            self.logger.addHandler(file_handler)
            self.initialized = True


'''
LOGGING_FORMAT = '[%(levelname)s] %(asctime)s - (%(name)s/%(filename)s/%(funcName)s/%(lineno)d) - %(message)s'
LOGGING_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
today = jdatetime.date.today()
current_month = f"{today.year}-{today.month:02d}"
if not os.path.isdir("logger/logs"):
    os.mkdir("logger/logs")
LOG_FILE = f'logger/logs/logs_{current_month}.log'
LOGGER_NAME = "DownloaderLogger"
'''
