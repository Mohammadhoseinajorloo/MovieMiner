from functools import wraps
from .file_logger import FileLogger
from .consol_logger import ConsolLogger


class LoggerDecorators:
    """Encapsulates logging decorators in a class for better organization and reuse."""
    file_logger = FileLogger().get_logger()
    consol_logger = ConsolLogger().get_logger()

    @classmethod
    def log_to_consol(cls, func):
        """Decorator for logging user-friendly messages to console."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                cls.consol_logger.info(f"{func.__name__.replace('_', ' ').capitalize()} completed successfully.")
                return result
            except Exception as e:
                cls.consol_logger.error(f"An error occurred: {e}")
                raise
        return wrapper

    @classmethod
    def log_to_file(cls, func):
        """Decorator for logging function execution to file only."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            cls.file_logger.info(f"Executing function: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                cls.file_logger.info(f"Function {func.__name__} executed successfully.")
                return result
            except Exception as e:
                cls.file_logger.error(f"Error in function {func.__name__}: {e}")
                raise
        return wrapper
