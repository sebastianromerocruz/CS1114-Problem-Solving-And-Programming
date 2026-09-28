SIZE = 5

for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print(row * col, end='\t')
    print()
