from typing import TypeVar, List

S = TypeVar("S")
T = TypeVar("T")


def alternate_lists(t1: List[S], t2: List[T]) -> List[S, T]:
    return [x for y in zip(t2, t1) for x in y]


def main() -> None:
    print(
        alternate_lists(
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
             'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        )
    )


if __name__ == '__main__':
    main()
