<h2 align=center>Review</h2>

<h1 align=center>Midterm 2: The Greenhouse Watering Log</h1>

[***Solutions***](SOLUTIONS.md)

These problems practice what Midterm 2 is about: **files**, **exceptions**, **lists**, and **tuples**. They all use the
same data file, [**`watering_log.txt`**](watering_log.txt), where a greenhouse keeps a record of every time a plant was
watered. Each entry is a line with three fields separated by commas:

```text
day,plant,ml
```

Here are the first lines of the file:

```csv
# Greenhouse watering log
# day,plant,ml
1,Pothos,200
1,Fern,150
2,Monstera,300
2,Pothos,180
```

The file is **not clean**. Lines that start with a `#` are comments, and are not entries. But further down there are also
lines where a number was replaced by something that is not a number. Your functions have to cope with that without
crashing.

For all of them, do not use dictionaries, sets, or list comprehensions. You do not need to write a `main()` unless a
problem asks for one. Try to write each answer on paper first, as you would in the exam.

### 1. `read_log(filename)`

Write a function that accepts a file name and returns a **list of tuples**, one per valid entry, in the form

```text
(day, plant, ml)
```

with `day` and `ml` as integers. Lines that start with a `#` are not entries. An entry is **not valid**, and must be
left out of the list, when `day` or `ml` cannot be converted to an `int`. This function does **not** deal with a missing
file.

```python
entries = read_log("watering_log.txt")

print(len(entries))
print(entries[0])
```

Output:

```text
10
(1, 'Pothos', 200)
```

<details>
<summary>Stuck? Hint</summary>

Which exception does `int()` raise when it is given text like `"lots"`? Once you catch it, what should the loop do with
that line?

</details>

### 2. `safe_read(filename)`

Write a function that calls `read_log()`, and that returns what it returns. If the file does not exist, it prints
`No log named <filename>` and returns an empty list instead.

```python
print(safe_read("missing.txt"))
```

Output:

```text
No log named missing.txt
[]
```

<details>
<summary>Stuck? Hint</summary>

Which exception does `open()` raise for a file that does not exist? Where, in the code of problem 1, would it be raised,
and where should it be caught?

</details>

### 3. `total_water(entries, plant)`

Write a function that accepts a list of entries as returned by problem 1 and the name of a plant, and returns the total
number of millilitres that plant has been given. If the plant does not appear, the total is `0`.

```python
print(total_water(entries, "Pothos"))
print(total_water(entries, "Rose"))
```

Output:

```text
580
0
```

<details>
<summary>Stuck? Hint</summary>

Each entry is a tuple with three elements. Can the `for`-loop give you each of them a name of its own?

</details>

### 4. `ranking(entries)`

Write a function that accepts a list of entries and returns a list of tuples `(total, plant)`, one per plant, that goes
from the plant that was given the most water to the one that was given the least. You are encouraged to reuse your
previous functions.

```python
print(ranking(entries))
```

Output:

```text
[(580, 'Pothos'), (550, 'Monstera'), (300, 'Fern'), (190, 'Basil'), (60, 'Aloe')]
```

<details>
<summary>Stuck? Hint</summary>

You need two things: the name of each plant **once**, and the total of each one. The tuples are `(total, plant)` and not
`(plant, total)` for a reason: when Python sorts a list of tuples, it compares their **first** elements first. Look at
the options of the list method `sort()`.

</details>

### 5. `write_summary(entries, filename)`

Write a function that accepts a list of entries and a file name, and **writes** a new file with one line per plant, in
**alphabetical order**, followed by a last line with the total number of millilitres.

```python
write_summary(entries, "summary.txt")
```

After running it, `summary.txt` contains:

```text
Aloe: 1 watering(s), 60 ml
Basil: 2 watering(s), 190 ml
Fern: 2 watering(s), 300 ml
Monstera: 2 watering(s), 550 ml
Pothos: 3 watering(s), 580 ml
Total: 1680 ml
```

<details>
<summary>Stuck? Hint</summary>

Build the list of names first, and sort it. Then, for each name, how many entries have that name? And what is the total
of the **whole** log, once the loop over the plants is over?

</details>

### 6. (Challenge) `split_at(entries, day)`

Write a function that accepts a list of entries and a day, and returns a tuple of two **new** lists: the entries from
**before** that day, and the entries from that day **onwards**. The list that was passed in must **not** change.

```python
before, after = split_at(entries, 4)

print(len(before), len(after))
print(before[-1])
print(after[0])
print(len(entries))
```

Output:

```text
5 5
(3, 'Basil', 100)
(4, 'Monstera', 250)
10
```

<details>
<summary>Stuck? Hint</summary>

A function can only `return` one value, but that value can be a tuple that holds two lists. How do you build two lists
in a single pass through the entries?

</details>
