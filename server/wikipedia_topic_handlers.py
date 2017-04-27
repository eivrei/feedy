import wikipedia
from nltk import word_tokenize, pos_tag


class WikipediaKeywordExtractor:
    WORD_TAG_WEIGHTS = {'NN': 5, 'NNS': 5, 'NNP': 5, 'NNPS': 5, 'JJ': 3, 'JJR': 3, 'JJS': 3, 'RB': 1, 'RBR': 1,
                        'RBS': 1}

    # May raise both ValueError and wikipedia.exceptions.DisambiguationError -- must be handled in generator
    def __init__(self, topic, language):
        self.language = language
        self.simple_topic = self.simplify_topic(topic)
        if self.simple_topic:
            self.summary = wikipedia.summary(self.simple_topic)
        else:
            # Raise an exception to be handled by QuizGenerator object
            # This exception should never actually be raised unless the topic is empty
            raise ValueError('Could not simplify topic')

    # Return a simplified version of "topic", to optimize wikipedia search results
    def simplify_topic(self, topic):
        simple_topic = ''

        found_noun = False

        words = word_tokenize(topic)
        tagged_words = pos_tag(words, self.language)
        for tagged_word in tagged_words:
            if tagged_word[1] in {'NN', 'NNS', 'NNP', 'NNPS'}:
                # Add consecutive nouns in "topic" to "simple_topic"
                simple_topic += tagged_word[0] + ' '
                found_noun = True
            elif found_noun:
                # Return the simplified topic if at least one noun has been found, but the current word is not a noun
                # simple_topic should now contain the first sequence of consecutive nouns in topic
                return simple_topic
            else:
                continue

        # If no words have been recognised as nouns, assume the topic is simple enough already
        return topic

    # Return dictionary with extracted wikipedia keywords as keys, and the corresponding weight as value
    # Choose keywords and their weight based on their word class and number of occurrences,
    # with specific word class weights defined in class variable WORD_TAG_WEIGHTS
    def extract_keywords(self):
        keywords = {}
        for tagged_word in pos_tag(word_tokenize(self.summary)):
            (word, tag) = tagged_word

            # If word is not sufficiently important, continue
            if tag not in WikipediaKeywordExtractor.WORD_TAG_WEIGHTS.keys():
                continue
            elif word not in keywords.keys():
                keywords[word.lower()] = WikipediaKeywordExtractor.WORD_TAG_WEIGHTS[tag]
            else:
                keywords[word.lower()] += WikipediaKeywordExtractor.WORD_TAG_WEIGHTS[tag]

        return keywords
