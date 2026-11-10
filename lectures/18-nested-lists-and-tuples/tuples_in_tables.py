def read_students(filepath):
    """Returns a list of (name, major, gpa, credits) tuples."""
    students = []

    try:
        with open(filepath, 'r') as students_file:
            students_file.readline()  # header

            for line in students_file:
                name, major, gpa, credits = line.strip().split(',')
                students.append((name, major, float(gpa), int(credits)))
    except FileNotFoundError:
        print(f"ERROR: Could not open file '{filepath}'")

    return students


def find_value(table, target):
    """Returns the (row, column) position of the first occurrence of target, or None if it is not there."""
    for row_idx in range(len(table)):
        for col_idx in range(len(table[row_idx])):
            if table[row_idx][col_idx] == target:
                return (row_idx, col_idx)

    return None


def main():
    students = read_students("students.csv")

    print(students[0])
    print(students[0][2])

    for name, major, gpa, credits in students:
        print(f"{name} ({major}): {gpa} GPA, {credits} credits")

    # Replacing a whole row is fine...
    students[0] = ("Emily", "MechE", 3.9, 17)
    print(students[0])

    # ...but editing a single value inside of a tuple is not
    # students[0][2] = 4.0  # TypeError: 'tuple' object does not support item assignment

    grades = [
        ["Student", "Midterm I", "Midterm II", "Final"],
        ["Edelgard", 91, 99, 89],
        ["Maelle", 74, 78, 100],
        ["Melinoë", 86, 81, 70],
        ["Hinako", 98, 96, 89]
    ]

    position = find_value(grades, 100)
    print(position)

    row, col = find_value(grades, "Hinako")
    print(f"Found at row {row}, column {col}")

    print(find_value(grades, 55))


main()
