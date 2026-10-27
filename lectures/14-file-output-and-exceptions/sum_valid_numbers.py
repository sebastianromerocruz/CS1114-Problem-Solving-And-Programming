def sum_valid_numbers(filepath):
    total = 0.0
    skipped = 0

    try:
        file = open(filepath, 'r')
    except FileNotFoundError:
        print(f"WARNING: There is no file called '{filepath}'.")
        return None

    for line in file:
        try:
            number = float(line.strip())
        except ValueError:
            skipped += 1
        else:
            total += number

    file.close()

    print(f"Skipped {skipped} invalid line(s).")
    return total


def main():
    print(sum_valid_numbers("grades_with_errors.txt"))
    print(sum_valid_numbers("grades_with_errors.csv"))


main()
