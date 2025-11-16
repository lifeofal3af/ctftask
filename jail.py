SAFE_BUILTINS = {
    "next": next,
    "open": open,
}

ALLOWED_CHARS = "abcefghijklmnopqrstuvwxyz()."


def is_unsafe(i: str) -> bool:
    return any(c not in ALLOWED_CHARS for c in i) or len(i) > 64 or 'str' in i or i.count('.') > 1


def jail_eval(s):
    if is_unsafe(s):
        return "FILTER"
    try:
        return eval(s, {"__builtins__": SAFE_BUILTINS}, {})
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"


tests = [
    "()",
    "open",
    "next",
    "open()",
    "next(open)",
    "open().a",
    "().a",
    "open.a",
    "().count",
    "().count()",
]

if __name__ == "__main__":
    for t in tests:
        print(f"{t!r} => {jail_eval(t)}")
