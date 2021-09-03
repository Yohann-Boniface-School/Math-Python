def factorial(x):
    r = 1
    for i in range(1, x + 1):
        r *= i

    return r


def main() -> None:
    nombre = int(input("Entrez votre nombre: "))
    print(f"La factorielle de {nombre} est: {factorial(r)}")


if __name__ == '__main__':
    main()
