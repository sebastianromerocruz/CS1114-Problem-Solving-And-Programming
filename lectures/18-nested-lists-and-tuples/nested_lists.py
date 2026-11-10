grades = [
    ["Student", "Midterm I", "Midterm II", "Final"],
    ["Edelgard", 91, 99, 89],
    ["Maelle", 74, 78, 100],
    ["Melinoë", 86, 81, 70],
    ["Hinako", 98, 96, 89]
]

# How big is the table?
print(len(grades))
print(len(grades[0]))

# One index gives us a row; two indices give us a single value
print(grades[1])
print(grades[1][3])
print(grades[0][2])
print(grades[2][0])

# Changing a single value in the table
grades[2][3] = 95
print(grades[2])

# Slicing gives us a list of rows
print(grades[1:3])
