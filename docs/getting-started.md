# 🛠️ Getting Started

This guide gets your computer ready to run every file in this handbook.

## 1. Install Python

Check whether Python is already installed:

```bash
python3 --version
```

You need **Python 3.10 or newer**. If it's missing, download it from [python.org](https://www.python.org/downloads/).
On macOS you can also run `brew install python`.

## 2. Choose an editor

| Editor | Why pick it |
|---|---|
| **PyCharm Community** | Built for Python. Its debugger is great for beginners. |
| **VS Code** + Python extension | Light, fast, and works for every language. |
| **Thonny** | Very simple. Shows variables changing step by step. |

## 3. Create a virtual environment

A virtual environment (`venv`) is a private folder that holds the packages for one project, so
different projects don't clash with each other.

```bash
cd python-mastery-handbook
python3 -m venv .venv          # create it (one time)
source .venv/bin/activate      # activate it (macOS/Linux) — every new terminal
# .venv\Scripts\activate       # Windows
pip install pytest             # install the test runner
deactivate                     # leave the venv when you're done
```

> 💡 `.venv/` is already in `.gitignore`. Never commit it.

## 4. Run code

```bash
python course/day-001-printing-variables/examples/01_print_basics.py   # run a script
python                                                                 # open the interactive REPL
>>> print("hi")
>>> exit()
```

The **REPL** (Read-Eval-Print Loop) is the best place to try out one line of code quickly.

## 5. Run the tests

```bash
pytest course/day-001-printing-variables -v
```

A green `passed` means your solution behaves correctly. A red `failed` shows you what was expected
and what your code actually produced.
