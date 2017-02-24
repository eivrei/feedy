import unittest
from server.pptx_extraction import extract


class PptxExtractionTest(unittest.TestCase):

    def setUp(self):
        self.path = "/Users/eivindreime/git/pugruppe100/server/temp/"

    def test_list_in_return(self):
        self.assertEqual(type(extract(self.path + "test_1.pptx")), list, "Return type is not a list")

    def test_containing_elements(self):
        self.assertTrue(len(extract(self.path + "test_1.pptx")) > 0, "The list was empty")

    def test_points(self):
        data = extract(self.path + "test_2.pptx")
        self.assertEqual(data[0][0], "En fantastisk presentasjon", "Expected 'En fantastisk presentasjon' but got " + data[0][0])
        self.assertEqual(data[1][0], "Barn", "Expected 'Barn' but got " + data[1][0])
        self.assertEqual(data[4][0], "Python", "Expected 'Python' but got " + data[4][0])

    def test_sub_points(self):
        self.assertTrue(["SSD", "Mye bedre enn en HDD", "Raskere", "Dyrere"] in extract(self.path + "test_2.pptx")
                        , "The list does not contains sub points")

    def test_sub_sub_points(self):
        data = extract(self.path + "test_2.pptx")
        self.assertFalse(["Vanskeligere å lage"] in data, "There are some sub sub point in there. Not good")
        self.assertFalse("Vanskeligere å lage" in data[2], "There are some sub sub point in there. Not good")
        self.assertFalse("Vanskeligere å lage" in data[3], "There are some sub sub point in there. Not good")

if __name__ == '__main__':
    unittest.main()
