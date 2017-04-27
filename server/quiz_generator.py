import string
import wikipedia
import nltk
from collections import OrderedDict
from wikipedia_topic_handlers import WikipediaKeywordExtractor
nltk.data.path.append("/home/groupswww/pugruppe100/nltk_data")
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords


# Class for generation of quiz from raw data
class QuizGenerator:
    GRAMMATICAL_WORD_TAGS = {'CC', 'DT', 'EX', 'IN', 'MD', 'PDT', 'PRP', 'PRP$', 'RP', 'TO',
                             'UH'}  # uses Penn Treebank Tagset

    # INPUTS:
    # - "pptx_data": a list containing data from each slide on the form [topic1_data, topic2_data, ...]
    #    where each "topicX_data"-field is of the form [title, bullet1, bullet2, ...]
    # - "quiz_language": the language used by nltk for POS_tagger and stopwords list
    #    for now, only english is supported
    def __init__(self, pptx_data, quiz_language='english'):
        self.pptx_data = pptx_data
        self.quiz_language = quiz_language
        self.quiz = None

    def run(self):
        self.clean_data()
        self.make_quiz()

    # Clean self.pptx_data in preparation of quiz generation
    def clean_data(self):
        cleaned_data = []

        self.pptx_data.pop(0)  # Always remove first page, which is assumed to be an intro-page
        if self.pptx_data[0][0] == 'Contents':
            self.pptx_data.pop(0)

        # Remove empty topics
        self.pptx_data = [topic_data for topic_data in self.pptx_data if len(topic_data) > 2]

        # Merge identically named slides
        merged_data = []
        merged_topics = []
        for topic_id in range(len(self.pptx_data)):
            topic_data = self.pptx_data[topic_id]
            topic = topic_data[0]
            merged_data.append(topic_data)
            for other_topic_data in self.pptx_data[topic_id+1:]:
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

        self.pptx_data = cleaned_data

    # Make the actual quiz in the format [topic, (keyword1, weight1), (keyword2, weight2), ...]
    def make_quiz(self):
        # Define the initial weight for all words included in presentation itself
        default_weight = 10

        quiz = []
        for topic_data in self.pptx_data:
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
                        new_kw_data = (current_quiz_topic_data[kw_index][0], current_quiz_topic_data[kw_index][1] +
                                       default_weight)
                        current_quiz_topic_data[kw_index] = new_kw_data

            # Add keywords extracted from wikipedia page on topic, if possible
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
            except wikipedia.exceptions.PageError:
                continue
            except ValueError:
                continue
            except wikipedia.exceptions.DisambiguationError:
                continue
            except Exception as e:
                print('Unhandled exception:', e)

        # Remove the weakest keywords (weight < 10)
        quiz = [[quiz_data[i] for i in range(len(quiz_data)) if i == 0 or
                 (quiz_data[i][1] >= 10 and quiz_data[i][0])] for quiz_data in quiz]

        self.quiz = quiz


# Removes all ENGLISH stopwords as defined in nltk stopwords list, and all ENGLISH function words
def rem_grammatical_words(text, language):
    stop_words = set(stopwords.words(language))

    words = word_tokenize(text)

    tagged_words = pos_tag(words, language)
    lexical_words = ' '.join([tagged_word[0] for tagged_word in tagged_words if tagged_word[1] not in
                              QuizGenerator.GRAMMATICAL_WORD_TAGS and tagged_word[0] not in stop_words])

    return lexical_words


# Remove all non-alphanumeric symbols except spaces, dashes and underscores from "text"
def rem_non_alphanumeric_symbols(text):
    whitelist = string.ascii_letters + string.digits + ' -_'
    clean_text = ''.join([char for char in text if char in whitelist]).lower()

    return clean_text


# Remove all duplicate words from "text"
# Should not be necessary, as duplicates are now handled (more effectively) in make_quiz() method
def rem_duplicates(text):
    unique_text = ' '.join(OrderedDict.fromkeys(text.split()))

    return unique_text
