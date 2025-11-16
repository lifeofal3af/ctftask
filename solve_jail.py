import pathlib

import jail

FLAG_PATH = pathlib.Path("flag.txt")
FLAG_PATH.write_text("fake{test_flag}\n", encoding="utf-8")

attempts = [
    # Baseline expressions from the challenge description
    *jail.tests,
    # Direct attempts to reach the fake flag and /proc/self/environ
    "open('flag.txt')",
    "open(flag.txt)",
    "next(open('flag.txt'))",
    "next(open(flag.txt))",
    "next(open('/proc/self/environ'))",
    "next(open(/proc/self/environ))",
]

for expr in attempts:
    print(f"{expr!r} => {jail.jail_eval(expr)}")
