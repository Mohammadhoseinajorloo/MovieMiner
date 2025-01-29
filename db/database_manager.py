import sys
import os
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)
from article import Article
from logger import logger
from core.config import setting

#import sqlite3
import mysql.connector


class DatabaseManager:

    def __init__(
            self
    ):
        try:
            db_url = setting.DATABASE_ADDRESS
            db_info = db_url.split('://')[1].split('@')
            user_pass = db_info[0].split(':')
            user = user_pass[0]
            password = user_pass[1]
            host_port = db_info[1].split('/')
            host = host_port[0].split(':')[0]
            port = host_port[0].split(':')[1]
            database = host_port[1]
            #self.connection = sqlite3.connect(db_address)
            self.connection = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                port=int(port),
                database=database
            )
            self.cursor = self.connection.cursor()
            logger.info(f"MySQL Connection Established!!!")

        except mysql.connector.Error as error:
            logger.error(f"Error while connection to mysql: {error}")

    def __exit__(self):
        return self.cursor.close()

    def create_table(self, tabel_name: str, article: Article):
        fields = article.get_filds()
        placeholders = ", ".join(f"{field} TEXT" for field in fields)  
        create_table_query = f"CREATE TABLE IF NOT EXISTS {tabel_name} (id INTEGER PRIMARY KEY AUTOINCREMENT,{placeholders})"
        self.cursor.execute(create_table_query)

    def insert(self, tabel_name: str, article: Article):
        fields = article.get_filds()
        field_names = ", ".join(fields)
        value_placeholders = ", ".join("?" for _ in fields)
        insert_query = f"INSERT INTO {tabel_name} ({field_names}) VALUES ({value_placeholders})"
        self.cursor.execute(insert_query, article.get_values())
        self.connection.commit()
