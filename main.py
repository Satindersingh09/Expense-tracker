#This main.py marks the beginning of the backend brain of "kngaal-khata"

from src import ocr

name = input("Enter the name of the image (with extension) : ")
extension = name.split('.')


if extension[1] != 'png':
    converter = ocr.Converter(name)
    print(converter.convert_to_png())
    name = f"{extension[0]}.png"
    


extractor = ocr.DataExtractor(name)
print(extractor.ocr())