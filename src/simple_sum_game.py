from random import randint


def game():
    numbers = [randint(1, 5) for _ in range(5)]
    print("->", *numbers)
    win = 1 - sum(numbers) % 2

    if win:
        print("Even sum: 1 point")

    if max(numbers) == 2:
        print("Max is 2 : 2 points")
        win += 2

    if max(map(lambda x: numbers.count(x), set(numbers))) >= 3:
        print("3+ n occurrence: 5 points")
        win += 5

    print(f"Total : {win} points")
    print('-' * 20)  # sep for readability


def main():
    is_running = True

    while is_running:
        game()
        is_running = input("continue ? [y/n] ").lower().startswith('y')


if __name__ == '__main__':
    main()
