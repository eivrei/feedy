import unittest
from server.quiz_generator import QuizGenerator


class QuizGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.data_in = [['A fantastic presentation', 'By me'], ['Contents', 'Children', 'Data', 'Python', 'This one is without points'], ['Children', 'Little and cute', 'They can be naughty or nice', 'Curious as in ”curious Nils”', 'Can be grumpy'], ['Data', 'RAM', 'SSD', 'CPU', 'Cache'], ['SSD', 'Much better than HDD', 'Faster', 'More expensive'], ['Python', 'Print()', 'Procedural oriented, but can also be object oriented', 'A good first language', 'For-loops are simple to manage'], ['This one is without points', '']]
        self.data_out = [['Children', 'little', 'cute', 'naughty', 'nice', 'curious', 'nils', 'grumpy'], ['Data', 'ram', 'ssd', 'cpu', 'cache'], ['SSD', 'much', 'better', 'hdd', 'faster', 'expensive'], ['Python', 'print', 'procedural', 'oriented', 'also', 'object', 'good', 'first', 'language', 'for-loops', 'simple', 'manage']]
        self.path = "/Users/eivindreime/git/pugruppe100/server/temp/test_1.pptx"
        self.quiz_data = QuizGenerator(self.data_in).quiz

    def test_remove_ppt_into(self):
        self.assertNotIn(['A fantastic presentation', 'By me'], self.quiz_data, "The ppt intro was not removed")
        self.assertNotIn(['A', 'fantastic', 'presentation', 'By', 'me'], self.quiz_data, "The ppt intro was not removed")

    def test_remove_content_page(self):
        self.assertNotIn(['Contents', 'Children', 'Data', 'Python', 'This', 'one', 'is', 'without', 'points'], self.quiz_data,
                         "The ppt content page was not removed")
        self.assertNotIn(['contents', 'children', 'data', 'python', 'this', 'one', 'is', 'without', 'points'], self.quiz_data,
                         "The ppt content page was not removed")
        self.assertNotIn(['Contents', 'children', 'data', 'python', 'this', 'one', 'is', 'without', 'points'], self.quiz_data,
                         "The ppt content page was not removed")

    def test_lower_case(self):
        self.assertEqual(self.quiz_data[0][0], "Children", "Expected 'Children', but got " + self.quiz_data[0][0])
        self.assertEqual(self.quiz_data[2][4], "faster", "Expected 'faster', but got " + self.quiz_data[2][4])

    def test_remove_symbols(self):
        self.assertEqual(self.quiz_data[3][1], "print", "Expected 'print', but got " + self.quiz_data[3][1])
        self.assertEqual(self.quiz_data[3][2], "procedural",
                         "Expected 'procedural', but got " + self.quiz_data[3][2])

    def test_remove_stopwords(self):
        self.assertEqual(self.quiz_data[3][1], "print", "Expected 'print', but got " + self.quiz_data[3][1])
        self.assertEqual(self.quiz_data[3][2], "procedural",
                         "Expected 'procedural', but got " + self.quiz_data[3][2])

    def test_remove_slide_without_points(self):
        self.assertNotIn(['This one is without points', ''], self.quiz_data, "Slides without points are not removed")

    def test_total_cleaning(self):
        self.assertEqual(self.quiz_data, self.data_out, "Output not as expected")

if __name__ == '__main__':
    unittest.main()
