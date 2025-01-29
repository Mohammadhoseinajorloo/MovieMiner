import jdatetime


LOGGING_FORMAT = '[%(levelname)s] %(asctime)s - (%(name)s/%(filename)s/%(funcName)s/%(lineno)d) - %(message)s'
LOGGING_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
today = jdatetime.date.today()
current_month = f"{today.year}-{today.month:02d}"
LOG_FILE = f'logger/logs/logs_{current_month}.log'
LOGGER_NAME = "DownloaderLogger"
