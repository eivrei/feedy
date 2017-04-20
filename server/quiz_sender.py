from db_connector import DbConnector


class QuizSender(DbConnector):
    def __init__(self, lecture_id, quiz_data):
        self.lecture_id = lecture_id
        self.quiz_data = quiz_data
        self.topic_id = []

    def run(self):
        self.send_topics()
        self.send_keywords()

    def send_topics(self):
        add_topic = "INSERT INTO QuizTopic(topic_id, topic, lecture_id) VALUES (NULL, %s, %s)"
        for topic in self.quiz_data:
            self.cursor.execute(add_topic, (topic.pop(0), self.lecture_id))
            self.topic_id.append(self.cursor.lastrowid)

    def send_keywords(self):
        add_keyword = "INSERT INTO QuizKeyword VALUES (NULL, %s, %s, %s, 0)"
        index = 0
        for topic in self.quiz_data:
            for keyword, weight in topic:
                self.cursor.execute(add_keyword, (keyword, weight, self.topic_id[index]))
            index += 1
