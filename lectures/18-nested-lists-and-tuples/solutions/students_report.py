NAME_IDX, GPA_IDX, CREDITS_IDX = 0, 2, 3
MIN_GPA = 3.5
MIN_CREDITS = 32


def read_students(filepath):
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


def get_names_above_gpa(students, min_gpa):
    names = []

    for student in students:
        if student[GPA_IDX] > min_gpa:
            names.append(student[NAME_IDX])

    return names


def get_names_above_credits(students, min_credits):
    names = []

    for student in students:
        if student[CREDITS_IDX] > min_credits:
            names.append(student[NAME_IDX])

    return names


def main():
    students = read_students("../students.csv")

    high_gpa = get_names_above_gpa(students, MIN_GPA)
    print(f"{len(high_gpa)} students have a GPA above {MIN_GPA}: {high_gpa}")

    high_credits = get_names_above_credits(students, MIN_CREDITS)
    print(f"{len(high_credits)} students have more than {MIN_CREDITS} credits: {high_credits}")


main()
