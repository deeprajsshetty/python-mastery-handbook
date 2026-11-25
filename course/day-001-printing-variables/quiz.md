# Day 001 · Quiz

Answer each one in your head (or in the REPL) **before** expanding it.

### 🟢 Beginner

**1.** What does this print?
```python
print("Hello" + "World")
```
<details><summary>Answer</summary>

`HelloWorld`, because `+` does not add a space.
</details>

**2.** What type does `input()` return when the user types `42`?
<details><summary>Answer</summary>

`str`, the text `"42"`. You need `int()` to turn it into a number (Day 2).
</details>

**3.** Which of these names are valid? `user_name`, `2nd_place`, `userName`, `user-name`, `_tmp`, `for`
<details><summary>Answer</summary>

Valid: `user_name`, `userName`, `_tmp`. Invalid: `2nd_place` (starts with a digit), `user-name` (`-` is
the minus operator), `for` (a keyword). `userName` is valid, but PEP 8 prefers `user_name`.
</details>

**4.** What is `len("Hi there")`?
<details><summary>Answer</summary>

`8`. The space counts as a character.
</details>

### 🟡 Intermediate

**5.** What does this print?
```python
print("a", "b", "c", sep="", end="!\n")
```
<details><summary>Answer</summary>

`abc!`
</details>

**6.** After this code runs, what are `x`, `y` and `z`?
```python
x, y, z = 1, 2, 3
x, y, z = z, x, y
```
<details><summary>Answer</summary>

`x=3, y=1, z=2`. The whole right-hand side is evaluated *before* anything is assigned.
</details>

**7.** Why does `"Age: " + 30` fail, and how do you fix it two different ways?
<details><summary>Answer</summary>

`TypeError`: Python won't add a `str` and an `int` together. Fix it with `"Age: " + str(30)` or `f"Age: {30}"`.
</details>

**8.** What's printed?
```python
word = "python"
word.upper()
print(word)
```
<details><summary>Answer</summary>

`python`. Strings are immutable, and `.upper()` returned a new string that was thrown away.
</details>

### 🔴 Expert

**9.** What does `print(print("hi"))` output?
<details><summary>Answer</summary>

```
hi
None
```
The inner `print` shows `hi` and returns `None`, and the outer `print` then shows that `None`.
</details>

**10.** A file has a `SyntaxError` on line 10. Does line 1 (`print("start")`) run?
<details><summary>Answer</summary>

No. Python parses the *whole file* before running any of it, so a `SyntaxError` stops everything.
A `NameError` on line 10 *would* let lines 1–9 run first.
</details>

**11.** After `a = "hi"` and `b = a`, is `b` a copy of `a`?
<details><summary>Answer</summary>

No. Both names refer to the same object (`a is b` is `True`). Assigning a new value to `a` only moves
the `a` label, so `b` still refers to `"hi"`.
</details>

**12.** What does `f"{3.14159:.2f}|{'py':>4}|{'py':^6}|"` produce?
<details><summary>Answer</summary>

`3.14|  py|  py  |`
</details>
