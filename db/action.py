import sys
import os
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)


from extractor.article import Article
from .base import DBConnection 
from .query import QueryGenerator
from logger import LoggerDecorators, consol_logger


class ActionDB(DBConnection):
    """ All action in database """

    def __init__(self, mode: str):
        """ Initialize action database class """
        DBConnection.__new__(self, mode)
        self.qg = QueryGenerator()


    @LoggerDecorators.log_to_file
    def _isexist(self, tabel_name: str, article: Article):
        """ Action is exist item in database """
        isexist_query = self.qg.isexist_query(self.connection, tabel_name, article)
        self.cursor.execute(isexist_query)
        awnser = self.cursor.fetchone()
        if awnser is None:
            return False
        return True


    @LoggerDecorators.log_to_file
    def _update(self, tabel_name:str, article: Article):
        """ Update row data in database """
        update_query = self.qg.update_query(self.connection, tabel_name, article)
        self.cursor.execute(update_query, article.get_values())
        self.connection.commit()


    @LoggerDecorators.log_to_file
    def create_table(self, tabel_name: str, article: Article):
        """ Action create table in database """
        create_table_query = self.qg.create_table_query(self.connection, tabel_name, article)
        self.cursor.execute(create_table_query)


    @LoggerDecorators.log_to_file
    def insert(self, tabel_name: str, article: Article):
        """ Action insert item in database """
        if not self._isexist(tabel_name, article):
            insert_query = self.qg.insert_query(self.connection, tabel_name, article)
            self.cursor.execute(insert_query, article.get_values())
            self.connection.commit()
        else:
            self._update(tabel_name, article)
            consol_logger.warning(f"{article.filds['title']} movie exist in database")
