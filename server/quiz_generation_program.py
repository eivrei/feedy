import sys
from server.pptx_extraction import extract
from server.quiz_generator import *
from server.quiz_sender import QuizSender


def main(filename, lecture_id):
    # Generate raw data from pptx file
    raw_data = extract("/home/groupswww/pugruppe100/pugruppe100/server/temp/" + filename + ".pptx")

    # Generate quiz data from raw_data
    quiz_generator = QuizGenerator(raw_data)
    quiz_generator.run()

    # Send quiz to db
    quiz_sender = QuizSender(lecture_id, quiz_generator.quiz)
    quiz_sender.run()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
