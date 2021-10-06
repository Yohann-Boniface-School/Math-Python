from typing import List


def find_divisors(n: int) -> List[int]:
    return [p for p in range(1, n + 1) if not n % p]


if __name__ == '__main__':
    print(', '.join(map(str, find_divisors(1234567))))
