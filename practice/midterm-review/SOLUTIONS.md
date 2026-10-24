<h2 align=center>Review Solutions</h2>

<h1 align=center>Midterm 1: Expressions, Tracing, Strings, and Functions</h1>

### 1. Expressions

| **Expression**                                                  | **Result** | **Why**                                                                                       |
|-----------------------------------------------------------------|------------|-----------------------------------------------------------------------------------------------|
| `atk // armor + level ** 2`                                     | `11`       | `**` first (`9`), then `//` (`2`), then `+`.                                                  |
| `(gold - hp) % mana * 2 + armor`                                | `9`        | `50 % 8` is `2`; `%` and `*` are evaluated left to right: `2 * 2 + 5`.                        |
| `gold / mana`                                                   | `12.5`     | `/` always gives a `float`.                                                                   |
| `(hp > gold // 2) and not is_stunned or level < 0`              | `False`    | `50 > 50` is `False`, so the `and` is `False`; `level < 0` is `False` too.                    |
| `is_alive and is_stunned or not is_stunned and level >= 3`      | `True`     | `and` binds tighter than `or`: `(True and False) or (True and True)`.                         |
| `armor + level * 2 ** 3 - 10 // 4`                              | `27`       | `2 ** 3` is `8`; `3 * 8` is `24`; `10 // 4` is `2`; so `5 + 24 - 2`.                          |
| `gold + "g"`                                                    | `ERROR`    | You cannot add an `int` and a `str`.                                                          |
| `"hp" * level + str(armor)`                                     | `"hphphp5"` | `"hp" * 3` repeats the string; `str(armor)` makes `"5"`; `+` concatenates.                   |
| `7 // 2 * 2.0`                                                  | `6.0`      | `7 // 2` is `3`; `3 * 2.0` is a `float`.                                                      |

### 2. Tracing Loops

**(a)** `14`

The loop counts the numbers from 1 to 30 that are multiples of 3 or 5. There are ten multiples of 3 and six of 5, but
`15` and `30` are in both groups, so we only count them once: `10 + 6 - 2 = 14`.

**(b)** `6904`

The loop peels off the last digit of `num` each turn and appends it to `var`, so it **reverses** the digits:

| `num` at the start | last digit | `var` after |
|--------------------|------------|-------------|
| `4096`             | `6`        | `6`         |
| `409`              | `9`        | `69`        |
| `40`               | `0`        | `690`       |
| `4`                | `4`        | `6904`      |

**(c)** `8`

Only pairs where `i + j` is odd are counted. The pairs with `j >= i` are `(1,1)`, `(1,2)`, `(1,3)`, `(2,2)`, `(2,3)`,
`(3,3)`; only `(1,2)` and `(2,3)` have an odd sum, so `var = 1 * 2 + 2 * 3 = 8`.

**(d)** `5`

For each `n`, the `while`-loop looks for a `k` such that `k * k == n`. So `found` ends up `True` exactly when `n` is a
perfect square: `1`, `4`, `9`, `16`, and `25`.

**(e)** `NO OUTPUT`

`range(5, 2)` is empty (it counts **up** from 5, and 5 is already past 2), so the body never runs.

**(f)** `ERROR`

Same empty loop, but now the `print` is outside of it. Since the body never ran, the variable `total` was never created,
so the `print` tries to use a variable that doesn't exist (a `NameError`).

### 3. Strings

After the cleaning steps, `cleaned` is `"Pixelart, 8 bit and 16 bit?"`. Here are its indices, which are worth writing
out on your scrap paper during the exam:

```text
P  i  x  e  l  a  r  t  ,     8     b  i  t     a  n  d     1  6     b  i  t  ?
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

| **Statement**                                    | **Output**                     | **Why**                                                                                    |
|--------------------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------|
| `print(cleaned)`                                 | `Pixelart, 8 bit and 16 bit?`  | `strip()` removes the outer spaces, and each `replace()` swaps one piece.                  |
| `print(len(cleaned))`                            | `27`                           | Indices `0` through `26`.                                                                  |
| `print(f"{cleaned.find('bit'):.2f}")`            | `12.00`                        | `find()` gives the **first** `"bit"`, at index `12`; `.2f` formats the `int` with 2 decimals. |
| `print(cleaned[2:12:2])`                         | `xlr,8`                        | Indices `2, 4, 6, 8, 10`.                                                                  |
| `print(cleaned.lower().count("it"))`             | `2`                            | Once in each `"bit"`.                                                                      |
| `print(cleaned[-1:-5:-1])`                       | `?tib`                         | Walks backwards from the last character: indices `26, 25, 24, 23`.                         |
| `print(cleaned.replace(" ", "").isalpha())`      | `False`                        | Spaces are gone, but the digits, the comma, and the `?` are still not letters.             |
| `print(cleaned[40])`                             | `ERROR`                        | Index `40` doesn't exist (the last one is `26`).                                           |

### 4. Functions

| **Statement**                          | **Output**             | **Why**                                                                                     |
|----------------------------------------|------------------------|---------------------------------------------------------------------------------------------|
| `print(boost(5))`                      | `15`                   | `bonus` uses its default, `10`.                                                             |
| `print(boost(score, bonus=1))`         | `31`                   | `30 + 1`.                                                                                   |
| `print(grade(boost(30)))`              | `B`                    | `boost(30)` is `40`, which is not `>= 50` but is `>= 40`.                                   |
| `print(grade(boost(10)))`              | `None`                 | `boost(10)` is `20`; neither condition is true, so `grade()` never reaches a `return`.      |
| `print(announce("Ada"))`               | `Hello, Ada` then `None` | `announce()` **prints** the greeting itself, but **returns** nothing, so `print()` shows `None`. |
| `print(double(score))`                 | `60`                   | `value` is `30`, doubled to `60` and returned.                                              |
| `print(score)`                         | `30`                   | `double()` changed its own copy, `value`, not the variable `score`.                         |
| `print(boost())`                       | `ERROR`                | `points` has no default value, so it is required.                                           |
| `print(boost(double(3), double(4)))`   | `14`                   | `double(3)` is `6` and `double(4)` is `8`; `6 + 8`.                                         |

The rule of thumb for any function question: **what does it print, and what does it return?** A function can do either,
both, or neither.
