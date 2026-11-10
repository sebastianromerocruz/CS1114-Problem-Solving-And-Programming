from random import randint, uniform

LO, HI = 0.0, 10.0
MIN_SIZE, MAX_SIZE = 8, 25


def create_random_grid(num_rows, num_cols):
    grid = []

    for row_num in range(num_rows):
        row = []
        for col_num in range(num_cols):
            row.append(round(uniform(LO, HI), 1))

        grid.append(row)

    return grid


def get_grid_average(grid):
    total = 0
    count = 0

    for row in grid:
        for value in row:
            total += value
            count += 1

    return total / count


def main():
    num_rows = randint(MIN_SIZE, MAX_SIZE)
    num_cols = randint(MIN_SIZE, MAX_SIZE)
    data = create_random_grid(num_rows, num_cols)

    print(f"{num_rows} rows and {num_cols} columns")
    print(f"Average: {get_grid_average(data):.2f}")


main()
