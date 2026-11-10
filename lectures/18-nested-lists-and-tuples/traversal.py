grades = [
    ["Student", "Midterm I", "Midterm II", "Final"],
    ["Edelgard", 91, 99, 89],
    ["Maelle", 74, 78, 100],
    ["Melinoë", 86, 81, 70],
    ["Hinako", 98, 96, 89]
]

# Approach 1: loop through the elements themselves
total = 0
count = 0

for row in grades[1:]:
    for grade in row[1:]:
        total += grade
        count += 1

print(f"The average grade of the class was {total / count:.2f}")

# Approach 2: loop through the indices
total = 0
count = 0

for row_idx in range(1, len(grades)):
    for col_idx in range(1, len(grades[row_idx])):
        total += grades[row_idx][col_idx]
        count += 1

print(f"The average grade of the class was {total / count:.2f}")

# One average per student (one per row)
for row in grades[1:]:
    total = 0
    for grade in row[1:]:
        total += grade

    print(f"{row[0]}: {total / (len(row) - 1):.2f}")

# One average per exam (one per column). Here we do need the indices
for col_idx in range(1, len(grades[0])):
    total = 0
    for row_idx in range(1, len(grades)):
        total += grades[row_idx][col_idx]

    print(f"{grades[0][col_idx]}: {total / (len(grades) - 1):.2f}")

# Flattening: from a 2D list to a 1D list of grades
all_grades = []

for row in grades[1:]:
    for grade in row[1:]:
        all_grades.append(grade)

print(all_grades)
