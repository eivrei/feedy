import sys
import os
from pptx_extraction import extract
from quiz_generator import *
from quiz_sender import QuizSender
from db_connector import DbConnector


class QuizGenerationProgram(DbConnector):
    def __init__(self, filename, lecture_id):
        self.filename = filename  # filename on format word_word_word
        self.lecture_id = lecture_id
        # self.path = "/home/groupswww/pugruppe100/pugruppe100/server/temp/" + self.filename + ".pptx"
        self.path = "/Users/eivindreime/git/pugruppe100/server/temp/" + self.filename + ".pptx"
        self.raw_data = ""
        self.quiz = ""

    def run(self):
        # Generate raw data from pptx file
        self.get_raw_data()

        # Generate quiz data from raw_data
        self.generate_quiz()
        try:
            # Send quiz to db
            self.send_quiz()

            # Add name to lecture in database
            self.add_lecture_name()

            self.commit()
        except Exception as error:
            print("Error: ", error)
            self.error()
        finally:
            self.close()

        # Remove .pptx file from temp folder after quiz is generated
        os.remove(self.path)

    def get_raw_data(self):
        self.raw_data = extract(self.path)

    def generate_quiz(self):
        quiz_generator = QuizGenerator(self.raw_data)
        quiz_generator.run()
        self.quiz = quiz_generator.quiz

    def send_quiz(self):
        quiz_sender = QuizSender(self.lecture_id, self.quiz)
        quiz_sender.run()

    def add_lecture_name(self):
        name = " ".join(word for word in self.filename.split('_'))
        self.cursor.execute("UPDATE Lecture SET lectureName = %s WHERE lecture_id = %s", (name, self.lecture_id))

if __name__ == '__main__':
    program = QuizGenerationProgram(sys.argv[1], sys.argv[2])
    program.run()
