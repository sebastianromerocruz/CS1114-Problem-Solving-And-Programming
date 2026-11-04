letters = ["b", "a", "c", "a"]

print(letters.index("a"))
print(letters.count("a"))

letters.sort()
print(letters)

letters.sort(reverse=True)
print(letters)

letters.reverse()
print(letters)

# sort() changes the list and returns None; sorted() returns a new list
numbers = [3, 1, 2]
print(numbers.sort())
print(numbers)

numbers = [3, 1, 2]
print(sorted(numbers), numbers)

print(sum(numbers), min(numbers), max(numbers), len(numbers))
