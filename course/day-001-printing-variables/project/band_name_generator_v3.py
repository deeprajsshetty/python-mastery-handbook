"""🎸 Band Name Generator — v3 (🔴 Professional)

New since v2:
  • Logic split into small, pure, *testable* functions
  • Type hints and docstrings
  • `if __name__ == "__main__":` guard so the module can be imported by tests
  • Optional command-line arguments (argparse) — skip the questions entirely
  • Several name styles, not just one
  • Graceful exit on Ctrl-C / Ctrl-D

Run interactively:    python project/band_name_generator_v3.py
Run non-interactively: python project/band_name_generator_v3.py --city "new york" --pet rex --shout
"""
from __future__ import annotations

import argparse

DEFAULT_CITY = "Nowhere"
DEFAULT_PET = "Nobody"


def clean(text: str, fallback: str) -> str:
    """Trim whitespace and title-case `text`; return `fallback` if it's blank.

    >>> clean("  new york ", "X")
    'New York'
    >>> clean("   ", "X")
    'X'
    """
    tidy = text.strip().title()
    return tidy or fallback


def make_band_name(city: str, pet: str) -> str:
    """Classic formula: '<City> <Pet>'."""
    return f"{clean(city, DEFAULT_CITY)} {clean(pet, DEFAULT_PET)}"


def band_name_variants(city: str, pet: str) -> list[str]:
    """A few alternative styles so the user can pick a favourite."""
    c = clean(city, DEFAULT_CITY)
    p = clean(pet, DEFAULT_PET)
    return [
        f"{c} {p}",
        f"The {p} Experience",
        f"{p} & The {c} Sound",
    ]


def boxed(text: str, padding: int = 2) -> str:
    """Return `text` inside a box that is exactly as wide as it needs to be."""
    inner = len(text) + padding * 2
    return "\n".join(
        [
            "╔" + "═" * inner + "╗",
            "║" + " " * padding + text + " " * padding + "║",
            "╚" + "═" * inner + "╝",
        ]
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a band name.")
    parser.add_argument("--city", help="City you grew up in")
    parser.add_argument("--pet", help="Your pet's name")
    parser.add_argument("--shout", action="store_true", help="PRINT IN CAPS")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    print(boxed("BAND NAME GENERATOR"))

    try:
        city = args.city if args.city is not None else input("Which city did you grow up in?\n> ")
        pet = args.pet if args.pet is not None else input("What's your pet's name?\n> ")
    except (EOFError, KeyboardInterrupt):
        print("\nNo worries — the stage will wait for you. 👋")
        return

    name = make_band_name(city, pet)
    if args.shout:
        name = name.upper()

    print("\nYour band name could be:")
    print(boxed(name))
    print("\nOther ideas:")
    for idea in band_name_variants(city, pet)[1:]:
        print(f"  • {idea}")


if __name__ == "__main__":
    main()
