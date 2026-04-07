import os
import re

class CleanData:
    """
    Cleans OCR text file to extract amounts
    """

    def __init__(self, name):
        self.name = name

    def data_cleaner(self):
        txt_path = f"mid_file/{self.name}.txt"
        data = ""
        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                data = f.read()
        except FileNotFoundError:
            print("Text file not found for cleaning.")
            return None

        matches = re.findall(r"\d+[.,]\d{2}", data)
        amounts = [float(x.replace(',', '.')) for x in matches]

        return max(amounts) if amounts else None