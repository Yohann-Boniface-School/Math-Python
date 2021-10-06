def time(s: int) -> str:
    return (
        "{0}s -> {3}h, {2}m {1}s".format(
            s, *((s % 60, s := s // 60)[0] for _ in range(2)), s
        )
    )


if __name__ == '__main__':
    print(time(int(input("s: "))))
