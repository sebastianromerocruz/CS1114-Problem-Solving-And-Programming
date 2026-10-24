<h2 align=center>Review</h2>

<h1 align=center>Midterm 1: Expressions, Tracing, Strings, and Functions</h1>

[***Solutions***](SOLUTIONS.md)

These problems are in the same format as the written part of the midterm: you evaluate or trace the code **by hand**,
and write down what it produces. Don't run the code until you have written down your answer.

Remember the rules from the exam:

- If an error occurs, write `ERROR`.
- If nothing is printed, write `NO OUTPUT`.
- Treat each code segment as independent from the others, unless the question says otherwise.

### 1. Expressions

Use the following variables to evaluate each expression, following the order of operations. If an expression would cause
an error, write `ERROR`. Pay attention to the **type** of each result (`7` is not the same as `7.0`, and `7` is not the
same as `"7"`).

```python
hp = 50
mana = 8
atk = 12
armor = 5
gold = 100
level = 3
is_alive = True
is_stunned = False
```

| **Expression**                                                  | **Result** |
|-----------------------------------------------------------------|------------|
| `atk // armor + level ** 2`                                     |            |
| `(gold - hp) % mana * 2 + armor`                                |            |
| `gold / mana`                                                   |            |
| `(hp > gold // 2) and not is_stunned or level < 0`              |            |
| `is_alive and is_stunned or not is_stunned and level >= 3`      |            |
| `armor + level * 2 ** 3 - 10 // 4`                              |            |
| `gold + "g"`                                                    |            |
| `"hp" * level + str(armor)`                                     |            |
| `7 // 2 * 2.0`                                                  |            |

### 2. Tracing Loops

What is printed by each of the following code segments?

**(a)**

```python
n = 30
count = 0
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        count += 1
print(count)
```

**(b)**

```python
num = 4096
var = 0
while num > 0:
    var = var * 10 + num % 10
    num //= 10
print(var)
```

**(c)**

```python
var = 0
for i in range(1, 4):
    for j in range(i, 4):
        if (i + j) % 2 == 1:
            var += i * j
print(var)
```

**(d)**

```python
count = 0
for n in range(1, 30):
    found = False
    k = 1
    while k * k <= n and not found:
        if k * k == n:
            found = True
        k += 1
    if found:
        count += 1
print(count)
```

**(e)**

```python
for step in range(5, 2):
    total = step
    print(total)
```

**(f)**

```python
for step in range(5, 2):
    total = step
print(total)
```

### 3. Strings

Evaluate each of the `print` statements below. Treat the whole code segment as **one continuous program**.

```python
text = "  Pixel@rt, 8-bit & 16-bit!  "

cleaned = text.strip().replace("@", "a").replace("&", "and")
cleaned = cleaned.replace("!", "?").replace("-", " ")
```

| **Statement**                                    | **Output** |
|--------------------------------------------------|------------|
| `print(cleaned)`                                 |            |
| `print(len(cleaned))`                            |            |
| `print(f"{cleaned.find('bit'):.2f}")`            |            |
| `print(cleaned[2:12:2])`                         |            |
| `print(cleaned.lower().count("it"))`             |            |
| `print(cleaned[-1:-5:-1])`                       |            |
| `print(cleaned.replace(" ", "").isalpha())`      |            |
| `print(cleaned[40])`                             |            |

### 4. Functions

Given the following code segment, what does each statement below print? Treat the whole code segment as **one
continuous program**.

```python
score = 30

def boost(points, bonus=10):
    return points + bonus

def grade(points):
    if points >= 50:
        return "A"
    elif points >= 40:
        return "B"

def announce(name):
    print("Hello,", name)

def double(value):
    value *= 2
    return value
```

| **Statement**                          | **Output** |
|----------------------------------------|------------|
| `print(boost(5))`                      |            |
| `print(boost(score, bonus=1))`         |            |
| `print(grade(boost(30)))`              |            |
| `print(grade(boost(10)))`              |            |
| `print(announce("Ada"))`               |            |
| `print(double(score))`                 |            |
| `print(score)`                         |            |
| `print(boost())`                       |            |
| `print(boost(double(3), double(4)))`   |            |
