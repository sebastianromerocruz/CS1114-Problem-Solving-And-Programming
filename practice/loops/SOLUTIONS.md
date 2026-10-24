<h2 align=center>Review Solutions<h2>

<h1 align=center>Loops and Strings</h1>

### 1. What will be printed by the following code snippets?

```
new york university
```
```
YUU
```
```
NNYYUU  TT
```
```
NtseiUko e
```
```
BBBrrBBBrrrooo
```
```
NYN
```
```
k9a8n7d6i5n4s3k2y1
```

### 2. What is the final value of `word` in each of these situations?

```python
"nyu"
```

<sub>`capitalize()` returns a **new** string and strings are immutable, so `word` never changes; the result is thrown away because it isn't assigned to anything.</sub>

```python
"NYU"
```
```python
'k'
```
```python
"new york university"
```

<sub>Same idea: `word[::-1]` creates a reversed string, but it is never assigned, so `word` is unchanged.</sub>

```python
"adn"
```
```python
"ysvUr N"
```
```text
2
3
yyyyyy
```
```python
"nlkrb"
```

<sub>The first block is what gets **printed** along the way (the vowels `o` at indices `2` and `3` print their indices, and the `y` at index `6` prints `'y' * 6`); the second is the final value of `word`.</sub>

```python
"wowowowo"
```
```python
"TimeIsNotReal"
```
