# Python Mastery Handbook — conventions

This repo turns the owner's notes from *100 Days of Code: The Complete Python Bootcamp* into an
original, structured course that takes a reader from beginner to expert.

## Workflow when a new day is uploaded

1. The owner uploads raw notes as `NNN-day/` (e.g. `002-day/main.py`, `project.py`). **Leave the raw
   folders untouched.** They are the owner's personal record.
2. Create the polished version at `course/day-NNN-<kebab-topic>/` (3-digit day number).
3. **Do not copy the course code or exercise wording.** Rewrite and extend: new examples, new
   exercises, new data, with deeper 🟢/🟡/🔴 explanations. The project may keep its theme (e.g.
   "Tip Calculator") but the code must be original and built in stages.
4. Update the roadmap table in the root `README.md` (link + ✅), and the "What's next" link at the
   end of the previous day's README.
5. Run `pytest course/` and run each example, solution and project script before finishing.

## Folder template (every day)

```
course/day-NNN-topic/
  README.md        lesson: numbered sections, each with 🟢 Beginner / 🟡 Intermediate / 🔴 Expert,
                   plus a "📂 Try it" link to examples; then Project, Interview corner, What's next
  cheatsheet.md    one-page revision sheet
  quiz.md          ~12 questions (4 per level) with answers in <details>
  examples/        NN_<concept>.py — runnable, one concept each, level badges in comments
  exercises/       README.md table + NN_<name>.py starters (docstring = task + exact expected output)
  solutions/       same filenames as exercises, with an explanatory docstring/comments
  project/         <name>_v1.py (basic) → _v2.py (polished) → _v3.py (pro: functions, type hints,
                   __main__ guard, argparse, testable)
  tests/           test_day_NNN.py — runs scripts as subprocesses with stdin; honours CHECK=exercises
```

## Style

- Python 3.10+, PEP 8, `snake_case`, f-strings. Docstring at the top of every file.
- Day-appropriate code: don't use a concept in the 🟢/🟡 material before the course introduces it.
  🔴 sections and v3 projects may preview later topics, but must label them ("covered on Day N").
- Exercise solutions stay function-free until functions are taught (Day 8). Tests check their
  stdout.
- Never reproduce the PDFs in `0003-download-resource-tips/` (App Brewery copyright). Only link to them.
