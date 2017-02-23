from nltk import word_tokenize, pos_tag
import string


# Class for generation of quiz from raw data
class QuizGenerator:
    GRAMMATICAL_WORDS = {'CC', 'DT', 'EX', 'IN', 'MD', 'PDT', 'PRP', 'PRP$', 'RP', 'TO',
                         'UH'}  # uses Penn Treebank Tagset

    # INPUTS:
    # data is a list containing data from each slide of the form [topic1_data, topic2_data, ...]
    # where each "topicX_data"-field is of the form [topic, text_1, text_2, ...]
    def __init__(self, data, quiz_language='eng'):
        self.data = data
        self.quiz_language = quiz_language

    def rem_empty_topics(self):
        self.data = [topic_data for topic_data in self.data if len(topic_data) < 2]

    def clean_text(self):
        for topic_data in self.data:
            for datum in topic_data:
                datum = rem_grammatical_words(datum, self.quiz_language)
                datum = rem_non_alphanumeric_symbols(datum)
                datum = rem_duplicates(datum)

    # Some methods here for cleansing data
    #       - merge topics with same or similar title

    # Some methods here for making quiz


# Removes all ENGLISH grammatical (function) words
# uses PoS tagger in nltk library
def rem_grammatical_words(text, language):
    words = word_tokenize(text)
    tagged_words = pos_tag(words, lang='eng')
    words = [word[0] for word in tagged_words if word[1] not in QuizGenerator.GRAMMATICAL_WORDS]
    return words


# Removes all non-alphanumeric symbols except dashes and underscores connecting words
def rem_non_alphanumeric_symbols(text):
    whitelist = string.ascii_letters + string.digits + ' _-'
    clean_text = ''.join([char for char in text if char in whitelist]).lower()
    return clean_text

# Removes all duplicate words
def rem_duplicates(text):
    unique_text = ' '.join(set(text.split()))
    return unique_text
