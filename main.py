# Student Grade Tracker
# Author: Atharv Das
# Course: Python Essentials - Mini Project

FILENAME = "grades.txt"


def calculate_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def load_data():
    records = {}
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comment lines (starting with #)
                if not line or line.startswith("#"):
                    continue

                parts = line.split(",")

                # Ensure line contains roll, name, and marks
                if len(parts) >= 3:
                    roll = parts[0].strip()
                    name = parts[1].strip()
                    try:
                        marks = float(parts[2].strip())
                        records[roll] = {"name": name, "marks": marks}
                    except ValueError:
                        # Skip if marks aren't a valid numeric value
                        continue
    except FileNotFoundError:
        # File will be created automatically on first save
        pass

    return records


def save_data(records):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for roll, info in records.items():
            f.write(f"{roll},{info['name']},{info['marks']}\n")


def add_student(records):
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    if roll in records:
        print("A student with this roll number already exists!")
        return

    name = input("Enter Student Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter Marks (0 - 100): "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter a valid number for marks.")
        return

    records[roll] = {"name": name, "marks": marks}
    save_data(records)
    print(f"Record for {name} saved successfully!")


def view_all_students(records):
    print("\n--- All Student Records ---")
    if not records:
        print("No student records found.")
        return

    print("-" * 55)
    print(f"{'Roll No':<10} | {'Name':<20} | {'Marks':<8} | {'Grade'}")
    print("-" * 55)

    for roll, info in records.items():
        grade = calculate_letter_grade(info["marks"])
        print(f"{roll:<10} | {info['name']:<20} | {info['marks']:<8.1f} | {grade}")

    print("-" * 55)


def search_student(records):
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ").strip()

    if roll in records:
        info = records[roll]
        grade = calculate_letter_grade(info["marks"])
        print("\nFound Student Details:")
        print(f"Roll Number : {roll}")
        print(f"Name        : {info['name']}")
        print(f"Score       : {info['marks']}")
        print(f"Grade       : {grade}")
    else:
        print("No student found with that roll number.")


def show_statistics(records):
    print("\n--- Class Statistics ---")
    if not records:
        print("No data available to calculate statistics.")
        return

    scores = [info["marks"] for info in records.values()]
    total_students = len(scores)
    average_score = sum(scores) / total_students
    highest_score = max(scores)
    lowest_score = min(scores)

    print(f"Total Students : {total_students}")
    print(f"Class Average  : {average_score:.2f}")
    print(f"Highest Score  : {highest_score:.1f}")
    print(f"Lowest Score   : {lowest_score:.1f}")


def main():
    records = load_data()

    while True:
        print("\n==============================")
        print("    STUDENT GRADE TRACKER      ")
        print("==============================")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Search Student by Roll No")
        print("4. View Class Statistics")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_all_students(records)
        elif choice == "3":
            search_student(records)
        elif choice == "4":
            show_statistics(records)
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
