import sys
import os
from pptx_extraction import extract
from quiz_generator import *
from quiz_sender import QuizSender


def main(filename, lecture_id):
    # Set path to .pptx file
    path = "/home/groupswww/pugruppe100/pugruppe100/server/temp/" + filename + ".pptx"

    # Generate raw data from pptx file
    raw_data = extract(path)

    # Generate quiz data from raw_data
    quiz_generator = QuizGenerator(raw_data)
    quiz_generator.run()

    # Send quiz to db
    quiz_sender = QuizSender(lecture_id, quiz_generator.quiz)
    quiz_sender.run()

    # Remove .pptx file from temp folder after quiz is generated
    os.remove(path)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
