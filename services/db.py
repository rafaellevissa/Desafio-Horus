import mysql.connector

class Database:
    def __init__(self):
        self.database = mysql.connector.connect(
            host='db',
            user='root',
            password='root',
            database='horus'
        )

    def connect(self) -> mysql.connector:
        return self.database.cursor()

    def commit(self) -> mysql:
        return self.database.commit()