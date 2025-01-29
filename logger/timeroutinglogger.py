from logging.handlers import TimedRotatingFileHandler
from logging import (
    INFO,
    DEBUG,
    StreamHandler,
    Formatter,
    getLogger,
    Filter,
)
from .config import (
    LOGGER_NAME,
    LOGGING_FORMAT,
    LOGGING_TIME_FORMAT,
    LOG_FILE,
)
import re


class NoHTMLFilter(Filter):
    def filter (self, record):
        return not bool(re.search(r"<[a-z][\s\S]*>", record.getMessage()))


def create_logger(
        name,
        logger_format = None,
):
    logger = getLogger(name)
    logger.setLevel(INFO)
    formatter = Formatter(logger_format, LOGGING_TIME_FORMAT)

    file_handler = TimedRotatingFileHandler(
        LOG_FILE,
        when="midnight",
        interval=30,
        backupCount=12,
    )
    file_handler.setLevel(DEBUG)
    file_handler.setFormatter(formatter)

    logger.addFilter(NoHTMLFilter())
    logger.propgate = False
    logger.addHandler(file_handler)
    return logger


logger = create_logger(LOGGER_NAME, LOGGING_FORMAT)
