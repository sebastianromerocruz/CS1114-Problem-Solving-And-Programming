<h2 align=center>Review Solutions</h2>

<h1 align=center>Midterm 2: Reading a Greenhouse Log</h1>

These solutions use the following constants:

```python
FIELD_COUNT = 4
HEIGHT_IDX, DAYS_IDX = 2, 3
```

### 1. `read_plants(filename)`

```python
def read_plants(filename):
    plants = []

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"Could not open {filename}")
        return plants

    file.readline()  # skip the header

    for line in file:
        fields = line.strip().split(",")

        if len(fields) == FIELD_COUNT:
            is_valid = True

            try:
                height = int(fields[HEIGHT_IDX])
                days = int(fields[DAYS_IDX])
            except ValueError:
                is_valid = False

            if is_valid:
                plants.append((fields[0], fields[1], height, days))

    file.close()
    return plants
```

The `try`-`except` around `open()` deals with the missing file, and the one inside the loop deals with the bad
numbers. The blank line and the line with three fields do not have four fields, so the first `if` leaves them out
before we even try to convert anything. If a conversion fails, `is_valid` becomes `False` and the plant is not added.

### 2. `tallest(plants)`

```python
def tallest(plants):
    if len(plants) == 0:
        return None

    best = plants[0]
    for plant in plants:
        if plant[HEIGHT_IDX] > best[HEIGHT_IDX]:
            best = plant

    return best
```

The comparison uses `>` and not `>=`, so that a tie keeps the plant that appeared first.

### 3. `rooms(plants)`

```python
def rooms(plants):
    found = []

    for plant in plants:
        if plant[1] not in found:
            found.append(plant[1])

    return found
```

### 4. `thirsty(plants, limit)`

```python
def thirsty(plants, limit):
    pairs = []

    for name, room, height, days in plants:
        if days >= limit:
            pairs.append((days, name))

    pairs.sort(reverse=True)
    return pairs
```

Each plant is a tuple with four elements, so the `for`-loop can **unpack** it into four variables. Sorting compares the
first element of each pair, which is why `days` goes first. `reverse=True` puts the largest first.

### 5. `write_report(plants, filename)`

```python
def write_report(plants, filename):
    with open(filename, "w") as report:
        for room in rooms(plants):
            count = 0
            total_height = 0

            for plant in plants:
                if plant[1] == room:
                    count += 1
                    total_height += plant[HEIGHT_IDX]

            average = total_height / count
            report.write(f"{room}: {count} plant(s), average height {average:.1f} cm\n")
```

`write()` does not add a new line by itself, so the `\n` at the end of the string is needed. `count` and `total_height`
are created inside the outer loop so that they start at zero for every room.

### 6. (Challenge) `grown(plants, extra)`

```python
def grown(plants, extra):
    new_plants = []

    for name, room, height, days in plants:
        new_plants.append((name, room, height + extra, days))

    return new_plants
```

A tuple cannot be changed, so each plant is **rebuilt** with its new height, and the new tuples go into a new list. The
original list is never touched.
