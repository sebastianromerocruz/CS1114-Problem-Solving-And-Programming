QUIT_SIGNAL = "quit"

word = input("Enter a word: ")
last_word = word

while word != QUIT_SIGNAL:
    if word > last_word: last_word = word

    word = input("Enter a word: ")

print("Last word:", last_word)
