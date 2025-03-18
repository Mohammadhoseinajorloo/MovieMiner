import sys
import os
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)

from core.config import setting
from logger import log_execution
from logger import logger
import sqlite3
import mysql.connector


class DBConnection:
    _instance = None # Singleton instance 
    db_address = setting.DATABASE_ADDRESS 

    @log_execution
    def __new__(cls, mode="Testing"):
        """Create a singleton database connection instance base on mode"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.mode = mode

            # if project status test connection to sqlite database
            if mode == "Testing":
                db_address = setting.DATABASE_ADDRESS
                cls._instance.connection = sqlite3.connect(db_address, check_same_thread=False)
                cls._instance.cursor = cls._instance.connection.cursor()
                print("Connected to SQLite (Test Mode)")

            # if project status product connection to mysql database
            elif mode == "Production":
                user, password, host, port, database = cls.return_info_from_address(cls.db_address)
                cls._instance.connection = mysql.connector.connect(
                    user=user,
                    password=password,
                    host=host,
                    port=int(port),
                    database=database,
                    charset="utf8mb4",
                    use_unicode=True,
                )
                cls._instance.cursor = cls._instance.connection.cursor(buffered=True)
                print("Conneced to MySQL (Production Mode)")

            # if not test or product mode return error log in log file
            else:
                logger.error("Invalid mode! Choose either 'Testing' or 'Production")
                raise ValueError("Invalid mode!")

        return cls._instance


    @log_execution
    def return_info_from_address(db_address):
        db_info = db_address.split('://')[1].split('@')
        user_pass = db_info[0].split(':')
        user = user_pass[0]
        password = user_pass[1]
        host_port = db_info[1].split('/')
        host = host_port[0].split(':')[0]
        port = host_port[0].split(':')[1]
        database = host_port[1]
        return user, password, host, port, database


    @log_execution
    def __exit__(self):
        """ Exit database after end work with database """
        if self.connection:
            self.connection.close()
            DBConnection._instance = None
            print("Database connection closed.")
