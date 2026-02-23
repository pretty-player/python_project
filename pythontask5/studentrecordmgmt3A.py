import os

FILE_NAME = "students.txt"

def add_student():
    """Appends new student data to the file without overwriting."""
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    marks = input("Enter Marks: ")
    
    # Mode 'a' opens the file for appending; it creates the file if it doesn't exist.
    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Record added successfully!")

def display_all():
    """Reads and prints all records from the file."""
    if not os.path.exists(FILE_NAME):
        print("No records found. The file is empty.")
        return

    print("\n--- Student Records ---")
    print(f"{'Roll No':<10} {'Name':<20} {'Marks':<5}")
    print("-" * 40)
    
    # Mode 'r' opens the file for reading.
    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"{roll:<10} {name:<20} {marks:<5}")

def search_student():
    """Searches for a specific roll number in the file."""
    search_roll = input("Enter Roll Number to search: ")
    found = False
    
    if not os.path.exists(FILE_NAME):
        print("File not found.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == search_roll:
                print(f"\nRecord Found!\nName: {name}\nRoll No: {roll}\nMarks: {marks}")
                found = True
                break
    
    if not found:
        print("Student record not found.")

def main():
    while True:
        print("\n1. Add Student\n2. Display All\n3. Search Student\n4. Exit")
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_all()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()