"""Automated checks for Day 001.

    pytest course/day-001-printing-variables -v                  # reference solutions
    CHECK=exercises pytest course/day-001-printing-variables -v  # your own exercise files

Each script is run as a real program: we feed text to its stdin and inspect stdout,
exactly as if a user typed the answers.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import pytest

DAY_DIR = Path(__file__).resolve().parents[1]
TARGET = DAY_DIR / os.environ.get("CHECK", "solutions")


def run(script: str | Path, stdin: str = "", *args: str) -> str:
    path = script if isinstance(script, Path) else TARGET / script
    result = subprocess.run(
        [sys.executable, str(path), *args],
        input=stdin,
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, f"{path.name} crashed:\n{result.stderr}"
    return result.stdout


# ---------------------------------------------------------------- exercises
def test_01_concert_ticket():
    assert run("01_concert_ticket.py").splitlines() == [
        "=" * 32,
        "  ROCK NIGHT LIVE - ADMIT ONE",
        '  Venue: "The Blue Frog"',
        "  Seat:  B-12",
        "=" * 32,
    ]


def test_02_escape_sequences():
    assert run("02_escape_sequences.py") == 'Folder:\tC:\\projects\\day1\nStatus:\t"done"\n'


def test_03_fix_the_bugs():
    assert run("03_fix_the_bugs.py").splitlines() == [
        "Debugging is a superpower",
        "Errors tell you WHERE and WHAT",
        "Read the last line first",
        "Line numbers are your map",
        "Fix one bug at a time",
    ]


@pytest.mark.parametrize(
    "typed, greeting, length",
    [("  ada lovelace ", "Hello, Ada Lovelace!", 12), ("grace", "Hello, Grace!", 5)],
)
def test_04_name_stats(typed, greeting, length):
    out = run("04_name_stats.py", typed + "\n")
    assert greeting in out
    assert f"Your name has {length} characters." in out


def test_05_swap_and_rotate():
    assert run("05_swap_and_rotate.py").splitlines() == ["cup1=coffee cup2=tea", "a=2 b=3 c=1"]


def test_05_does_not_retype_values():
    source = (TARGET / "05_swap_and_rotate.py").read_text()
    assert source.count('"tea"') == 1 and source.count('"coffee"') == 1


@pytest.mark.parametrize("name", ["Grace", "Ada Lovelace", "X"])
def test_06_name_badge(name):
    lines = run("06_name_badge.py", name + "\n").splitlines()
    border = "+" + "-" * (len(name) + 4) + "+"
    assert lines[0].endswith(border)  # the input prompt may share this line
    assert f"|  {name}  |" in lines
    assert lines[-1] == border


# ---------------------------------------------------------------- project
PROJECT = DAY_DIR / "project"


def test_project_v1():
    out = run(PROJECT / "band_name_generator_v1.py", "Pune\nTiger\n")
    assert "Your band name could be Pune Tiger" in out


def test_project_v2_cleans_and_defaults():
    out = run(PROJECT / "band_name_generator_v2.py", "  new york \n\n")
    assert "Your band name could be: New York Nobody" in out


def _load_v3():
    spec = importlib.util.spec_from_file_location("bng_v3", PROJECT / "band_name_generator_v3.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_project_v3_functions():
    v3 = _load_v3()
    assert v3.clean("  new york ", "X") == "New York"
    assert v3.clean("   ", "X") == "X"
    assert v3.make_band_name("pune", "tiger") == "Pune Tiger"
    assert v3.band_name_variants("pune", "tiger")[0] == "Pune Tiger"
    box = v3.boxed("Hi").splitlines()
    assert len({len(line) for line in box}) == 1  # every line the same width


def test_project_v3_cli():
    out = run(PROJECT / "band_name_generator_v3.py", "", "--city", "pune", "--pet", "tiger", "--shout")
    assert "PUNE TIGER" in out


def test_project_v3_handles_eof():
    out = run(PROJECT / "band_name_generator_v3.py", "")
    assert "stage will wait" in out
