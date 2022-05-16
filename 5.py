from functools import reduce

print(
    reduce(
        lambda x, y: x * y, map(
            lambda n: n ** 5, map(
                int, input().split()
            )
        )
    )
)
