from random import randint


def valid_input(text: str) -> int:
    x: str = input(text)
    while not x.isdigit() or int(x) < 1:
        x = input(text)

    return int(x)


def main():
    is_running: bool = True
    r: int = randint(1, 100)

    while is_running:
        g = valid_input("Nombre > 1 :")

        if g != r:
            print('trop', 'petit' if g < r else 'grand')
        else:
            is_running = False

    print("Bravo !")


if __name__ == '__main__':
    main()
