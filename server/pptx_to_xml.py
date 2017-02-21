# Note: susceptible to zip bombs


from zipfile import ZipFile
import os
from shutil import copyfile


class PptxToXml:
    # INPUTS:
    # pptx_dir - directory of pptx file to be converted
    # zip_folder - folder in which to save zip file
    # extraction_folder - folder in which to extract zip file
    def __init__(self, pptx_dir, zip_folder='temp/', extraction_folder='extraction_folder/'):
        self.pptx_dir = pptx_dir
        self.zip_folder = zip_folder
        self.extraction_folder = extraction_folder

        self.dest_zip_dir = None

    # Creates a new .zip file based on .pptx
    def copy_and_rename(self):
        pos = self.pptx_dir('.')
        pptx_base_dir = self.pptx_dir[:pos]  # pptx_base_dir - directory of pptx file minus file extension '.pptx'

        zip_dir = pptx_base_dir + '_zip.zip'  # zip_dir - directory of converted zip file
        copyfile(self.pptx_dir, zip_dir)

        self.dest_zip_dir = self.zip_folder + zip_dir

    # Extracts zip-file to directory indicated in constructor
    def extract_zip_file(self):
        with ZipFile(self.dest_zip_dir, 'r') as zip_file:
            zip_file.extractall(self.extraction_folder)

    # Deletes .pptx and .zip files after they have been converted
    def delete_files(self):
        pass


# if __name__ == '__main__':
#     pptxToXml = PptxToXml('temp\\test_1.pptx')
#     pptxToXml.copy_and_rename()
#     pptxToXml.extract_zip_file()
