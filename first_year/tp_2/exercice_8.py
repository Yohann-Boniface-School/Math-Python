def check_a(a) -> None:
    if a > 0:
        print("a est positif")
    elif a < 0:
        print("a est négatif")
    else:
        print("a est nul")


if __name__ == '__main__':
    for a_val in (-1, 0, 1):
        check_a(a_val)
