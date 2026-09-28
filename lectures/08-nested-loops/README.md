<h2 align=center>Lecture VIII</h2>

<h1 align=center>Nested Loops</h1>

<h3 align=center>6 de Vendémiaire, de l'Année CCXXXV de la République</h3>

***Song of the day***: _[**Autumn Leaves**](https://youtu.be/Jw_siaIZewQ) performed by Asal Vaseghnia (2025)._

0. [**How Many Times Does This Print?**](#part-0-how-many-times-does-this-print)
1. [**Nesting**](#part-1-nesting)
2. [**Nested Loops**](#part-2-nested-loops)
3. [**The Multiplication Table**](#part-3-the-multiplication-table)
4. [**Practice Problems**](#part-4-practice-problems)

### Part 0: _How Many Times Does This Print?_

Before we get into today's topic, let's warm up. How many times does the string `"CS1114"` get printed in each of
the following snippets?

1.
```python
for i in range(5):
    print("CS1114")
```

2.
```python
for i in range(5):
    if i % 2 == 0:
        print("CS1114")
```

3.
```python
for i in range(3):
    print("CS1114 " * i)
```

Take a moment to trace through each one on paper before reading on.

---

1. The first snippet prints `"CS1114"` **5 times**—once for every value that `i` takes from `range(5)` (`0`, `1`, `2`,
`3`, `4`).
2. The second snippet only prints when `i` is even. Out of `0`, `1`, `2`, `3`, `4`, only `0`, `2`, and `4` satisfy
`i % 2 == 0`, so `"CS1114"` gets printed **3 times**.
3. The third snippet is the tricky one: `print()` is still only called **3 times** (once for `i = 0`, once for
`i = 1`, once for `i = 2`). It doesn't matter that the *string itself* contains zero, one, or two repetitions of
`"CS1114 "`—the loop still only executes its body 3 times. How many times a loop's body executes is a property of
the loop, not of what happens to get printed inside of it.

> **Essentially**: how many times a loop's body executes depends entirely on the code *inside* of it. We can put
> any kind of code inside of a loop, just like we can put any kind of code inside of a selection statement.

### Part 1: _Nesting_

Here's a program that checks whether `number` is divisible by 3, and if it is, counts up to it:

```python
number = int(input("Enter a number: "))

if number % 3 == 0:
    for i in range(number):
        print("CS1114")
else:
    print("Non-divisible")
```

Notice that we have a `for`-loop living *inside* of an `if`-statement. This is called ***nesting***; here, we have a
`for`-loop **nested** inside of an `if`-statement.

This should feel familiar—we've been putting loops inside of selection statements, and selection statements inside
of loops, for a while now without necessarily calling it that. Today, we take it one step further: nesting a loop
inside of *another loop*.

### Part 2: _Nested Loops_

> **Nested loops**: loops that are nested inside of an "outer" loop.

Take a look at the following [**example**](nested_print.py):

```python
# whatever is inside this loop runs 2 TIMES
for i in range(2):
    # whatever is inside this loop runs 3 TIMES
    for j in range(3):
        # so this line runs 2 * 3 = 6 TIMES
        print("CS1114")
```

Output:

```text
CS1114
CS1114
CS1114
CS1114
CS1114
CS1114
```

Let's trace through this line by line:

1. The **outer** `for`-loop starts, and assigns `i` a value of `0`.
2. The **inner** `for`-loop starts, and assigns `j` a value of `0`.
3. `print("CS1114")` executes.
4. The inner loop gives `j` a value of `1`, then `2`, printing `"CS1114"` each time—3 total prints so far.
5. The inner loop's condition becomes false (`j` would be `3`), so it ends. Control returns to the outer loop.
6. The outer loop gives `i` a value of `1`.
7. The inner loop starts over **completely**, running from `j = 0` to `j = 2` again—3 more prints (6 total).
8. The outer loop's condition becomes false (`i` would be `2`), so it ends.

In English:

> For every value that `i` takes from `range(2)`, run the **entire** inner `for`-loop from start to finish.

Because the inner loop restarts completely for every single iteration of the outer loop, the total number of times
the innermost line executes is the **product** of both ranges: `2 * 3 = 6`.

### Part 3: _The Multiplication Table_

Nested loops are most useful when we want to repeat an action across two dimensions—rows and columns, for instance.
Let's use one to build a multiplication table.

We want output that looks like this:

```text
1	2	3	4	5	
2	4	6	8	10	
3	6	9	12	15	
4	8	12	16	20	
5	10	15	20	25	
```

Here's [**how we'd build it**](multiplication_table.py):

```python
SIZE = 5

for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print(row * col, end='\t')
    print()
```

In English:

> For every value that `row` takes from `1` to `SIZE` (inclusive), and for every value that `col` takes from `1` to
> `SIZE` (inclusive), print `row * col` followed by a tab instead of a newline. Once the inner loop finishes an
> entire row, print a newline to move on to the next one.

Notice something important here: the second `print()` call is indented to line up with the **outer** `for`, not the
inner one. If we indented it one level deeper—so that it belonged to the inner loop instead—every single number
would print on its own line instead of five numbers per row. Indentation is doing a lot of work here; it's the only
thing telling Python which loop each line belongs to.

### Part 4: _Practice Problems_

Try tracing through each of the following by hand before running them.

(a)
```python
for i in range(4):
    for j in range(4):
        print(i * j, end=" ")
    print()
```

(b)
```python
for i in range(5):
    for j in range(i + 1, 5):
        print(i, j)
```

(c)
```python
for i in range(1, 10):
    if i % 2 == 0:
        for j in range(i, 10, 2):
            print(j, end=" ")
        print()
```

(d)
```python
for i in range(1, 10):
    if i % 2 == 0:
        for j in range(0, i, 2):
            print(j, end=" ")
        print()
```

---

Now try writing a full program from scratch:

1. Ask the user to input a positive integer, `high`.
2. Print every number from `1` to `high` (inclusive) that has ***more even digits than odd digits***.

For example, if `high = 30`, your program should print:

```text
Input a positive integer: 30
2
4
6
8
20
22
24
26
28
```

Here, `30` is **not** printed, because it contains one odd digit (`3`) and one even digit (`0`)—you need *strictly
more* even digits than odd ones.

---

<sub>**Previous: [Control-Flow Structures: The `for`-Loop](/lectures/07-for-loop)** || **Next: [Loop Review and Strings as Sequences](/lectures/09-loops-review-and-strings)**</sub>
