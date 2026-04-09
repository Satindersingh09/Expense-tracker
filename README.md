# Expense-tracker
💸 Expense Tracker (Phase 1)

A simple Python-based Expense Tracker that automatically extracts spending data from bill images using OCR (Optical Character Recognition).

This project is currently in Phase 1, focusing on extracting expense amounts from bills and storing them in a structured format.

🚀 Features
📸 Extract text from bill images using OCR
🔄 Automatically convert images to PNG format
💰 Detect and extract total expense from text
🧹 Clean noisy OCR data using regex
💾 Save expenses into a CSV database
⚠️ Prevent duplicate bill entries
📁 Project Structure
Expense-tracker/
│
├── bills/                # Stores input bill images
├── mid_file/             # Temporary OCR text output
├── database/             # Stores CSV file
│   └── saved_bills.csv
│
├── src/
│   ├── ocr.py            # OCR + image conversion logic
│   ├── clean_data.py     # Extracts amount from text
│   └── data_saver.py     # Saves data to CSV
│
├── main.py               # Main entry point
├── README.md
└── .gitignore
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/Expense-tracker.git
cd Expense-tracker
2. Install dependencies
pip install pillow pytesseract
3. Install Tesseract OCR
Download from: https://github.com/tesseract-ocr/tesseract
Add it to your system PATH
▶️ How to Run
python main.py

Then enter the image name when prompted:

Enter the name of the image: bill.jpg
🔄 How It Works
User provides a bill image
Image is converted to PNG (if needed)
OCR extracts text from the image
Regex finds valid currency values
Highest value is assumed as total expense
Data is saved in saved_bills.csv
🧪 Example Output
File Converted To png Successfully!
Bill Scanned Successfully!
Extracted amount: 23.45
Data Saved Successfully!
⚠️ Error Handling
Handles missing files
Handles OCR failures
Prevents duplicate entries
Handles cases where no valid amount is found
🛠️ Technologies Used
Python 🐍
Tesseract OCR
Pillow (PIL)
CSV (for data storage)
Regex (for data cleaning)
🔮 Future Improvements (Phase 2+)
👥 Group expense tracking (roommates, friends)
💳 Track who paid and who owes whom
📊 Expense summaries & analytics
🖥️ GUI or Web App interface
🗄️ Database integration (SQLite / MongoDB)
🤖 Better OCR accuracy with preprocessing
