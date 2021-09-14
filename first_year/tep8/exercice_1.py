from typing import List


def lumino_moy(mat: List[List[int]]) -> int:
    return sum(sum(line) for line in mat) // (len(mat) ** 2)


def modif_contrast(mat: List[List[int]], m: int) -> List[List[int]]:
    return [[x * 2 if x < m else x // 2 for x in line] for line in mat]


def modif_contrast_100(mat: List[List[int]], m: int) -> List[List[int]]:
    return [
        [min(x * 2 if x < m else x // 2, 100) for x in line]
        for line in mat
    ]


def main():
    mat = [
        [100, 100, 100, 75, 75, 0],
        [0, 100, 100, 75, 65, 0],
        [100, 100, 100, 65, 40, 0],
        [100, 0, 100, 75, 40, 0],
        [0, 0, 100, 65, 40, 0],
        [0, 0, 100, 51, 20, 0]
    ]

    m = lumino_moy(mat)
    print(modif_contrast(mat, m))
    print(modif_contrast_100(mat, m))


if __name__ == '__main__':
    main()
