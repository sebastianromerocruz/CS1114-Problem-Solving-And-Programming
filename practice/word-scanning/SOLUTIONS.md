<h2 align=center>Review Solutions</h2>

<h1 align=center>Scanning Strings For Words</h1>

### 1. Word Counter

```python
text = input("Text: ")

word_count = 0
previous_is_letter = False

for character in text:
    if character.isalpha() and not previous_is_letter:
        word_count += 1

    previous_is_letter = character.isalpha()

print("Word count:", word_count)
```

The variable `previous_is_letter` is what lets the loop "remember" what the last character was. A word starts exactly
when a letter shows up and the previous character wasn't one.

### 2. Acronym

```python
text = input("Text: ")

acronym = ""
previous_is_letter = False

for character in text:
    if character.isalpha() and not previous_is_letter:
        acronym += character.upper()

    previous_is_letter = character.isalpha()

print("Acronym:", acronym)
```

### 3. Word Lengths

```python
text = input("Text: ")

length = 0

for character in text:
    if character.isalpha():
        length += 1
    elif length > 0:
        print(length)
        length = 0

if length > 0:
    print(length)
```

The `if` after the loop handles a text that ends with a letter: no non-letter ever comes along to tell the loop that
the last word is over, so we have to print it ourselves.

### 4. (Challenge) Longest Word

```python
text = input("Text: ")

length = 0
longest = 0

for character in text:
    if character.isalpha():
        length += 1
    else:
        if length > longest:
            longest = length

        length = 0

if length > longest:
    longest = length

print("Longest word:", longest)
```

This is Problem 3 with a comparison in place of a `print()`. As there, a text that ends with a letter never triggers
the `else`, so the last word has to be checked after the loop.
