<h2 align=center>Review</h2>

<h1 align=center>Scanning Strings For Words</h1>

[***Solutions***](SOLUTIONS.md)

For these problems, do not use `split()`.

For all of them, a **letter** is any of `a`-`z` or `A`-`Z`, and a **word** is a run of consecutive letters. Words are
separated by one or more non-letters (spaces, digits, punctuation—anything). The input may start or end with
non-letters.

### 1. Word Counter

Write a program that asks the user for a string, and prints how many words it contains.

```text
Text: to be, or not to be: that is the question
Word count: 10
```

```text
Text:   hello,   world  
Word count: 2
```

```text
Text: route66 is-open 24/7!
Word count: 3
```

<details>
<summary>Stuck? Hint</summary>

A word _starts_ whenever you see a letter and the character right before it was **not** a letter. What do you need to
remember from the previous step of your loop to know that?

</details>

### 2. Acronym

Write a program that asks the user for a string, and prints a string made of the **first letter** of every word,
in uppercase, with nothing in between.

```text
Text: self-contained underwater breathing apparatus
Acronym: SCUBA
```

```text
Text:   portable   NETWORK--graphics!! 
Acronym: PNG
```

<details>
<summary>Stuck? Hint</summary>

This is Problem 1 again, except that instead of adding `1` each time a word starts, you add the character that
started it to a result string.

</details>

### 3. Word Lengths

Write a program that asks the user for a string, and prints the **length of every word on its own line**, in the order
that the words appear.

```text
Text: no pain, no gain
2
4
2
4
```

```text
Text: ...up, 4 the win
2
3
3
```

Make sure that your program also works when the text **ends with a letter**, as in both examples above, and when it
**ends with something else**:

```text
Text: wow!!!
3
```

<details>
<summary>Stuck? Hint</summary>

Keep a counter for the length of the word you are currently inside of. What should happen to it when you see a letter?
What should happen when you see a non-letter? And what is still waiting to be printed when your loop finishes?

</details>

### 4. (Challenge) Longest Word

Write a program that asks the user for a string, and prints the length of its **longest** word.

```text
Text: to be, or not to be: that is the question
Longest word: 8
```

```text
Text: a-b c
Longest word: 1
```

<details>
<summary>Stuck? Hint</summary>

You already know how to keep track of the length of the word you are currently inside of (Problem 3). What do you need
to compare that length against each time a word finishes? And what happens to the very last word of the text?

</details>
