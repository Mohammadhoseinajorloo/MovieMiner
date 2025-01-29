from functools import wraps
from time import time
import hashlib
from .timeroutinglogger import (
    logger,
    loggerboxing,
)


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        loggerboxing.info(f"***************** {func.__name__} *********************")
        logger.info(f"Executing function: {func.__name__}")
        logger.info(f"Arguments: args={args}, kwargs={kwargs}")
        start_time = time()
        try:
            result = func(*args, **kwargs)
            end_time = time()

            # Calculate hash result
            result_str = result.prettify() if hasattr(result, "prettify") else str(result)
            result_hash = hashlib.sha256(result_str.encode()).hexdigest()

            logger.info(f"Function {func.__name__} executed successfully in {end_time - start_time:.2f} seconds. result : {result_hash}")
            return result
        except Exception as e:
            logger.error(f"Error in function {func.__name__}: {e}")
            raise
    return wrapper
