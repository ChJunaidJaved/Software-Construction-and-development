
def get_input():
    name = input("Enter Student Name: ")
    marks1 = float(input("Enter English Marks: "))
    marks2 = float(input("Enter Math Marks: "))
    marks3 = float(input("Enter Computer Marks: "))
    return name, marks1, marks2, marks3


def calculate_total(marks1, marks2, marks3):
    return marks1 + marks2 + marks3


def calculate_percentage(total):
    return (total / 300) * 100


def calculate_grade(percentage):
    if percentage >= 80:
        return "A Grade"
    elif percentage >= 70:
        return "B Grade"
    elif percentage >= 60:
        return "C Grade"
    elif percentage >= 50:
        return "D Grade"
    else:
        return "Fail"


def print_result(name, total, percentage, grade):
    print("\n--- Student Result ---")
    print("Student Name:", name)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)


name, m1, m2, m3 = get_input()

total = calculate_total(m1, m2, m3)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

print_result(name, total, percentage, grade)