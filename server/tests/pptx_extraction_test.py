import unittest
from server.pptx_extraction import extract


class PptxExtractionTest(unittest.TestCase):
    def setUp(self):
        self.path = "/Users/eivindreime/git/pugruppe100/server/temp/test_1.pptx"
        self.data = extract(self.path)

    def test_list_in_return(self):
        self.assertEqual(type(self.data), list, "Return type is not a list")

    def test_containing_elements(self):
        self.assertTrue(len(self.data) > 0, "The list was empty")

    def test_points(self):
        self.assertEqual(self.data[0][0], "A fantastic presentation",
                        "Expected 'A fantastic presentation' but got " + self.data[0][0])
        self.assertEqual(self.data[2][0], "Children", "Expected 'Children' but got " + self.data[2][0])
        self.assertEqual(self.data[5][0], "Python", "Expected 'Python' but got " + self.data[5][0])

    def test_whole_sentence(self):
        self.assertEqual(self.data[2][3], "Curious as in ”curious Nils”",
                    "Expected 'Curious as in ”curious Nils”' but got " + self.data[4][1])
        self.assertEqual(self.data[5][1], "Print()")

    def test_sub_points(self):
        self.assertTrue(['SSD', 'Much better than HDD', 'Faster', 'More expensive'] in self.data
                        ,"The list does not contains sub points")

    def test_sub_points_on_right_place(self):
            self.assertEqual(['SSD', 'Much better than HDD', 'Faster', 'More expensive'], self.data[4])

    def test_sub_sub_points(self):
        self.assertFalse(["Difficult to make"] in self.data, "There are some sub sub point in there. Not good")
        self.assertFalse("Difficult to make" in self.data[3], "There are some sub sub point in there. Not good")
        self.assertFalse("Difficult to make" in self.data[4], "There are some sub sub point in there. Not good")

if __name__ == '__main__':
    unittest.main()
