from server.db_connector import DbConnector
from numpy import std

'''
For hvert topic skal følgende genereres:
    - antall svar
    - gjennomsnittsprosent
    - et tall på sprik i svar
    - keywords med en svarprosent på mindre enn X %

Lagres i databasen på formen [topic1, numAnswered, avgPercent, gapNumber, keyword1, keyword2][topic2....]
'''


class Statistics(DbConnector):
    def __init__(self, lecture_id):
        self.lecture_id = lecture_id
        self.all_topics = []
        self.all_answers = []
        self.answers_per_topic = []
        self.avgPercents = []
        self.low_scoring_keywords = []
        self.gap = []

    def run(self):
        try:
            self.get_answers()
            self.get_avg_percents()
            self.get_gap()
            self.get_answers_per_topic()
            self.get_low_scoring_keywords()
            self.send_statistics()
            self.commit()
        except Exception as error:
            print(error)
            self.error()
        finally:
            self.close()

    def get_answers(self):
                get_answers = "SELECT CorrectPercent, qt.Text " \
                              "FROM QuizAnswer AS qa " \
                              "Natural JOIN QuizTopic AS qt " \
                              "WHERE qt.LectureID=%s ORDER BY qt.TopicID ASC, qa.AnswerID ASC" % self.lecture_id
                self.cursor.execute(get_answers)

                last_topic = ""
                topic_answers = []
                for correct_percent, topic_text in self.cursor:
                    if topic_text != last_topic:
                        if last_topic != "":
                            self.all_answers.append(topic_answers)
                            topic_answers = []
                        last_topic = topic_text
                        self.all_topics.append(topic_text)
                    topic_answers.append(correct_percent)
                self.all_answers.append(topic_answers)
                print("all_topics: ", self.all_topics, "\nall_answers: ", self.all_answers)

    def get_avg_percents(self):
        for topic in self.all_answers:
            avg = 0
            for answer in topic:
                avg += answer
            self.avgPercents.append(round(avg/len(topic), 1))

    def get_gap(self):
        for topic in range(len(self.all_topics)):
            self.gap.append(round(std(self.all_answers[topic]), 1))

    def get_answers_per_topic(self):
        query = "SELECT qa.TopicID, COUNT(*) FROM QuizAnswer AS qa NATURAL JOIN QuizTopic AS qt " \
                "WHERE qt.LectureID = %s GROUP BY qa.TopicID" % self.lecture_id
        self.cursor.execute(query)
        for topic_id, answers in self.cursor:
            self.answers_per_topic.append(answers)
        print("answers_per_topic: ", self.answers_per_topic)

    def get_low_scoring_keywords(self):
        query = "SELECT qk.Text, NumAnswered, qt.Text " \
                "FROM QuizKeyword as qk JOIN QuizTopic AS qt ON qk.TopicID = qt.TopicID " \
                "WHERE LectureID = %s ORDER BY qk.TopicID ASC" % self.lecture_id
        self.cursor.execute(query)

        last_topic = ""
        keywords = []
        for keyword, num_answered, topic in self.cursor:
            if topic != last_topic and topic in self.all_topics:
                if last_topic != "":
                    self.low_scoring_keywords.append(keywords)
                    keywords = []
                last_topic = topic
            if (num_answered/self.answers_per_topic[self.all_topics.index(topic)]) <= 0.20:
                keywords.append(keyword)
        self.low_scoring_keywords.append(keywords)
        print("low_scoring_keywords: ", self.low_scoring_keywords)

    def send_statistics(self):
        statistics = ""
        for i in range(len(self.all_topics)):
            statistics += "[" + self.all_topics[i] + "," + str(self.answers_per_topic[i]) + "," + str(self.avgPercents[i]) + "," + \
                          str(self.gap[i]) + ("," if self.low_scoring_keywords[i] else "") + ",".join(keyword for keyword in self.low_scoring_keywords[i]) + "]"
        print(statistics)
        s = "hei"
        query = "UPDATE Lecture SET Statistics = %s WHERE LectureID = %s"
        self.cursor.execute(query, (statistics, self.lecture_id))

if __name__ == '__main__':
    statistics = Statistics(2)
    statistics.run()
