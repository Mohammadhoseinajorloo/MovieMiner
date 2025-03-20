from logging.handlers import TimedRotatingFileHandler
from .base_logger import BaseLogger
import jdatetime
import logging
import os


class FileLogger(BaseLogger):


    def __init__(self, log_level=logging.DEBUG):
        if not hasattr(self, "initialized"):
            super().__init__(log_level)
            log_file = self.calculate_log_file()
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=30)
            file_handler.setLevel(log_level)
            file_handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s"))
            self.logger.addHandler(file_handler)
            self.initialized = True


    def calculate_log_file(self):
       today = jdatetime.date.today()
       log_format = ".log"
       log_location = "logger/logs" 
       current_month = f"logs_{today.year}-{today.month:02d}"
       log_file = f"{log_location}/{current_month}{log_format}"
       return log_file


file_logger = FileLogger().get_logger()
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
