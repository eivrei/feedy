# Note: susceptible to zip bombs


from zipfile import ZipFile
import os
from shutil import copyfile


class PptxToXml:
    # INPUTS:
    # pptx_name - name of pptx file to be converted
    def __init__(self, pptx_name):
        self.pptx_name = pptx_name
        self.zip_name = None

    # Creates a new .zip file based on .pptx
    def copy_and_rename(self):
        pos = self.pptx_name.index('.')
        pptx_basename = self.pptx_name[:pos]  # pptx_name - name of pptx file minus extension name

        zip_name = 'zip_' + pptx_basename + '.zip'  # zip_name - name of converted zip file
        copyfile('temp\\' + self.pptx_name, 'temp\\' + zip_name)

        self.zip_name = zip_name

    # Extracts zip-file to directory indicated in constructor
    def extract_zip_file(self):
        with ZipFile('temp\\' + self.zip_name, 'r') as zip_file:
            extract_dir = 'extraction_folder\\'
            zip_file.extractall(extract_dir)

    # Deletes .pptx and .zip files after they have been converted
    def delete_files(self):
        pass


# if __name__ == '__main__':
#     pptxToXml = PptxToXml('temp\\test_1.pptx')
#     pptxToXml.copy_and_rename()
#     pptxToXml.extract_zip_file()
