
def is_bonus_eligible(
    active,
    months_worked,
    performance_rating,
    disciplinary_action,
    attendance
):
    """Check whether an employee qualifies for a bonus."""

    meets_service_requirement = months_worked >= 12
    meets_performance_requirement = performance_rating >= 4
    has_clean_disciplinary_record = not disciplinary_action
    meets_attendance_requirement = attendance >= 90

    return (
        active
        and meets_service_requirement
        and meets_performance_requirement
        and has_clean_disciplinary_record
        and meets_attendance_requirement
    )


def main():
    active = True
    months_worked = 12
    performance_rating = 4
    disciplinary_action = False
    attendance = 90

    eligible = is_bonus_eligible(
        active,
        months_worked,
        performance_rating,
        disciplinary_action,
        attendance
    )

    if eligible:
        print("Employee is eligible for bonus.")
    else:
        print("Employee is not eligible for bonus.")


if __name__ == "__main__":
    main()