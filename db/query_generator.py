import sys
import os
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)

from article import Article
from logger import log_execution
import sqlite3

class QueryGenerator:

    @log_execution
    def create_table_query(self, connection , tabel_name: str, article: Article):
        fields = article.get_filds()
        placeholders = ", ".join(f"`{field}` TEXT" for field in fields)
        if isinstance(connection, sqlite3.Connection):
            return f"CREATE TABLE IF NOT EXISTS `{tabel_name}` (id INTEGER PRIMARY KEY AUTOINCREMENT,{placeholders})"
        else:
            return f"CREATE TABLE IF NOT EXISTS `{tabel_name}` (id INT PRIMARY KEY AUTO_INCREMENT, {placeholders})"


    @log_execution
    def insert_query(self, connection , tabel_name: str, article: Article):
        fields = article.get_filds()
        field_names = ", ".join(fields)
        if isinstance(connection, sqlite3.Connection):
            value_placeholders = ", ".join("?" for _ in fields)
        else:
            value_placeholders = ", ".join("s%" for _ in fields)
        return f"INSERT INTO `{tabel_name}` (`{field_names}`) VALUES ({value_placeholders})"

