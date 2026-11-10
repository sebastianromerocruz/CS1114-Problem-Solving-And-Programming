from random import uniform

LO, HI = 0.0, 10.0
SIZE = 5


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
    data = create_random_grid(SIZE, SIZE)

    for row in data:
        print(row)

    print(f"Average: {get_grid_average(data):.2f}")


main()
