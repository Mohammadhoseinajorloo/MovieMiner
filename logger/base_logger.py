from threading import Lock
import jdatetime
import logging
import os
import json


class SingletonMeta(type):
    """A metaclass for Singleton implementation"""
    _instance = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                instance = super().__call__(*args, **kwargs)
                cls._instance[cls] = instance
        return cls._instance[cls]


class BaseLogger(metaclass=SingletonMeta):
    def __init__(self, log_level=logging.INFO):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(log_level)

    def get_logger(self):
        return self.logger

    def serialize(self):
        """Serialize logger configurtion to JSON"""
        return json.dumps({
            "name": self.logger.name,
            "level": logging.getLevelName(self.logger.level),
            "handlers": [handler.__class__.__name__ for handler in self.logger.handlers ]
        }, indent=4)
