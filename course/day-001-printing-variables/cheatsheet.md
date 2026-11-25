# Day 001 · Cheatsheet

## Output
```python
print("text")                     # prints, then a newline
print("a", "b", 3)                # a b 3        (space-separated)
print("a", "b", sep="-")          # a-b
print("no newline", end="")       # stays on the same line
```

## Strings
```python
"double" == 'single'              # same thing
"Hello" + " " + "World"           # concatenation (no auto spaces!)
"ha" * 3                          # hahaha
f"Hi {name}, {age + 1}"           # f-string: any expression in {}
"""multi
line"""                           # triple quotes
r"C:\raw\path"                    # raw string: escapes ignored
```

| Escape | `\n` newline | `\t` tab | `\\` backslash | `\"` quote |
|---|---|---|---|---|

## String methods (return NEW strings)
```python
s.strip()   s.title()   s.upper()   s.lower()   s.center(20)   len(s)
```

## Input
```python
name = input("Prompt: ")          # ALWAYS returns str
name = input("> ").strip().title()  # clean it up
```

## Variables
```python
x = 5                             # assign
x = "five"                        # reassign (any type)
a, b = b, a                       # swap
a, b, c = b, c, a                 # rotate
total = count = 0                 # chain
city: str = "Pune"                # type hint
```

## Naming
`snake_case` variables · `UPPER_CASE` constants · no leading digits · no spaces/hyphens ·
no keywords · case-sensitive · don't shadow built-ins (`len`, `print`, `str`, `input`)

## Errors
| Error | Usual cause |
|---|---|
| `SyntaxError` | Missing/mismatched quote or bracket |
| `IndentationError` | Stray spaces at the start of a line |
| `NameError` | Typo, wrong case, or used before assignment |
| `TypeError` | `"text" + 5` — mixing types |

**Read tracebacks bottom-up:** last line = *what*, line number = *where*.
