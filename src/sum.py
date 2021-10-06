def main() -> None:
    a, b = (int(input(f'{x}:')) for x in 'ab')
    print(f"A vaut {a}, B vaut {b} et leur somme vaut {a + b}")


if __name__ == '__main__':
    main()
