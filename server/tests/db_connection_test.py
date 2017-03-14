import unittest
from server.db_connection import *


class DbConnectionTest(unittest.TestCase):
    def setUp(self):
        self.db_connection = DatabaseConnector(2, [['Data', ('ram', 3), ('ssd', 2), ('cpu', 1), ('cache', 1)], ['SSD',
                                              ('much', 1), ('better', 1), ('hdd', 1), ('faster', 1), ('expensive', 1)],
                                              ['Python', ('print', 1), ('procedural', 1), ('oriented', 1), ('also', 1),
                                              ('object', 1), ('good', 1), ('first', 1), ('language', 1),
                                              ('for-loops', 1), ('simple', 1), ('manage', 1)]])
        try:
            self.db_connection.send_topics()
            self.db_connection.send_keywords()

        except Exception:
            self.fail("There was an error sending the quiz")

    def test_send_topics(self):
        try:
            get_topic = "SELECT Text FROM QuizTopic WHERE TopicID = %s AND LectureID = %s"
            self.db_connection.cursor.execute(get_topic, (self.db_connection.topic_id[0], self.db_connection.lecture_id))
            result1 = self.db_connection.cursor.fetchone()[0]

            # Check if database contains the first topic
            self.assertEqual(result1, "Data", "Expected 'Data', but got " + result1)

            self.db_connection.cursor.execute(get_topic, (self.db_connection.topic_id[-1], self.db_connection.lecture_id))
            result2 = self.db_connection.cursor.fetchone()[0]

            # Check if database contains the last topic
            self.assertEqual(result2, "Python", "Expected 'Python', but got " + result2)

        except Exception:
            self.fail()

    def test_send_keyword(self):
        try:
            get_keyword = "SELECT Text FROM QuizKeyword WHERE TopicID = %s AND Text = %s"
            self.db_connection.cursor.execute(get_keyword, (self.db_connection.topic_id[0], "ram"))
            result1 = self.db_connection.cursor.fetchone()[0]

            # Check if database contains the first keyword
            self.assertEqual(result1, "ram", "Expected 'ram', but got " + result1)

            self.db_connection.cursor.execute(get_keyword, (self.db_connection.topic_id[-1], "manage"))
            result2 = self.db_connection.cursor.fetchone()[0]

            # Check if database contains the last keyword
            self.assertEqual(result2, "manage", "Expected 'manage', but got " + result2)

        except Exception:
            self.fail()

if __name__ == '__main__':
    unittest.main()
