grades = [87.0, 56.0, 100.0]

grades.append(91.5)
print(grades)

grades.insert(1, 72.5)
print(grades)

grades.extend([60.0, 45.5])
print(grades)

# append() vs extend() vs +
appended = [1, 2]
appended.append([3, 4])
print(appended)

extended = [1, 2]
extended.extend([3, 4])
print(extended)

added = [1, 2]
added = added + [3, 4]
print(added)

# a classic mistake: append() changes the list and returns None
mistake = [1, 2]
mistake = mistake.append(3)
print(mistake)
