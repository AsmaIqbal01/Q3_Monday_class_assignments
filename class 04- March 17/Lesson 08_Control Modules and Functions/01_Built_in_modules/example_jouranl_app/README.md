🛠 Project: "Personal Daily Journal CLI App"
💡 What it does:
Lets you write daily journal entries

Automatically saves them to files with the current date

Can show previous entries

Uses built-in modules only (like os, datetime, sys, etc.)

🔧 Modules We'll Use:

Module	Purpose
os	Handle file paths & directories
datetime	Get current date
time	(Optional) Delay or timestamp logs
sys	Take input from command-line args
🚀 Step-by-Step Guide
✅ Step 1: Setup a Folder
Create a folder, e.g., journal_app/, and inside it create a file named:
journal.py

✅ Step 2: Basic Structure
Let’s write a base script to get the date and accept a journal entry.

python
Copy
Edit
# journal.py
import os
import datetime

def get_today_filename():
    today = datetime.date.today()
    return f"journal_{today}.txt"

def write_entry(entry):
    filename = get_today_filename()
    with open(filename, 'a') as file:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(f"[{time}] {entry}\n")

def read_entries():
    filename = get_today_filename()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print("No entry found for today.")

def main():
    print("Welcome to your Daily Journal!")
    print("1. Write new entry")
    print("2. Read today's entry")
    choice = input("Choose (1 or 2): ")

    if choice == "1":
        entry = input("Write your journal entry: ")
        write_entry(entry)
        print("✅ Entry saved!")
    elif choice == "2":
        print("📖 Today's Entries:")
        read_entries()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
✅ Step 3: Run It
From your terminal:

bash
Copy
Edit
python journal.py
It’ll:

Ask if you want to write or read

Save your entries in a file named journal_YYYY-MM-DD.txt

