pets = ["cat", "dog", "bird", "dog"]

print(pets.pop(), pets)
print(pets.pop(0), pets)

pets = ["cat", "dog", "bird", "dog"]
pets.remove("dog")
print(pets)

pets.clear()
print(pets)

# removing while looping skips elements
numbers = [1, 2, 2, 3, 2]
for number in numbers:
    if number == 2:
        numbers.remove(number)
print(numbers)

# building a new list instead
numbers = [1, 2, 2, 3, 2]
kept = []
for number in numbers:
    if number != 2:
        kept.append(number)
print(kept)
