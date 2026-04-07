# main.py - Expense Tracker

from src import ocr
from src.clean_data import CleanData
from src.data_saver import SaveData

import os
import datetime

def main():
    name = input("Enter the name of the image (with extension): ")
    base, ext = os.path.splitext(name)

    if not os.path.exists("bills"):
        os.makedirs("bills")

    # Convert to PNG if not already
    if ext.lower() != '.png':
        converter = ocr.Converter(name)
        print(converter.convert_to_png())
        name = f"bills/{converter.new_name}.png"
    else:
        name = f"bills/{name}" if not name.startswith("bills/") else name

    extractor = ocr.DataExtractor(name)
    print(extractor.ocr())

    cleaner = CleanData(os.path.basename(name))
    amount = cleaner.data_cleaner()

    if amount is None:
        print("No valid amount found")
        return

    print(f"Extracted amount: {amount}")

    date = str(datetime.date.today())
    saver = SaveData(os.path.basename(name), amount, date)
    saver.check_data()


if __name__ == "__main__":
    main()