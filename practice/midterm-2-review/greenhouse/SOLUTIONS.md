<h2 align=center>Review Solutions</h2>

<h1 align=center>Midterm 2: The Greenhouse Watering Log</h1>

These solutions use the following constants:

```python
DAY_IDX, PLANT_IDX, ML_IDX = 0, 1, 2
```

### 1. `read_log(filename)`

```python
def read_log(filename):
    entries = []

    with open(filename, "r") as file:
        for line in file:
            if not line.startswith("#"):
                fields = line.strip().split(",")

                is_valid = True

                try:
                    day = int(fields[DAY_IDX])
                    ml = int(fields[ML_IDX])
                except ValueError:
                    is_valid = False

                if is_valid:
                    entries.append((day, fields[PLANT_IDX], ml))

    return entries
```

The comment lines are left out by the first `if`. For every other line, the `try` converts the two numbers. If either
conversion fails, `is_valid` becomes `False` and the entry is not added.

### 2. `safe_read(filename)`

```python
def safe_read(filename):
    try:
        return read_log(filename)
    except FileNotFoundError:
        print(f"No log named {filename}")
        return []
```

`read_log()` does not catch anything about the file, so the `FileNotFoundError` from `open()` travels **up** to the
function that called it. That is where this `try`-`except` catches it.

### 3. `total_water(entries, plant)`

```python
def total_water(entries, plant):
    total = 0

    for day, name, ml in entries:
        if name == plant:
            total += ml

    return total
```

Each entry is a tuple with three elements, so the `for`-loop can **unpack** it into three variables.

### 4. `ranking(entries)`

```python
def ranking(entries):
    names = []
    for entry in entries:
        if entry[PLANT_IDX] not in names:
            names.append(entry[PLANT_IDX])

    pairs = []
    for name in names:
        pairs.append((total_water(entries, name), name))

    pairs.sort(reverse=True)
    return pairs
```

The first loop collects each name once. The second one pairs each name with its total, using problem 3. Sorting compares
the first element of each pair, which is why the total goes first. `reverse=True` puts the largest first.

### 5. `write_summary(entries, filename)`

```python
def write_summary(entries, filename):
    names = []
    for entry in entries:
        if entry[PLANT_IDX] not in names:
            names.append(entry[PLANT_IDX])
    names.sort()

    with open(filename, "w") as summary:
        for name in names:
            count = 0
            for entry in entries:
                if entry[PLANT_IDX] == name:
                    count += 1

            summary.write(f"{name}: {count} watering(s), {total_water(entries, name)} ml\n")

        total = 0
        for entry in entries:
            total += entry[ML_IDX]

        summary.write(f"Total: {total} ml\n")
```

`write()` does not add a new line by itself, so the `\n` at the end of each string is needed. The `Total` line is written
**after** the loop over the plants, but still inside the `with`, while the file is open.

### 6. (Challenge) `split_at(entries, day)`

```python
def split_at(entries, day):
    before = []
    after = []

    for entry in entries:
        if entry[DAY_IDX] < day:
            before.append(entry)
        else:
            after.append(entry)

    return before, after
```

Both lists are built in a single pass, and `return before, after` returns them as a tuple. The entries themselves are
tuples that are shared with the original list, but since tuples cannot change, and the original list is never modified,
nothing that was passed in is touched.
