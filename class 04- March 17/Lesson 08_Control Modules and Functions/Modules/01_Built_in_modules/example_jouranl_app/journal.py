#journal ----a small project using built in module
import os
import datetime

def get_today_filename():
    today = datetime.date.today()
    return f"journal_{today}.txt"

def write_entry(entry):
    filename = get_today_filename()
    with open(filename,'a') as file:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(f"[{time}{entry}\n")

def read_entries():
    filename=get_today_filename()
    if os.path.exists(filename):
        with open(filename,'r') as file:
            print(file.read())
    else:
        print("No entry found for today.")

def main():
    print("Welcome to your daily Journal!")
    print("1. Write new entry")
    print("2. Read today's entry")
    choice = input("Choose (1 or 2) : ")

    if choice == "1":
        entry = input("Write your journal entry: ")
        write_entry(entry)
        print("✅ Entry saved! ")
    elif choice == '2':
        print("📖 Today's Entries: ")
        read_entries()
    else:
        print("❌ Invalid choice.") 

if __name__ == '__main__':
    main()