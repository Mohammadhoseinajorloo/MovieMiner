from article import Article

import sqlite3


class DataBaseHandler:

    def __init__(self, db_address: str):
        try:
            self.connection = sqlite3.connect(db_address)
            self.cursor = self.connection.cursor()
            print(f"SQLITE Connection Established!!!")

        except sqlite3.Error as error:
            print(f"Error while connection to sqlite", error)

    def __exit__(self):
        return self.cursor.close()

    def create_table(self, tabel_name: str, article: Article):
        fields = article.get_filds()
        placeholders = ", ".join(f"{field} TEXT" for field in fields)  
        create_table_query = f"CREATE TABLE IF NOT EXISTS {tabel_name} ({placeholders})"
        self.cursor.execute(create_table_query)

    def insert(self, tabel_name: str, article: Article):
        fields = article.get_filds()
        field_names = ", ".join(fields)
        value_placeholders = ", ".join("?" for _ in fields)
        insert_query = f"INSERT INTO {tabel_name} ({field_names}) VALUES ({value_placeholders})"
        self.cursor.execute(insert_query, article.get_values())
        self.connection.commit()
