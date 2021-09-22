from __future__ import annotations

import functools
from string import ascii_uppercase
from matrix import Matrix


class MulMatrix(Matrix):

    def __matmul__(self, other) -> MulMatrix:
        return MulMatrix(
            [
                sum(
                    functools.reduce(lambda _a, _b: _a * _b, x)
                    for x in zip(i, j)
                )
                for j in list(zip(*other))
            ] for i in self
        )


class MatrixCipher:

    def __init__(self, key: MulMatrix):
        self.__key = key

    @staticmethod
    def to_mat(initial_text: str) -> MulMatrix:
        return MulMatrix(
            [ascii_uppercase.index(char) for char in initial_text[i:i + 3]]
            for i in range(0, len(initial_text), 3)
        )

    def cipher(self, clear_text: str) -> str:
        return ''.join(
            ''.join(ascii_uppercase[item % 26] for item in line)
            for line in (self.to_mat(clear_text) @ self.__key)
        )


def main():
    cipherer = MatrixCipher(
        key=MulMatrix(
            [1, 2, 1],
            [2, 1, 3],
            [2, 4, 2]
        )
    )

    print(cipherer.cipher('CARTES'))

    for n in range(15, 26):
        cipherer = MatrixCipher(
            key=MulMatrix(
                [11, n, 14],
                [7, 9, 21],
                [17, 0, 3]
            )
        )

        print(f'cipher(GEL, {n}) ~>', cipherer.cipher('GEL'))


if __name__ == '__main__':
    main()
