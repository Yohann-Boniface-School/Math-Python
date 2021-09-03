def check_a(a) -> None:
    if a > 100:
        print("a dépasse la centaine")
    else:
        print("a ne dépasse pas la centaine")


if __name__ == '__main__':
    for a_val in (20, 101):
        check_a(a_val)
