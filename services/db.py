import mysql.connector

class Database:
    def __init__(self):
        self.database = mysql.connector.connect(
            host='localhost',
            user='root',
            password='SynysterGates1',
            database='horus'
        )

    def connect(self) -> mysql.connector:
        return self.database.cursor()

    def disconnect(self, cursor) -> any:
        cursor.close()
        self.database.close()