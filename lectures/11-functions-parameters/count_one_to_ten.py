# function DEFINITION (doesn't run any code by itself)
def count_one_to_ten():
    for number in range(1, 11):
        print(number, end=' ')


# function CALLS (each one runs the code inside the definition)
count_one_to_ten()
print()

count_one_to_ten()
print()

for time in range(5):
    count_one_to_ten()
    print()
