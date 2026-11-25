# Day 001 — Printing, Strings, Input & Variables

> **Goal:** Write programs that talk to the user. They show text, ask questions, remember the
> answers in variables, and combine everything into useful output.
>
> **Project:** 🎸 Band Name Generator
>
> **Time:** ~90 minutes · **Prerequisites:** none

---

## 📋 Table of contents

1. [`print()` — showing output](#1-print--showing-output)
2. [Strings — working with text](#2-strings--working-with-text)
3. [Debugging — reading error messages](#3-debugging--reading-error-messages)
4. [`input()` — getting data from the user](#4-input--getting-data-from-the-user)
5. [Variables — remembering data](#5-variables--remembering-data)
6. [Naming variables well](#6-naming-variables-well)
7. [Project: Band Name Generator](#7-project-band-name-generator)
8. [Interview corner](#8-interview-corner)
9. [What's next](#9-whats-next)

Files for this day: [examples](examples/) · [exercises](exercises/) · [solutions](solutions/) ·
[project](project/) · [cheatsheet](cheatsheet.md) · [quiz](quiz.md)

---

## 1. `print()` — showing output

### 🟢 Beginner

`print()` is a **function**, a named piece of code that does a job. You call it by writing its name
followed by parentheses. Whatever you put inside the parentheses is the **argument**, and `print()`
shows it on the screen.

```python
print("Hello, World!")      # Hello, World!
print(42)                   # 42
print()                     # (prints an empty line)
```

Each `print()` call ends with a new line by default, so the next call starts on the next line.

### 🟡 Intermediate: multiple arguments, `sep` and `end`

You can pass several values, separated by commas. `print()` puts a **space** between them
automatically, and it converts numbers to text for you.

```python
print("Score:", 98, "points")              # Score: 98 points
print("2026", "11", "25", sep="-")         # 2026-11-25
print("Loading", end="...")                # Loading...  (no newline)
print("done!")                             # Loading...done!
```

| Parameter | Default | What it controls |
|---|---|---|
| `sep` | `" "` | The text placed *between* arguments |
| `end` | `"\n"` | The text placed *after* the last argument |

### 🔴 Expert: what `print()` really does

- `print()` calls `str()` on every argument, joins the results with `sep`, adds `end`, and writes the
  result to `sys.stdout`, which is a file-like object.
- You can redirect output: `print("log", file=sys.stderr)` sends it to the error stream.
- Output is **buffered**. When you pipe output to a file or another program, it may not appear
  straight away. `print(..., flush=True)` forces it out, which matters for progress bars and logs.
- `print()` always returns `None`, so `x = print("hi")` leaves `x` as `None`.

📂 Try it: [`examples/01_print_basics.py`](examples/01_print_basics.py)

---

## 2. Strings — working with text

### 🟢 Beginner

A **string** (`str`) is a sequence of characters wrapped in quotes. Single and double quotes work
exactly the same way.

```python
"Hello"
'Hello'
"It's easy"          # use double quotes when the text contains an apostrophe
'She said "hi"'      # and single quotes when it contains double quotes
```

**Concatenation** joins strings together with `+`:

```python
print("Hello" + " " + "World")     # Hello World
```

⚠️ `+` does **not** add spaces for you. `"Hello" + "World"` gives `HelloWorld`.

### 🟢 Escape sequences

A backslash `\` gives the next character a special meaning:

| Sequence | Meaning | Example output |
|---|---|---|
| `\n` | New line | line break |
| `\t` | Tab | indentation |
| `\\` | A real backslash | `\` |
| `\"` / `\'` | A quote inside the same kind of quotes | `"` |

```python
print("Line one\nLine two")
print("Name:\tAda")
print("Path: C:\\Users\\ada")
```

### 🟡 Intermediate: f-strings (the modern way)

Joining text with `+` gets messy quickly, and it fails when one of the values is a number.
**f-strings** (Python 3.6+) let you put values straight into the text:

```python
name = "Ada"
age = 36
print("Hi " + name + ", you are " + str(age))   # old way: needs str()
print(f"Hi {name}, you are {age}")              # ✅ clean, works with any type
print(f"Next year you'll be {age + 1}")         # any expression works inside {}
```

Other useful tools:

```python
print("ha" * 3)                     # hahaha       (repetition)
print("""Multi-line
string""")                          # triple quotes keep line breaks
print("  padded  ".strip())         # 'padded'     (remove surrounding spaces)
print("ada lovelace".title())       # Ada Lovelace
print("Python".upper(), "Python".lower())
```

### 🔴 Expert

- **Strings are immutable.** `s.upper()` returns a *new* string and leaves `s` unchanged.
- Joining strings with `+` inside a loop builds a new string every time, which gets slow (O(n²)).
  Use `"".join(parts)` instead.
- **Raw strings** turn escape sequences off: `r"C:\new\folder"` keeps every backslash. They are
  essential for regular expressions and Windows paths.
- f-strings have their own formatting language: `f"{3.14159:.2f}"` → `3.14`,
  `f"{42:>6}"` → right-aligned, `f"{name=}"` → `name='Ada'`, which is handy for debugging.

📂 Try it: [`examples/02_strings_and_escapes.py`](examples/02_strings_and_escapes.py)

---

## 3. Debugging — reading error messages

### 🟢 Beginner

Errors are **normal**. Professional developers see them all day. Python tells you exactly what went
wrong, as long as you read the message.

```
  File "main.py", line 3
    print("Hello"
         ^
SyntaxError: '(' was never closed
```

**How to read it:** look at the **last line** first to learn *what* happened, then the line number
to find *where*.

### 🟢 The five errors you'll meet on Day 1

| Error | Cause | Broken | Fixed |
|---|---|---|---|
| `SyntaxError` | Missing quote or bracket | `print(Hello")` | `print("Hello")` |
| `SyntaxError` | Unclosed bracket | `print("Hi"` | `print("Hi")` |
| `IndentationError` | Unexpected space at the start of a line | `␣print("Hi")` | `print("Hi")` |
| `NameError` | Typo in a name, or variable not defined | `priint("Hi")` | `print("Hi")` |
| `TypeError` | Mixing types with `+` | `"Age: " + 5` | `"Age: " + str(5)` or `f"Age: {5}"` |

### 🟡 Intermediate: a debugging method

1. **Reproduce** the bug reliably.
2. **Read** the traceback from the bottom up.
3. **Inspect** your values with `print(f"{variable=}")` to see what they really hold.
4. **Isolate** the problem by commenting code out until the error disappears.
5. **Fix one thing at a time**, then run the code again.

### 🔴 Expert

- `SyntaxError` happens at **parse time**, so *no* line of the file runs. `NameError` and
  `TypeError` happen at **run time**, so every line before them has already run.
- Python 3.10+ gives much better hints, for example ``Did you mean 'print'?``.
- Use a real debugger: `breakpoint()` drops you into `pdb`. Use `n` to step to the next line,
  `p var` to print a variable, and `c` to continue. You can also click in the editor margin to set
  a breakpoint in PyCharm or VS Code.

📂 Practise: [`exercises/03_fix_the_bugs.py`](exercises/03_fix_the_bugs.py)

---

## 4. `input()` — getting data from the user

### 🟢 Beginner

`input()` shows a prompt, **waits** for the user to type something and press Enter, then gives back
what they typed.

```python
name = input("What is your name? ")
print("Hello " + name + "!")
```

💡 Put a space or `\n` at the end of the prompt so the user's answer isn't squashed against it.

Code runs **inside out**: in `print("Hi " + input("Name? "))`, the `input()` call runs first, and
its result is then used by `print()`.

### 🟡 Intermediate

- `input()` **always returns a string**, even when the user types `42`. Day 2 covers converting it
  to a number with `int()`.
- Clean up user input before you use it:

```python
city = input("City: ").strip().title()   # "  new york " → "New York"
```

- `len()` counts the characters in a string, spaces included:

```python
print(len("Ada Lovelace"))   # 12
```

### 🔴 Expert

- `input()` reads from `sys.stdin`. When input is piped in (`echo Ada | python app.py`), the prompt
  still prints, but nobody is typing. That is how automated tests feed input to a program.
- At end of input (Ctrl-D, or an empty pipe), `input()` raises `EOFError`. Robust command-line
  tools catch it.
- Never pass user input to `eval()` or `exec()`. That lets anyone run any code on your machine.

📂 Try it: [`examples/03_input_basics.py`](examples/03_input_basics.py)

---

## 5. Variables — remembering data

### 🟢 Beginner

A **variable** is a name that refers to a value. You create one with `=`, the **assignment**
operator. In Python `=` means "store", not "equals".

```python
username = "ada"
print(username)        # ada
username = "grace"     # reassign: the name now refers to a new value
print(username)        # grace
```

### 🟢 Classic exercise: swapping two variables

```python
glass1 = "milk"
glass2 = "juice"

# Way 1 — a temporary variable (works in every language)
temp = glass1
glass1 = glass2
glass2 = temp
```

### 🟡 Intermediate: the Pythonic swap

```python
glass1, glass2 = glass2, glass1      # ✅ one line, no temp variable
```

You can also assign several variables at once and **chain** assignments:

```python
x, y, z = 1, 2, 3
a = b = 0
```

Python is **dynamically typed**, which means a variable can refer to any type and you don't declare
it in advance:

```python
value = "ten"
value = 10          # allowed (but confusing — avoid it in real code)
print(type(value))  # <class 'int'>
```

### 🔴 Expert: names, objects and references

- A variable is **not a box** that holds a value. It is a **label** attached to an object somewhere
  in memory.

```python
a = "hello"
b = a                # b is a second label on the SAME object
print(a is b)        # True
print(id(a) == id(b))  # True — same memory identity
```

- The one-line swap works because the right-hand side `(glass2, glass1)` is evaluated first and
  packed into a **tuple**. That tuple is then **unpacked** into the names on the left.
- **Type hints** document what type a variable is meant to hold. Python doesn't enforce them, but
  tools such as `mypy` and your IDE do:

```python
city: str = "Mumbai"
```

📂 Try it: [`examples/04_variables_and_swap.py`](examples/04_variables_and_swap.py) ·
[`examples/05_references_under_the_hood.py`](examples/05_references_under_the_hood.py)

---

## 6. Naming variables well

### 🟢 Rules (break these and you get a `SyntaxError`)

- Names may contain letters, digits and `_`, but **cannot start with a digit**: `1st_name` ❌, `first_name` ✅
- Names cannot contain spaces or symbols: `user name` ❌, `user-name` ❌
- Names cannot be a **keyword**: `class`, `if`, `for`, `True`…
- Names are **case-sensitive**: `Name` and `name` are different variables.

### 🟡 Conventions (PEP 8, the Python style guide)

| Kind | Style | Example |
|---|---|---|
| Variables & functions | `snake_case` | `pet_name`, `get_total()` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES = 3` |
| Classes (Day 16+) | `PascalCase` | `BandNameGenerator` |

Choose names that explain what the value means: `n` ❌ → `name_length` ✅

### 🔴 Expert

- Don't shadow built-ins. Writing `print = "hi"` or `len = 5` breaks those functions for the rest of
  the program.
- You can list every keyword with `import keyword; print(keyword.kwlist)`.
- A leading underscore `_temp` signals "internal, please don't use". A plain `_` is a common name for
  a value you're throwing away.

📂 Try it: [`examples/06_naming_rules.py`](examples/06_naming_rules.py)

---

## 7. Project: Band Name Generator

The project is built in three stages. **Build v1 yourself first**, then compare your version with
the reference files.

| Version | File | What it teaches |
|---|---|---|
| **v1 — Basic** 🟢 | [`band_name_generator_v1.py`](project/band_name_generator_v1.py) | `print`, `input`, variables, concatenation |
| **v2 — Polished** 🟡 | [`band_name_generator_v2.py`](project/band_name_generator_v2.py) | f-strings, `.strip()`, `.title()`, validating empty input, ASCII banner |
| **v3 — Professional** 🔴 | [`band_name_generator_v3.py`](project/band_name_generator_v3.py) | Functions, type hints, docstrings, `__main__` guard, CLI arguments, testable design |

**Example run (v2):**

```
╔════════════════════════════════════╗
║        BAND NAME GENERATOR         ║
╚════════════════════════════════════╝
Which city did you grow up in?
> mumbai
What's your pet's name?
> bruno

Your band name could be: Mumbai Bruno 🤘
(That's 12 characters of pure rock.)
```

### 🚀 Extend it (pick at least one)

1. Ask a third question (favourite colour?) and offer three different name combinations.
2. Print the band name inside a box whose width fits the name. Hint: `len()` and `"═" * n`.
3. Generate a "tour poster" in the terminal with the band name, city and a made-up date.
4. 🔴 Add a `--shout` flag to v3 that prints the name in UPPERCASE.

---

## 8. Interview corner

| Question | Short answer |
|---|---|
| What's the difference between `'` and `"`? | Nothing. Pick one and use it consistently. |
| How do you swap two variables in Python? | `a, b = b, a` (tuple packing and unpacking). |
| What does `input()` return? | Always a `str`. |
| What does `print()` return? | `None`. |
| Is Python statically or dynamically typed? | Dynamically typed and **strongly** typed: `"1" + 1` is an error rather than a silent conversion. |
| Why prefer f-strings over `+`? | They're more readable, convert any type automatically, and are faster. |
| What's the difference between `is` and `==`? | `==` compares *values*; `is` checks whether two names refer to the *same object*. |

---

## 9. What's next

✅ Self-check: [quiz.md](quiz.md) · Revise: [cheatsheet.md](cheatsheet.md) · Test:
`pytest course/day-001-printing-variables -v`

➡️ **Day 002:** data types, numbers, maths operators and type conversion. That's where
`input()` + `int()` starts doing real calculations.
