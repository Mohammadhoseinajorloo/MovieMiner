from logging.handlers import TimedRotatingFileHandler
from logging import (
    INFO,
    DEBUG,
    StreamHandler,
    Formatter,
    getLogger,
)
from .config import (
    LOGGER_NAME,
    LOGGING_FORMAT,
    LOGGING_TIME_FORMAT,
    LOG_FILE,
)


logger = getLogger(LOGGER_NAME)
logger.setLevel(INFO)
formatter = Formatter(LOGGING_FORMAT, LOGGING_TIME_FORMAT)

file_handler = TimedRotatingFileHandler(
    LOG_FILE,
    when="midnight",
    interval=30,
    backupCount=12,
)
file_handler.setLevel(DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
