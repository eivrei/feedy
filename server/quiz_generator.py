

# Class for generation of quiz from raw data
class QuizGenerator:
    # INPUTS:
    # data is a list containing data from each slide on the form [[data from slide 1], [data from slide 2]...]
    def __init__(self, data):
        self.data = data

    # Some methods here for cleansing data
    #       - remove slides with no text
    #       - remove slides only containing title
    #       - remove lines containing just space
    #       - remove lines containing just symbols
    #       - merge slides with same or similar title
    #       - prune symbols (commas, quotation marks, etc.)
    #       - remove grammatical words (i.e. non-lexical words)

    # Some methods here for making quiz
