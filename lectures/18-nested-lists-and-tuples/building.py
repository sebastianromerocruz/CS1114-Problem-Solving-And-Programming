from random import uniform

LO, HI = 0.0, 10.0
SIZE = 5

# Build the table one row at a time
data = []

for row_num in range(SIZE):
    row = []
    for col_num in range(SIZE):
        row.append(round(uniform(LO, HI), 1))

    data.append(row)

print(data)

# A common mistake
print([0] * 3)

bad_grid = [[0] * 3] * 3
bad_grid[0][0] = 1
print(bad_grid)

# The fix: make a brand new row on every pass of the loop
good_grid = []

for row_num in range(3):
    good_grid.append([0] * 3)

good_grid[0][0] = 1
print(good_grid)
