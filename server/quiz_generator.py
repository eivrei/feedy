from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from collections import OrderedDict
import string

# Class for generation of quiz from raw data
class QuizGenerator:
    GRAMMATICAL_WORD_TAGS = {'CC', 'DT', 'EX', 'IN', 'MD', 'PDT', 'PRP', 'PRP$', 'RP', 'TO',
                         'UH'}  # uses Penn Treebank Tagset
    STOP_WORDS = set(stopwords.words('english'))

    # INPUTS:
    # data -- a list containing data from each slide of the form [topic1_data, topic2_data, ...]
    # where each "topicX_data"-field is of the form [topic, text_1, text_2, ...]
    def __init__(self, data, quiz_language='eng'):
        self.data = data
        self.quiz_language = quiz_language
        self.quiz = None
        self.rem_empty_topics()
        self.clean_data()
        self.make_quiz()
        #self.send_quiz()

    def rem_empty_topics(self):
        self.data = [topic_data for topic_data in self.data if len(topic_data) > 2]

    # Cleaning the data in preparation of quiz generation
    def clean_data(self):
        cleaned_data = []

        self.data.pop(0)
        if self.data[0][0] == 'Contents':
            self.data.pop(0)

        merged_data = []
        for topic_id in range(len(self.data)):
            hasMerged = False
            topic_data = self.data[topic_id]
            topic = topic_data[0]
            for other_topic_data in self.data[topic_id+1:]:
                other_topic = other_topic_data[0]
                if topic == other_topic:
                    merged_data.append(topic_data + other_topic_data[1:])
                    hasMerged = True
            if not hasMerged:
                merged_data.append(topic_data)

        for topic_data in merged_data:
            cleaned_data.append([])

            for datum_id in range(len(topic_data)):
                datum = topic_data[datum_id]
                if datum_id != 0:
                    datum = rem_grammatical_words(datum, self.quiz_language)
                    datum = rem_non_alphanumeric_symbols(datum)
                    datum = rem_duplicates(datum)

                cleaned_data[len(cleaned_data)-1].append(datum)

        self.data = cleaned_data

    # Idea for extension: use PyDictionary to attach more words to the title

    # Some methods here for cleansing data
    #       - merge topics with same or similar title

    # Some methods here for making quiz
    def make_quiz(self):
        quiz = []
        for topic_data in self.data:
            topic = topic_data[0]
            quiz.append([topic])
            for datum in topic_data[1:]:
                for word in datum.split():
                    quiz[len(quiz)-1].append((word, 1))
        self.quiz = quiz

    def print_quiz(self):
        with open("quiz.txt", 'w') as file:
            for q in self.quiz:
                file.write("Topic: " + q[0] + "\n")
                file.write(", ".join(word for word in q[1:]))
                file.write("\n\n")


# Removes all ENGLISH stopwords as defined in nltk stopwords list, and all ENGLISH function words
def rem_grammatical_words(text, language):
    words = word_tokenize(text)

    non_stop_words = [word for word in words if word.lower() not in QuizGenerator.STOP_WORDS]

    tagged_words = pos_tag(non_stop_words, lang='eng')
    lexical_words = ' '.join([word[0] for word in tagged_words if word[1] not in QuizGenerator.GRAMMATICAL_WORD_TAGS and word[0] not in QuizGenerator.STOP_WORDS])

    return lexical_words


# Removes all non-alphanumeric symbols except dashes and underscores connecting words
def rem_non_alphanumeric_symbols(text):
    whitelist = string.ascii_letters + string.digits + ' _-'
    clean_text = ''.join([char for char in text if char in whitelist]).lower()

    return clean_text


# Removes all duplicate words
def rem_duplicates(text):
    unique_text = ' '.join(OrderedDict.fromkeys(text.split()))

    return unique_text

if __name__ == '__main__':
    from server.pptx_extraction import extract
    quiz_generator = QuizGenerator(extract("D:/Feedy/pugruppe100/server/temp/test_1.pptx"))
    quiz_generator.rem_empty_topics()
    quiz_generator.clean_data()
    quiz_generator.make_quiz()
    # quiz_generator.print_quiz()
    print(quiz_generator.quiz)
