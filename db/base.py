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

    def create_table(self, tabel_name: str, columns: dict):
        columns = str(columns).replace(":", " ").replace("'", "").replace("{", "").replace("}", "")
        query = f""" CREATE TABLE IF NOT EXISTS {tabel_name} ({columns});"""
        return self.cursor.execute(query)
