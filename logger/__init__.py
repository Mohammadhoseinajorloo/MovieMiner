from .base_logger import BaseLogger
from .file_logger import FileLogger
from .consol_logger import ConsolLogger
from .decorators_logger import LoggerDecorators

__version__ = "1.0.0"

# Initialize loggers
file_logger = FileLogger().get_logger()
consol_logger = ConsolLogger().get_logger()

__all__ = ["BaseLogger", "FileLogger", "ConsoleLogger", "LoggerDecorators", "file_logger", "console_logger"]
