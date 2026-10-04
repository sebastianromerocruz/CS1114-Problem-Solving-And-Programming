VOWELS = "aeiouAEIOU"

user_string = input("Enter a string: ")

vowel_count = 0

for character in user_string:
    if character in VOWELS:
        vowel_count += 1

print("Vowel count:", vowel_count)
