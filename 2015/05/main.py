rows = [row.strip() for row in open("input", "r").readlines()]


def cnt_vowels(s: str) -> int:
    return len([c for c in s if c in "aeiou"])


def p1(row: str) -> bool:
    return (
            not any(v in row for v in ["ab", "cd", "pq", "xy"])
            and any(c == nc for c, nc in zip(row, row[1:]))
            and cnt_vowels(row) >= 3
    )


print("1:", sum(map(p1, rows)))
