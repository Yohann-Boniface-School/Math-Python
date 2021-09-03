def seven_multiple(x: int) -> None:
    print(*(f"{7 * i}%s" % ('*' * (not 7 * i % 3)) for i in range(1, x)))


if __name__ == '__main__':
    seven_multiple(21)
