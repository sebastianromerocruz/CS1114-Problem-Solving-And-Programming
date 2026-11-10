FINAL_IDX = 3


def get_column(table, col_idx):
    """Returns a list with the value at position col_idx of every row in table."""
    column = []

    for row in table:
        column.append(row[col_idx])

    return column


def find_value(table, target):
    """Returns the (row, column) position of the first occurrence of target, or None if it is not there."""
    for row_idx in range(len(table)):
        for col_idx in range(len(table[row_idx])):
            if table[row_idx][col_idx] == target:
                return (row_idx, col_idx)

    return None


def main():
    grades = [
        ["Edelgard", 91, 99, 89],
        ["Maelle", 74, 78, 100],
        ["Melinoë", 86, 81, 70],
        ["Hinako", 98, 96, 89]
    ]

    finals = get_column(grades, FINAL_IDX)
    print(finals)
    print(f"The highest final grade was {max(finals)}")

    row_idx, col_idx = find_value(grades, max(finals))
    print(f"{grades[row_idx][0]} earned it")


main()
