import xml.etree.ElementTree as etree
import os.path


class XmlToRawData:
    def __init__(self):
        self.path = "./ppt_template/basic_ppt/ppt/slides/"
        # self.path = './extraction_folder/ppt/slides/'  # Set path for extracting of slides
        self.number_of_slides = len([f for f in os.listdir(self.path) if f.endswith('.xml')
                                     and os.path.isfile(os.path.join(self.path, f))]) # Find number of slides in folder

    # Generate data from .xml files
    def generate_data(self):
        all_data = []
        for file_nr in range(1, self.number_of_slides + 1):
            slide_data = []
            tree = etree.parse(self.path + 'slide' + str(file_nr) + '.xml')
            for element in tree.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t'):
                slide_data.append(element.text)
            all_data.append(slide_data)
        return all_data

        # To be implemented!
        # Send data to quiz generator

if __name__ == "__main__":
    # execute only if run as a script
    xmlToRawData = XmlToRawData()
    print(xmlToRawData.generate_data())