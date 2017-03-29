from abc import ABC
import mysql.connector


class DbConnector(ABC):
    db_connection = mysql.connector.connect(user='magnukun_secure', password='YEa2VJXHxmWQ',
                                            host='mysql.stud.ntnu.no',
                                            database='magnukun_pudb')
    cursor = db_connection.cursor()

    def error(self):
        self.db_connection.rollback()
        self.close()

    def commit(self):
        self.db_connection.commit()
        self.close()

    def close(self):
        self.cursor.close()
        self.db_connection.close()