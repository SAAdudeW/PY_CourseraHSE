from sys import stdin

print(
    any(
        map(
            lambda x: x == 0, map(int, stdin.readlines()[1:])
        )
    )
)
