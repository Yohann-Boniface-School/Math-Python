def seven_multiple(x: int) -> str:
    return ' '.join(
        f"{7 * i}%s" % ('*' * (not 7 * i % 3)) for i in range(1, x)
    )


def main() -> None:
    print(seven_multiple(21))


if __name__ == '__main__':
    main()
