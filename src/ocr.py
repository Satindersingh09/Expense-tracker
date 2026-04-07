from PIL import Image
import pytesseract
import os

class DataExtractor:
    """
    Extract text from an image and save to mid_file text file
    """

    def __init__(self, name):
        self.name = name
        self.image_path = f"bills/{self.name}" if not name.startswith("bills/") else name

        if not os.path.exists("mid_file"):
            os.makedirs("mid_file")

    def ocr(self):
        try:
            bill = Image.open(self.image_path)
            text = pytesseract.image_to_string(bill)

            output_filename = os.path.basename(self.name)
            with open(f"mid_file/{output_filename}.txt", 'w', encoding="utf-8") as mid:
                mid.write(text)

        except FileNotFoundError:
            print(f"File Not Found at: {self.image_path}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

        return "Bill Scanned Successfully!"


class Converter(DataExtractor):
    """
    Convert any image to PNG format inside bills folder
    """

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
            print(f"Unable to convert: {e}")
            return None
        return f"File Converted To png Successfully! Saved at {self.png_path}"


if __name__ == "__main__":
    name = input("Enter image name: ")
    conv = Converter(name)
    print(conv.convert_to_png())
    extractor = DataExtractor(f"bills/{conv.new_name}.png")
    print(extractor.ocr())