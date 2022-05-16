print(
    ' '.join(
        map(
            str, list(
                map(
                    lambda pair: int(pair[0] != pair[1]), zip(
                        map(int, input().split()), map(int, input().split())
                    )
                )
            )
        )
    )
)
