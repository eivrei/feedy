import unittest
from server.quiz_generator import QuizGenerator


class QuizGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.data_in = [['A fantastic presentation', 'By me'], ['Contents', 'Children', 'Data', 'Python', 'This one is without points'], ['Children', 'Little and cute', 'They can be naughty or nice', 'Curious as in ”curious Nils”', 'Can be grumpy'], ['Data', 'RAM', 'SSD', 'CPU', 'Cache'], ['SSD', 'Much better than HDD', 'Faster', 'More expensive'], ['Python', 'Print()', 'Procedural oriented, but can also be object oriented', 'A good first language', 'For-loops are simple to manage'], ['This one is without points', '']]
        self.data_out = [['Children', 'little', 'cute', 'naughty', 'nice', 'curious', 'nils', 'grumpy'], ['Data', 'ram', 'ssd', 'cpu', 'cache'], ['SSD', 'much', 'better', 'hdd', 'faster', 'expensive'], ['Python', 'print', 'procedural', 'oriented', 'also', 'object', 'good', 'first', 'language', 'for-loops', 'simple', 'manage']]
        self.rel_path = "/server/temp/test_1.pptx"

        quiz_generator = QuizGenerator(self.data_in)
        quiz_generator.generate()
        self.quiz_data = quiz_generator.quiz
        self.topic_list = [topic_data[0] for topic_data in self.quiz_data]  # Generate list of all topics in quiz

    def test_remove_ppt_intro(self):
        self.assertNotEqual('A fantastic presentation', self.topic_list[0], "The ppt intro was not removed")

    def test_remove_content_page(self):
        self.assertNotEqual('Contents', self.topic_list[0], "The ppt content page was not removed")
        self.assertNotEqual('contents', self.quiz_data, "The ppt content page was not removed")

    def test_lower_case(self):
        self.assertEqual(self.quiz_data[0][0], "Children", "Expected 'Children', but got " + self.quiz_data[0][0])
        self.assertEqual(self.quiz_data[2][4][0], "faster", "Expected 'faster', but got " + self.quiz_data[2][4][0])

    def test_remove_symbols(self):
        self.assertEqual(self.quiz_data[3][1][0], "print", "Expected 'print', but got " + self.quiz_data[3][1][0])
        self.assertEqual(self.quiz_data[3][2][0], "procedural",
                         "Expected 'procedural', but got " + self.quiz_data[3][2][0])

    def test_remove_stopwords(self):
        self.assertEqual(self.quiz_data[3][1][0], "print", "Expected 'print', but got " + self.quiz_data[3][1][0])
        self.assertEqual(self.quiz_data[3][2][0], "procedural",
                         "Expected 'procedural', but got " + self.quiz_data[3][2][0])

    def test_remove_slide_without_points(self):
        self.assertNotIn('This one is without points', self.topic_list, "Slides without points are not removed")

    def test_total_cleaning(self):
        pass
        # TODO: Remove, same output not useful test

if __name__ == '__main__':
    unittest.main()
