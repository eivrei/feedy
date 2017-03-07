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

if __name__ == '__main__':
    send_quiz(2, "[['Data', 'ram', 'ssd', 'cpu', 'cache'], ['SSD', 'much', 'better', 'hdd', 'faster', 'expensive'],"
                 " ['Python', 'print', 'procedural', 'oriented', 'also', 'object', 'good', 'first', 'language',"
                 " 'for-loops', 'simple', 'manage']]")
