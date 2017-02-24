import unittest
from server.quiz_generator import QuizGenerator


class QuizGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.data_in = [['A fantastic presentation', 'By me'], ['Children', 'Little and cute', 'They can be naughty or nice', 'Curious as in ”curious Nils”', 'Can be grumpy'], ['SSD', 'Much better than HDD', 'Faster', 'More expensive'], ['Data', 'RAM', 'SSD', 'CPU', 'Cache'], ['Python', 'Print()', 'Procedural oriented, but can also be object oriented', 'A good first language', 'For-loops are simple to manage']]
        self.data_out = [['Children', 'little cute', 'naughty nice', 'curious nils', 'grumpy'], ['SSD', 'much better hdd', 'faster', 'expensive'], ['Data', 'ram', 'ssd', 'cpu', 'cache'], ['Python', 'print', 'procedural oriented also object', 'good first language', 'for-loops simple manage']]

    def test_data_cleaning(self):
        quiz_gen = QuizGenerator(self.data_in)
        quiz_gen.clean_data()
        self.assertEqual(quiz_gen.data, self.data_out, "Output not as expected")
