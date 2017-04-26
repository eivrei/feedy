from abc import ABC
import mysql.connector


# Class to connect files to our database
class DBConnector(ABC):
    db_connection = mysql.connector.connect(user='magnukun_secure', password='YEa2VJXHxmWQ',
                                            host='mysql.stud.ntnu.no',
                                            database='magnukun_pudb')
    cursor = db_connection.cursor()

    # Used when there is an error between server and database
    def error(self):
        self.db_connection.rollback()
        self.close()

    # Saves our changes to the database
    def commit(self):
        self.db_connection.commit()
        self.close()

    # Close the connection to the database
    def close(self):
        self.cursor.close()
        self.db_connection.close()
