<h2 align=center>Review</h2>

<h1 align=center>Midterm 2: Lists, Tuples, Exceptions, and Memory</h1>

<!--[***Solutions***](SOLUTIONS.md)-->

These problems are in the same format as the written part of the midterm: you evaluate or trace the code **by hand**,
and write down what it produces, or draw what memory looks like. Don't run the code until you have written down your
answer.

Remember the rules from the exam:

- If an error occurs, write `ERROR`.
- If nothing is printed, write `NO OUTPUT`.
- Treat each code segment as independent from the others, unless the question says otherwise.

There is also a [**programming review**](greenhouse/) for this midterm.

### 1. Lists and Tuples

What is printed by each of the following code segments?

**(a)**

```python
marks = [72, 95, 88]
ordered = marks.sort()
print(ordered)
print(marks)
```

**(b)**

```python
def add_bonus(scores):
    scores = scores + [100]
    return scores

def add_bonus_inplace(scores):
    scores.append(100)

grades = [90]
result = add_bonus(grades)
add_bonus_inplace(grades)
add_bonus_inplace(grades)
print(grades, result)
```

**(c)**

```python
record = ("Ada", [90, 85])
record[1].append(70)
record[1] = [100]
print(record)
```

**(d)**

```python
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[1:5:2], letters[::-2], letters[-3:])
```

### 2. Exceptions

What is printed by each of the following code segments? Pay attention to **when** each `print` happens, and to which
`except` (if any) catches each exception.

**(a)**

```python
def ratio(total, count):
    try:
        return total / count
    except ZeroDivisionError:
        return -1
    finally:
        print("done", end=" ")

print(ratio(9, 3), ratio(5, 0))
```

**(b)**

```python
values = [2, "3", 4]
total = 0

try:
    for value in values:
        total += value
except ValueError:
    print("bad value")

print(total)
```

**(c)**

```python
for text in ["8", "0", "-"]:
    try:
        number = 24 // int(text)
    except ZeroDivisionError:
        print("zero", end=" ")
    except ValueError:
        print("text", end=" ")
    else:
        print(number, end=" ")

print("end")
```

**(d)**

```python
def check(age):
    if age < 0:
        raise ValueError("negative")
    return age

for age in [5, -2, 7]:
    try:
        print(check(age), end=" ")
    except ValueError:
        print("bad", end=" ")
```

### 3. Aliases and Copies

Evaluate each of the `print` statements below. Treat the whole code segment, from the top down, as **one continuous
program**: each statement runs after all of the ones before it.

```python
import copy

team = [["Ada", 90], ["Bo", 80]]
alias = team
shallow = team.copy()
deep = copy.deepcopy(team)
```

| **Statements**                                                                  | **Output** |
|---------------------------------------------------------------------------------|------------|
| `alias.append(["Cy", 70])`<br>`print(len(team), len(shallow))`                  |            |
| `shallow[0][1] = 95`<br>`print(team[0][1], deep[0][1])`                         |            |
| `team[1][0] = "Bob"`<br>`print(shallow[1][0], deep[1][0])`                      |            |

### 4. Memory Maps

Draw the **memory map** after the last line has run: the namespace with its names,
every list, and every `int` object, with an arrow for every reference. Then answer the question.

```python
a = [1, 2]
b = a
c = [a, a]
b.append(3)
```

How many **list objects** exist? What does `print(c)` show?
