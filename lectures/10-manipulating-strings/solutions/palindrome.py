word = input("Enter a word: ")

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
