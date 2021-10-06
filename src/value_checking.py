def check_a(a) -> None:
    if a > 100:
        print("a dépasse la centaine")
    else:
        print("a ne dépasse pas la centaine")


def check_a_sign(a) -> None:
    if a > 0:
        print("a est positif")
    elif a < 0:
        print("a est négatif")
    else:
        print("a est nul")


if __name__ == '__main__':
    for a_val in (20, 101):
        check_a_sign(a_val)

    for a_val in (-1, 0, 1):
        check_a(a_val)
