import mysql.connector

cnx = mysql.connector.connect(user='magnukun_pu100', password='pugruppe100',
                              host='mysql.stud.ntnu.no',
                              database='magnukun_pudb')
cursor = cnx.cursor()


def send_quiz(lecture_id, quiz):
    try:
        add_quiz = "INSERT INTO Quiz(QuizPlaintext, LectureID) " \
                    "VALUES(%s, %s)"
        args = quiz, lecture_id
        cursor.execute(add_quiz, args)
        cnx.commit()
        cnx.close()
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        cnx.close()
