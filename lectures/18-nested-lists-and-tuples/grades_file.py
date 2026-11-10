def read_grades(filepath):
    """Returns the header (a list of strings) and the rows (a list of lists) of a grades file."""
    header = []
    rows = []

    try:
        with open(filepath, 'r') as grades_file:
            header = grades_file.readline().strip().split(',')

            for line in grades_file:
                name, midterm_1, midterm_2, final = line.strip().split(',')

                # The name stays a string, and the grades become numbers
                rows.append([name, int(midterm_1), int(midterm_2), int(final)])
    except FileNotFoundError:
        print(f"ERROR: Could not open file '{filepath}'")

    return header, rows


def write_averages(rows, report_filepath):
    with open(report_filepath, 'w') as report_file:
        print("Student,Average", file=report_file)

        for row in rows:
            total = 0
            for grade in row[1:]:
                total += grade

            print(row[0], round(total / (len(row) - 1), 1), sep=',', file=report_file)


def main():
    header, rows = read_grades("grades.csv")

    print(header)
    print(rows)

    write_averages(rows, "averages.csv")


main()
