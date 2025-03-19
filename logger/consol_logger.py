from .base_logger import BaseLogger
from rich.console import Console
from rich.logging import RichHandler
import logging


class ConsolLogger(BaseLogger):
    def __init__(self, log_level=logging.INFO):
        if not hasattr(self, "initialized"):  # Prevent re-initialization
            super().__init__(log_level)
            console = Console()
            console_handler = RichHandler(console=console, show_time=True, show_level=True, rich_tracebacks=True)
            console_handler.setLevel(log_level)
            self.logger.addHandler(console_handler)
            self.initialized = True  # Mark as initialized


consol_logger = ConsolLogger().get_logger()
