import zipfile
import os
from shutil import copyfile


class PptxToXml:
    # INPUTS:
    # pptx_loc - location of pptx file to be converted
    # save_dir - directory in which converted zip file is to be extracted
    def __init__(self, pptx_loc, save_dir=''):
        self.pptx_dir = pptx_loc  # 'self.pptx_dir' contains the directory location of the pptx file
        self.save_dir = save_dir
        self.zip_dir = None

    # Creates a new .zip file based on .pptx
    def CopyAndRename(self):
        pos = self.pptx_dir.index('.')
        pptx_name = self.pptx_dir[:pos]

        zip_dir = 'zip_' + pptx_name + '.zip'
        copyfile(self.pptx_dir, zip_dir)

        self.zip_dir = zip_dir

    # Extracts zip-file to directory indicated in constructor
    def ExtractZipFile(self):
        with zipfile.ZipFile(self.zip_dir, 'r') as zip_file:
            pass

    # Deletes .pptx and .zip files after they have been converted
    def DeleteFiles(self):
        pass


if __name__ == '__main__':
    pptxToXml = PptxToXml('test_1.pptx')
    pptxToXml.CopyAndRename()
