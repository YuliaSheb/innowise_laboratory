students = {}
avg_list = {}


def compute_avg():
    """
        Recalculates the average grade for all students.

            Description:
                Clears the `avg_list` dictionary and recalculates
                the average grade for each student who has at least
                one recorded grade.

            Side Effects:
                Replaces the contents of `avg_list`.
    """
    avg_list.clear()
    for name, grades in students.items():
        if grades:
            avg_list[name] = round((sum(grades) / len(grades)),2)


def add_student():
    """
        Adds a new student to the system.

            Description:
                Requests a student name from the user and validates it.
                A student can be added only if:
                    - The name is not empty.
                    - The name contains alphabetic characters only.
                    - The student does not already exist in the system.
    """
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if not name.isalpha():
        print("Name must contain only letters.")
        return

    if name in students:
        print("Student already exists.")
        return

    students[name] = []


def add_grades():
    """
        Adds one or more grades to an existing student.

            Description:
                Prompts for a student name and allows entering grades
                until the user types 'done'. Each grade must be an integer
                between 0 and 100.

            Side Effects:
                Updates the student's grade list.
                Calls compute_avg() to recalculate average grades.

            Errors:
                Prints a warning if:
                    - The student does not exist.
                    - A grade is outside the range 0–100.
                    - The user enters a non-numeric value.
    """
    name = input("Enter student name: ")
    if name not in students:
        print("Invalid input. Please enter an existing student name.")
    else:
        while True:
            grade = input("Enter a grade (or 'done' to finish): ")

            if grade.lower() == "done":
                break

            try:
                grade = int(grade)

                if not 0 <= grade <= 100:
                    raise ValueError("Grade must be between 0 and 100.")

                students[name].append(grade)

            except ValueError:
                print("Invalid input. Please enter a number from 0 to 100.")
                continue

    compute_avg()


def show_report():
    """
        Displays a complete report of all students and grade statistics.

            Output Includes:
                - Each student's average grade (or 'N/A' if none exists).
                - Maximum average grade.
                - Minimum average grade.
                - Overall average across all students with grades.

            Notes:
                If there are no students or no recorded grades,
                relevant messages are displayed instead of statistics.
    """
    print("--- Student Report ---")
    if not students:
        print("Student not found.")
    else:
        for name, grades in students.items():
            if name not in avg_list:
                avg_grade = "N/A"
            else:
                avg_grade = avg_list[name]
            print(f"{name}'s average grade is {avg_grade}.")
        print("-"*20)
        if avg_list:  # only if there are actual grades
            print("Max Average:", max(avg_list.values()))
            print("Min Average:", min(avg_list.values()))
            print("Overall Average:",
                  round(sum(avg_list.values()) / len(avg_list.values()), 2))
        else:
            print("No grades available to calculate statistics.")


def top_student():
    """
        Prints the student with the highest average grade.

            Description:
                Uses the built-in `max()` function with a lambda key
                to identify the student with the highest average.

            Output:
                Example:
                    "The student with the highest average is Alice with a grade of 95.5."

            Notes:
                If no averages are available, prints an appropriate message.
    """
    if avg_list:
        name, avg = max(avg_list.items(), key=lambda x: x[1])
        print(f"The student with the highest average is {name} with a grade of {avg}.")
    else:
        print("No average grades available.")


# Main program loop
while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        add_grades()
    elif choice == 3:
        show_report()
    elif choice == 4:
        top_student()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid input! Please enter a number from 1 to 5.")
