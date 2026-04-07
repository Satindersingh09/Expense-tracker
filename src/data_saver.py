import csv
import os

class SaveData:
    """
    Save extracted expense data to CSV
    """

    def __init__(self, name, expense, date):
        self.name = name
        self.expense = expense
        self.date = date
        self.csv_file = "database/saved_bills.csv"

        # Ensure database folder exists
        if not os.path.exists("database"):
            os.makedirs("database")

    def input_data(self):
        file_exists = os.path.exists(self.csv_file)

        with open(self.csv_file, 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["name", "expense", "date"])
            writer.writerow([self.name, self.expense, self.date])

    def check_data(self):
        # Check if this bill is already saved
        exists = False
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r', encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if self.name in row:
                        exists = True
                        break

        if exists:
            print("This bill is already uploaded")
        else:
            self.input_data()
            print("Data Saved Successfully!")