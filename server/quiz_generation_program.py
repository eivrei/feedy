from server.pptx_extraction import extract
from server.quiz_generator import *
from server.quiz_sender import QuizSender


def main(filename, lecture_id):
    # Generate raw data from pptx file
    raw_data = extract("/groupswww/pugruppe100/server/temp/" + filename + ".pptx")

    # Generate quiz data from raw_data
    quiz_generator = QuizGenerator(raw_data)
    quiz_generator.rem_empty_topics()
    quiz_generator.clean_data()
    quiz_generator.make_quiz()

    # Send quiz to db
    db_connection = QuizSender(lecture_id, quiz_generator.quiz)
    db_connection.send_quiz()

# if __name__ == '__main__':
#     main()
