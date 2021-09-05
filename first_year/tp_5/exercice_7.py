from typing import List


def syracuse(u) -> List[int]:
    r: list = []
    while u != 1:
        u: int = (3 * u + 1) if u % 2 else int(u / 2)
        r.append(u)
    return r


if __name__ == '__main__':
    print(syracuse(120))
