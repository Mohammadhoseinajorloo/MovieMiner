import sys
import os
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)

from article import Article
from logger import logger
from core.config import setting
from .query_generator import QueryGenerator
from logger import log_execution

import sqlite3
import mysql.connector


class DatabaseManager:

    @log_execution
    def __init__(self, status: str):
        self.querygenerator = QueryGenerator()
        try:
            # if project status test connection to sqlite database
            if status == "test":
                db_address = setting.DATABASE_ADDRESS
                self.connection = sqlite3.connect(db_address, check_same_thread=False)

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
                    self.connection = mysql.connector.connect(
                        user=user,
                        password=password,
                        host=host,
                        port=int(port),
                        database=database,
                        charset="utf8mb4",
                        use_unicode=True,
                    )
            else:
                logger.error("This status not exist in default project")


            self.cursor = self.connection.cursor()
            logger.info(f"{status} database Connection Established!!!")

        except mysql.connector.Error as error:
            logger.error(f"Error while connection to {status} database : {error}")


    @log_execution
    def __exit__(self):
        return self.cursor.close()


    @log_execution
    def _isexist(self, tabel_name: str, article: Article):
        isexist_query = self.querygenerator.isexist_query(self.connection, tabel_name, article)
        self.cursor.execute(isexist_query)
        awnser = self.cursor.fetchone()
        #print(awnser)
        if awnser is None:
            return False
        return True

    @log_execution
    def create_table(self, tabel_name: str, article: Article):
        create_table_query = self.querygenerator.create_table_query(self.connection, tabel_name, article)
        self.cursor.execute(create_table_query)


    @log_execution
    def insert(self, tabel_name: str, article: Article):
        if not self._isexist(tabel_name, article):
            insert_query = self.querygenerator.insert_query(self.connection, tabel_name, article)
            self.cursor.execute(insert_query, article.get_values())
            self.connection.commit()
        else:
            logger.warning(f"{article.filds["title"]} movie exist in database")
