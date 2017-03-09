import mysql.connector


class DatabaseConnector:
    def __init__(self, lecture_id, quiz_data):
        self.lecture_id = lecture_id
        self.quiz_data = quiz_data
        self.db_connection = mysql.connector.connect(user='magnukun_pu100', password='pugruppe100',
                                                     host='mysql.stud.ntnu.no',
                                                     database='magnukun_pudb')
        self.cursor = self.db_connection.cursor()
        self.topic_id = []

    def send_quiz(self):
        try:
            self.send_topics()
            self.send_keywords()
            self.db_connection.commit()
            self.db_connection.close()
        except Exception as error:
            print("Error: ", error)
            self.db_connection.rollback()
        finally:
            self.cursor.close()
            self.db_connection.close()

    def send_topics(self):
        add_topic = "INSERT INTO QuizTopic (TopicID, Text, LectureID) VALUES (NULL, %s, %s)"
        for topic in self.quiz_data:
            self.cursor.execute(add_topic, (topic.pop(0), self.lecture_id))
            self.topic_id.append(self.cursor.lastrowid)

    def send_keywords(self):
        add_keyword = "INSERT INTO QuizKeyword (KeywordID, Text, Weight, TopicID) VALUES (NULL, %s, %s, %s)"
        index = 0
        for topic in self.quiz_data:
            for keyword, weight in topic:
                self.cursor.execute(add_keyword, (keyword, weight, self.topic_id[index]))
            index += 1

if __name__ == '__main__':
    dbConnector = DatabaseConnector(2, [['Data', ('ram', 3), ('ssd', 2), ('cpu', 1), ('cache', 1)], ['SSD', ('much', 1),
                                        ('better', 1), ('hdd', 1), ('faster', 1), ('expensive', 1)], ['Python',
                                        ('print', 1), ('procedural', 1), ('oriented', 1), ('also', 1), ('object', 1),
                                        ('good', 1), ('first', 1), ('language', 1), ('for-loops', 1), ('simple', 1),
                                        ('manage', 1)]]
)
    dbConnector.send_quiz()
