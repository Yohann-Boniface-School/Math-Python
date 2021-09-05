from typing import List


def fib(n: int) -> List[int]:
    a: int = 0
    b: int = 1
    r: List[int] = []

    for _ in range(n):
        a, b = b, a + b
        r.append(a)
    return r


if __name__ == '__main__':
    print(*fib(100))
