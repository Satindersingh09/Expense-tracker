'''
ocr.py takes an image as an input and extracts out text from it, furthermore, the text is stored in a mid_file text file. That text file is then imported by
main.py to extract out the expense amount from the bill.
'''

from PIL import Image
import pytesseract
import os

class DataExtractor:
    '''
    DataExtractor extracts data from an image through tesseract module
    '''
    
    def __init__(self, name):
        self.name = name
        if name.startswith("bills/"):
            self.image_path = name
        else:
            self.image_path = f"bills/{self.name}"

    def ocr(self):
        try:
            bill = Image.open(self.image_path)
            text = pytesseract.image_to_string(bill)
            
            output_filename = os.path.basename(self.name)
            with open(f"mid_file/{output_filename}.txt", 'w') as mid:
                mid.write(text)

        except FileNotFoundError:
            print(f"File not Found at: {self.image_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
        return "Bill Scanned Successfully!"

class Converter(DataExtractor):
    def __init__(self, name):
        super().__init__(name)
        filename_only = os.path.basename(self.name)
        self.new_name = filename_only.split('.')[0]
        self.png_path = f"bills/{self.new_name}.png"
    
    def convert_to_png(self):
        try:
            with Image.open(self.image_path) as img:
                img.save(self.png_path, 'PNG')
        except Exception as e:
            print(f'unable to convert: {e}')
        return "File Converted To png Successfully!"

if __name__ == "__main__":
    name = input("Enter image name: ")
    conv = Converter(name)
    print(conv.convert_to_png())
    
    extractor = DataExtractor(f"bills/{conv.new_name}.png")
    print(extractor.ocr())