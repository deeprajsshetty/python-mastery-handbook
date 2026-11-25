# 🐍 Python Mastery Handbook

A structured, hands-on Python course that goes from **absolute beginner to expert**. It follows the
100-day order of *100 Days of Code: The Complete Python Bootcamp*. The lessons, examples, exercises
and projects are rewritten and extended here, so they are not copies of the course material.

Every day is a self-contained lesson you can read and run on its own, or use later as a reference.

---

## 📚 How each day is organised

```
course/day-NNN-<topic>/
├── README.md        ← The lesson: concepts explained in three levels (🟢 → 🟡 → 🔴)
├── cheatsheet.md    ← One-page summary for quick revision
├── quiz.md          ← Self-check questions with hidden answers
├── examples/        ← Small runnable scripts, one concept per file
├── exercises/       ← Practice problems (starter files with TODOs)
├── solutions/       ← Reference solutions, with explanations in comments
├── project/         ← The day's project, built in stages (v1 basic → v3 professional)
└── tests/           ← Automated tests for the solutions and project
```

### Difficulty levels used throughout

| Badge | Level | Who it's for |
|---|---|---|
| 🟢 | **Beginner** | First time seeing the concept. Covers what it is and how to use it. |
| 🟡 | **Intermediate** | You know the basics and want cleaner, more idiomatic Python. |
| 🔴 | **Expert** | How it works under the hood, edge cases, and interview-level depth. |

Read the 🟢 sections first. Come back for 🟡 and 🔴 when you're ready.

---

## 🗺️ Course roadmap

| Day | Topic | Project | Status |
|---|---|---|---|
| [001](course/day-001-printing-variables/README.md) | Printing, Strings, Input & Variables | Band Name Generator | ✅ |
| 002 | Data Types, Numbers, Operations & Type Conversion | Tip Calculator | ⏳ |
| 003 | Control Flow & Logical Operators | Treasure Island | ⏳ |
| 004 | Randomisation & Lists | Rock Paper Scissors | ⏳ |
| 005 | Loops | Password Generator | ⏳ |
| … | *New days are added as they are completed* | | |

---

## 🚀 Quick start

```bash
# 1. Clone and enter the repo
git clone <this-repo-url> && cd python-mastery-handbook

# 2. Create a virtual environment (one time)
python3 -m venv .venv && source .venv/bin/activate

# 3. Install the test runner
pip install pytest

# 4. Run any example, solution or project
python course/day-001-printing-variables/project/band_name_generator_v3.py

# 5. Check your work
pytest course/day-001-printing-variables
```

New to Python? Start with the **[Getting Started guide](docs/getting-started.md)**, then read the
**[Learning Guide](docs/learning-guide.md)** for advice on studying effectively.

---

## 🗂️ Other folders

| Folder | What's inside |
|---|---|
| [`docs/`](docs/) | Setup guide, learning strategy, and how to use this handbook |
| `0003-download-resource-tips/` | Printable course resources (pledge, posters, notebook sheets, wallpapers). Kept locally and git-ignored. |
| `001-day/` … | Raw notes written while following the course. The polished version lives in `course/` |

---

## 🎯 What you'll be able to do by the end

Fundamentals → OOP → data structures & algorithms → files & APIs → web development → data science →
automation → testing → concurrency & async → design patterns → AI engineering.
