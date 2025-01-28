from .timeroutinglogger import logger
from functools import wraps
from time import time


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing function: {func.__name__}")
        logger.info(f"Arguments: args={args}, kwargs={kwargs}")
        start_time = time()
        try:
            result = func(*args, **kwargs)
            end_time = time()
            logger.info(f"Function {func.__name__} executed successfully in {end_time - start_time:.2f} seconds.")
            logger.info(f"Result: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in function {func.__name__}: {e}")
            raise
    return wrapper
