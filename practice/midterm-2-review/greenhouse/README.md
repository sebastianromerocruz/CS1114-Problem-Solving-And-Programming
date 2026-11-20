<h2 align=center>Review</h2>

<h1 align=center>Midterm 2: Reading a Greenhouse Log</h1>

[***Solutions***](SOLUTIONS.md)

These problems practice what Midterm 2 is about: **files**, **exceptions**, **lists**, and **tuples**. They all use the
same data file, [**`greenhouse.txt`**](greenhouse.txt), which has the plants of a greenhouse, one per line, with four
fields separated by commas:

```text
plant,room,height_cm,days_since_water
```

Here are the first lines of the file:

```csv
plant,room,height_cm,days_since_water
Monstera,Living Room,120,3
Pothos,Kitchen,45,6
Snake Plant,Bedroom,60,12
Fern,Bathroom,30,2
Basil,Kitchen,25,1
```

The file is **not clean**. Further down it has a blank line, a line with a missing field, and lines where a number was
replaced by something that is not a number. Your functions have to cope with that without crashing.

For all of them, do not use dictionaries, sets, or list comprehensions. You do not need to write a `main()` unless a
problem asks for one. Try to write each answer on paper first, as you would in the exam.

### 1. `read_plants(filename)`

Write a function that accepts a file name and returns a **list of tuples**, one per valid plant, in the form

```text
(plant, room, height_cm, days_since_water)
```

with the two numbers as integers. The first line of the file is a header, and is not a plant.

A line is **not valid**, and must be left out of the list, when it does not have exactly four fields, or when either of
its numbers cannot be converted to an `int`. If the file cannot be opened, the function prints `Could not open <filename>`
and returns an empty list.

```python
plants = read_plants("greenhouse.txt")

print(len(plants))
print(plants[0])
print(read_plants("missing.txt"))
```

Output:

```text
9
('Monstera', 'Living Room', 120, 3)
Could not open missing.txt
[]
```

<details>
<summary>Stuck? Hint</summary>

There are **two** things that can go wrong, and they are handled in different ways. A missing file is an exception that
you handle around the call to `open()`. A line with the wrong number of fields is not an exception at all: it is a
question that you can ask with `len()`. And the number conversions are the part that can raise a `ValueError`. What
should the loop do with a line when that happens?

</details>

### 2. `tallest(plants)`

Write a function that accepts a list of plants as returned by problem 1, and returns the **tuple** of the tallest one.
If there is a tie, return the one that appears first. If the list is empty, return `None`.

```python
print(tallest(plants))
print(tallest([]))
```

Output:

```text
('Monstera', 'Living Room', 120, 3)
None
```

<details>
<summary>Stuck? Hint</summary>

Start by assuming that the first plant is the tallest. What do you need to do each time you see a plant that is taller
than the best one so far? And what must you check **before** looking at the first plant?

</details>

### 3. `rooms(plants)`

Write a function that accepts a list of plants and returns a list with the name of every room, **without repeats**, in
the order in which each room first appears.

```python
print(rooms(plants))
```

Output:

```text
['Living Room', 'Kitchen', 'Bedroom', 'Bathroom']
```

<details>
<summary>Stuck? Hint</summary>

You are building a new list as you go. Before adding a room to it, how can you know whether it is already there?

</details>

### 4. `thirsty(plants, limit)`

Write a function that accepts a list of plants and a number of days, and returns a list of tuples `(days, plant)` for
every plant that has gone **at least** `limit` days without water. The list must go from the plant that has waited the
longest to the one that has waited the least.

```python
print(thirsty(plants, 6))
print(thirsty(plants, 99))
```

Output:

```text
[(15, 'Aloe'), (12, 'Snake Plant'), (9, 'Mint'), (6, 'Pothos')]
[]
```

<details>
<summary>Stuck? Hint</summary>

The tuples are `(days, plant)` and not `(plant, days)` for a reason: when Python sorts a list of tuples, it compares
their **first** elements first. Look at the options of the list method `sort()`.

</details>

### 5. `write_report(plants, filename)`

Write a function that accepts a list of plants and a file name, and **writes** a new file with one line per room, in the
order given by problem 3. Each line has the room, the number of plants in it, and their average height with one
decimal. You are encouraged to reuse your previous functions.

```python
write_report(plants, "report.txt")
```

After running it, `report.txt` contains:

```text
Living Room: 3 plant(s), average height 70.0 cm
Kitchen: 3 plant(s), average height 30.7 cm
Bedroom: 2 plant(s), average height 39.0 cm
Bathroom: 1 plant(s), average height 30.0 cm
```

<details>
<summary>Stuck? Hint</summary>

For each room, you need two running totals: how many plants you have seen in it, and how tall they are all together. Both
start at zero, and both need to be reset for every new room. What do you do with them once you have gone through
all the plants?

</details>

### 6. (Challenge) `grown(plants, extra)`

Write a function that accepts a list of plants and a number of centimetres, and returns a **new** list in which every
plant is `extra` centimetres taller. The list that was passed in must **not** change.

```python
taller = grown(plants, 10)

print(taller[0])
print(plants[0])
```

Output:

```text
('Monstera', 'Living Room', 130, 3)
('Monstera', 'Living Room', 120, 3)
```

<details>
<summary>Stuck? Hint</summary>

Tuples cannot be changed once they are made, so you cannot write `plant[2] += extra`. What can you do instead, with
the four values that a tuple holds? And what would happen to the original list if you modified its contents in place
instead of building a new one?

</details>
