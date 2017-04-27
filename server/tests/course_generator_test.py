import unittest
from server.web_scraper import CourseGenerator
from server.db_connector import DBConnector


class CourseGeneratorTest(unittest.TestCase, DBConnector):
    @classmethod
    def setUpClass(cls):
        cls.course_generator = CourseGenerator("tma4105")
        # NTNU's website is giving different responses. Run scraper several times to assure we are getting all data
        cls.course_generator.get_raw_data()
        cls.course_generator.find_lectures()
        cls.course_generator.update_db()

    def test_find_lectures(self):
        self.assertEqual(len(self.course_generator.lectures), 154, "There is missing some lecture objects here. Expected 154, "
                                                            "but got " + str(len(self.course_generator.lectures)))
        self.assertEqual(len(self.course_generator.lectures_by_parallel['MTFYMA, MTIØT, MTMART, MTNANO, MTTK']), 14,
                         "Expected 14 lectures with to the parallel 'MTFYMA, MTIØT, MTMART, MTNANO, MTTK', but got" +
                         str(self.course_generator.lectures_by_parallel['MTFYMA, MTIØT, MTMART, MTNANO, MTTK']))
        for lecture in self.course_generator.lectures_by_parallel['MTFYMA, MTIØT, MTMART, MTNANO, MTTK']:
            self.assertEqual(lecture.programmes, 'MTFYMA, MTIØT, MTMART, MTNANO, MTTK',
                             "This lecture is under wrong parallel. Expected 'MTFYMA, MTIØT, MTMART, MTNANO, MTTK', "
                             "but got" + lecture.programmes)

    def test_get_all_weeks(self):
        weeks = self.course_generator.get_all_weeks(['1-3', '12-14', '17'])
        self.assertEqual(weeks, [1, 2, 3, 12, 13, 14, 17], "Expected [1-3, 12-14, 17], but got" + str(weeks))

    def test_commit(self):
        get_course = "SELECT COUNT(*) FROM Course WHERE course_code = 'TMA4105'"
        get_parallels = "SELECT COUNT(*) FROM Parallel WHERE course_code = 'TMA4105'"
        get_lectures = "SELECT COUNT(*) FROM Lecture AS l JOIN LectureParallel AS lp ON l.lecture_id = lp.lecture_id " \
                       "JOIN Parallel AS p ON lp.parallel_id = p.parallel_id WHERE course_code = 'TMA4105'"
        self.cursor.execute(get_course)
        self.assertEqual(self.cursor.fetchone()[0], 1, "We are missing a course with course_code 'TMA4105'")

        self.cursor.execute(get_parallels)
        parallel_count = self.cursor.fetchone()[0]
        self.assertEqual(parallel_count, 9, "Expected 9 parallels, but got " + str(parallel_count))

        self.cursor.execute(get_lectures)
        lecture_count = self.cursor.fetchone()[0]
        self.assertEqual(lecture_count, 154, "Expected 154 lectures, but got " + str(lecture_count))

if __name__ == '__main__':
    unittest.main()
