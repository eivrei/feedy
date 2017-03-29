from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from collections import OrderedDict
import wikipedia
import string

from wikipedia_topic_handlers import WikipediaKeywordExtractor


# Class for generation of quiz from raw data
class QuizGenerator:
    GRAMMATICAL_WORD_TAGS = {'CC', 'DT', 'EX', 'IN', 'MD', 'PDT', 'PRP', 'PRP$', 'RP', 'TO',
                             'UH'}  # uses Penn Treebank Tagset

    # INPUTS:
    # data is a list containing data from each slide of the form [topic1_data, topic2_data, ...]
    # where each "topicX_data"-field is of the form [title, keyword_1, keyword_2, ...]
    def __init__(self, data, quiz_language='english'):
        self.data = data
        self.quiz_language = quiz_language
        self.quiz = None

    # Cleaning the data in preparation of quiz generation
    def clean_data(self):
        cleaned_data = []

        self.data.pop(0)  # Always remove first page, which is assumed to be an intro-page
        if self.data[0][0] == 'Contents':
            self.data.pop(0)

        # Remove empty topics
        self.data = [topic_data for topic_data in self.data if len(topic_data) > 2]

        merged_data = []
        merged_topics = []
        for topic_id in range(len(self.data)):
            has_merged = False
            topic_data = self.data[topic_id]
            topic = topic_data[0]
            merged_data.append(topic_data)
            for other_topic_data in self.data[topic_id+1:]:
                other_topic = other_topic_data[0]
                if other_topic in merged_topics:  # If already merged into "merged_data"
                    continue
                if topic == other_topic:
                    merged_data[-1] += other_topic_data[1:]

            merged_topics = [topic_data[0] for topic_data in merged_data]

        for topic_data in merged_data:
            cleaned_data.append([])

            for datum_id in range(len(topic_data)):
                datum = topic_data[datum_id]
                if datum_id != 0:
                    datum = rem_grammatical_words(datum, self.quiz_language)
                    datum = rem_non_alphanumeric_symbols(datum)
                    # datum = rem_duplicates(datum)

                cleaned_data[len(cleaned_data)-1].append(datum)

        self.data = cleaned_data

    # Idea for extension: use PyDictionary to attach more words to the title

    # Some methods here for cleansing data
    #       - merge topics with same or similar title

    # Make the actual quiz in the agreed-upon format
    def make_quiz(self):
        # Define the initial weight for all words included in presentation itself
        default_weight = 10

        quiz = []
        for topic_data in self.data:
            topic = topic_data[0]
            quiz.append([topic])

            current_quiz_topic_data = quiz[len(quiz)-1]
            for keyphrase in topic_data[1:]:
                for keyword in keyphrase.split(' '):
                    included_kws = [kw_data[0] for kw_data in current_quiz_topic_data]
                    if keyword not in included_kws:
                        current_quiz_topic_data.append((keyword, default_weight))
                    else:
                        kw_index = included_kws.index(keyword)
                        new_kw_data = (current_quiz_topic_data[kw_index][0], current_quiz_topic_data[kw_index][1] + default_weight)
                        current_quiz_topic_data[kw_index] = new_kw_data

            try:
                wiki_kws = WikipediaKeywordExtractor(topic, self.quiz_language).extract_keywords()

                for keyword in wiki_kws.keys():
                    included_kws = [kw_data[0] for kw_data in current_quiz_topic_data]
                    if keyword not in included_kws:
                        current_quiz_topic_data.append((keyword, wiki_kws[keyword]))
                    else:
                        kw_index = current_quiz_topic_data.index(keyword)
                        current_quiz_topic_data[kw_index][1] += wiki_kws[keyword]

            # If wikipedia search for topic produces no results, simply move on to next topic
            except ValueError:
                continue
            except wikipedia.exceptions.DisambiguationError:
                continue

        # Remove the weakest keywords (weight < 10)
        quiz = [[quiz_data[i] for i in range(len(quiz_data)) if i == 0 or (quiz_data[i][1] >= 10 and quiz_data[i][0])] for quiz_data in quiz]

        self.quiz = quiz

    # def print_quiz(self):
    #     with open("quiz.txt", 'w') as file:
    #         for q in self.quiz:
    #             file.write("Topic: " + q[0] + "\n")
    #             file.write(", ".join(word for word in q[1:]))
    #             file.write("\n\n")

# Removes all ENGLISH stopwords as defined in nltk stopwords list, and all ENGLISH function words
def rem_grammatical_words(text, language):
    stop_words = set(stopwords.words(language))

    words = word_tokenize(text)

    tagged_words = pos_tag(words, language)
    lexical_words = ' '.join([tagged_word[0] for tagged_word in tagged_words if tagged_word[1] not in QuizGenerator.GRAMMATICAL_WORD_TAGS and tagged_word[0] not in stop_words])

    return lexical_words


# Removes all non-alphanumeric symbols except dashes and underscores connecting words
def rem_non_alphanumeric_symbols(text):
    whitelist = string.ascii_letters + string.digits + ' _-'
    clean_text = ''.join([char for char in text if char in whitelist]).lower()

    return clean_text


# Removes all duplicate words
# Should not be necessary, as duplicates are now handled (more effectively) in make_quiz() method
def rem_duplicates(text):
    unique_text = ' '.join(OrderedDict.fromkeys(text.split()))

    return unique_text

if __name__ == '__main__':
    from server.pptx_extraction import extract
    quiz_generator = QuizGenerator(extract("temp/test_1.pptx"))
    quiz_generator.clean_data()
    quiz_generator.make_quiz()
    # quiz_generator.print_quiz()
    print(quiz_generator.quiz)
