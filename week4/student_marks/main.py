
from validation import validate_mark
from calculation import (
    calculate_total,
    calculate_average,
    calculate_grade,
)
from display import display_result


def get_student_marks():
    marks = []

    for i in range(3):
        while True:
            try:
                mark = float(
                    input(f"Enter marks for subject {i + 1}: ")
                )

                if validate_mark(mark):
                    marks.append(mark)
                    break

                print("Invalid marks. Enter a value from 0 to 100.")

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    return marks


def main():
    """Coordinate the student marks application."""
    name = input("Enter student name: ").strip()

    while not name:
        print("Student name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = get_student_marks()

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)


if __name__ == "__main__":
    main()