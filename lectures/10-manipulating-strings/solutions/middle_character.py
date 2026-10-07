word = input("Enter a word: ")

length = len(word)
middle = length // 2

if length % 2 == 1:
    print(word[middle])
else:
    print(word[middle - 1:middle + 1])
