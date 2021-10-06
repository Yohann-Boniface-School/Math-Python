def square_sum(n) -> int:
    return sum(map(lambda x: x ** 2, range(1, n + 1)))


if __name__ == '__main__':
    print(square_sum(5))
