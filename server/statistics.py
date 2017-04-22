import sys
from db_connector import DbConnector
from numpy import std

'''
For each topic we must generate:
    - number of answers
    - average percent
    - standard deviation
    - keywords with a total answer percent on less than 20% (numAnswered/answers_per_topic < 0.2)

Statistics are saved in db as "[topic1, answers_per_topic, avgPercent, standard deviation, keyword1, keyword2][...]"
'''


class Statistics(DbConnector):
    def __init__(self, lecture_id):
        self.lecture_id = lecture_id
        self.all_topics = []
        self.all_answers = []
        self.answers_per_topic = []
        self.avgPercents = []
        self.low_scoring_keywords = []
        self.standard_deviations = []

    def run(self):
        try:
            self.get_answers()
            # If self.all_answers == [[]], then there are no answers to this lecture
            if not self.all_answers[0]:
                print("There are no answers to this lecture")
            else:
                self.get_avg_percents()
                self.get_standard_deviation()
                self.get_answers_per_topic()
                self.get_low_scoring_keywords()
                self.send_statistics()
                self.commit()
        except Exception as error:
            print(error)
            self.error()
        finally:
            self.close()

    # Collect all answers for this lecture from our database
    def get_answers(self):
                get_answers = "SELECT correctPercent, topic " \
                              "FROM QuizAnswer AS qa " \
                              "Natural JOIN QuizTopic AS qt " \
                              "WHERE qt.lecture_id=%s ORDER BY qt.topic_id ASC, qa.answer_id ASC" % self.lecture_id
                self.cursor.execute(get_answers)

                last_topic_text = ""
                topic_answers = []
                for correct_percent, topic_text in self.cursor:
                    if topic_text != last_topic_text:
                        if last_topic_text != "":
                            self.all_answers.append(topic_answers)
                            topic_answers = []
                        last_topic_text = topic_text
                        self.all_topics.append(topic_text)
                    topic_answers.append(correct_percent)
                self.all_answers.append(topic_answers)

    # Get average correctness percent for all topics
    def get_avg_percents(self):
        for topic in self.all_answers:
            avg = 0
            for answer in topic:
                avg += answer
            self.avgPercents.append(round(avg/len(topic), 1))

    # Get standard deviation for all topics
    def get_standard_deviation(self):
        for topic in range(len(self.all_topics)):
            self.standard_deviations.append(round(std(self.all_answers[topic]), 1))

    # Count number of answers per topic
    def get_answers_per_topic(self):
        query = "SELECT qa.topic_id, COUNT(*) FROM QuizAnswer AS qa NATURAL JOIN QuizTopic AS qt " \
                "WHERE qt.lecture_id = %s GROUP BY qa.topic_id" % self.lecture_id
        self.cursor.execute(query)
        for topic_id, answers in self.cursor:
            self.answers_per_topic.append(answers)

    # Get all keywords with an answered percentage less than 20%.
    def get_low_scoring_keywords(self):
        query = "SELECT keyword, numAnswered, topic " \
                "FROM QuizKeyword as qk JOIN QuizTopic AS qt ON qk.topic_id = qt.topic_id " \
                "WHERE lecture_id = %s ORDER BY qk.topic_id ASC" % self.lecture_id
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

    # Send statistics to database
    def send_statistics(self):
        statistics = ""
        for i in range(len(self.all_topics)):
            statistics += "[" + self.all_topics[i] + "," + str(self.answers_per_topic[i]) + "," + \
                          str(self.avgPercents[i]) + "," + str(self.gap[i]) + \
                          ("," if self.low_scoring_keywords[i] else "") + \
                          ",".join(keyword for keyword in self.low_scoring_keywords[i]) + "]"
        query = "UPDATE Lecture SET lectureStats = %s WHERE lecture_id = %s"
        self.cursor.execute(query, (statistics, self.lecture_id))

if __name__ == '__main__':
    statistics = Statistics(sys.argv[1])
    statistics.run()
