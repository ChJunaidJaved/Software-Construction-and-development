
def display_result(name, total, average, grade):
    print("\n" + "=" * 35)
    print("          STUDENT RESULT")
    print("=" * 35)
    print(f"Student Name : {name}")
    print(f"Total Marks  : {total:g} / 300")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")
    print("=" * 35)