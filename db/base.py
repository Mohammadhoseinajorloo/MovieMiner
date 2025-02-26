import sys
import os
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)

from core.config import setting
from logger import log_execution
from logger import logger
import sqlite3
import mysql.connector


class BaseDB:
    """ Base connection in databse """

    @log_execution
    def __init__(self, status: str):
        """ Initialize connection in database """
        try:
            # if project status test connection to sqlite database
            if status == "test":
                db_address = setting.DATABASE_ADDRESS
                self.con = sqlite3.connect(db_address, check_same_thread=False)
                self.cur = self.con.cursor()

            # if project status product connection to mysql database
            elif status == "product":
                db_url = setting.DATABASE_ADDRESS
                db_info = db_url.split('://')[1].split('@')
                user_pass = db_info[0].split(':')
                user = user_pass[0]
                password = user_pass[1]
                host_port = db_info[1].split('/')
                host = host_port[0].split(':')[0]
                port = host_port[0].split(':')[1]
                database = host_port[1]
                self.con = mysql.connector.connect(
                    user=user,
                    password=password,
                    host=host,
                    port=int(port),
                    database=database,
                    charset="utf8mb4",
                    use_unicode=True,
                )
                self.cur = self.con.cursor(buffered=True)
            else:
                logger.error("This status not exist in default project")


            logger.info(f"{status} database Connection Established!!!")

        except mysql.connector.Error as error:
            logger.error(f"Error while connection to {status} database : {error}")


    @log_execution
    def __exit__(self):
        """ Exit database after end work with database """
        self.con.close()
