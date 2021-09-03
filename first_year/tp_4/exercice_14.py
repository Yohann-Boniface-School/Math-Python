def time(s: int) -> str:
    return (
        "{0}s -> {3}h, {2}m {1}s".format(
            s, *((s % 60, s := s // 60)[0] for _ in range(2)), s
        )
    )


def seven_multiple(x: int) -> str:
    return ' '.join(
        f"{7 * i}%s" % ('*' * (not 7 * i % 3)) for i in range(1, x)
    )


def main() -> None:
    print(seven_multiple(21))
    print(time(int(input("s: "))))


if __name__ == '__main__':
    main()
