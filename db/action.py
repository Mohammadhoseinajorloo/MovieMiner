import sys
import os
WORK_DIR = os.getcwd()
sys.path.append(WORK_DIR)


from article import Article
from logger import log_execution
from logger import logger
from .base import BaseDB
from .query import QueryGenerator


class ActionDB(BaseDB):
    """ All action in database """

    @log_execution
    def __init__(self, status: str):
        """ Initialize action database class """
        super().__init__(status)
        self.qg = QueryGenerator()


    @log_execution
    def _isexist(self, tabel_name: str, article: Article):
        """ Action is exist item in database """
        isexist_query = self.qg.isexist_query(self.con, tabel_name, article)
        self.cur.execute(isexist_query)
        awnser = self.cur.fetchone()
        #print(awnser)
        if awnser is None:
            return False
        return True


    @log_execution
    def create_table(self, tabel_name: str, article: Article):
        """ Action create table in database """
        create_table_query = self.qg.create_table_query(self.con, tabel_name, article)
        self.cur.execute(create_table_query)


    @log_execution
    def insert(self, tabel_name: str, article: Article):
        """ Action insert item in database """
        if not self._isexist(tabel_name, article):
            insert_query = self.qg.insert_query(self.con, tabel_name, article)
            self.cur.execute(insert_query, article.get_values())
            self.con.commit()
        else:
            logger.warning(f"{article.filds["title"]} movie exist in database")
