import random


def play():
    random.seed()

    while True:
        try:
            numTries = int(input('Input number of tries: '))
        except ValueError:
            print("Please input an integer.")
            continue
        else:
            break

    while True:
        try:
            high = int(input('Input upper bound: '))
        except ValueError:
            print("Please input an integer.")
            continue
        else:
            break

    rnd = random.randint(1, high)

    for i in range(numTries):
        guess = int(input(f"Attempt {i + 1} Guess the number: "))
        if guess == rnd:
            print("You win!")
            break
        elif guess > rnd:
            print("Too High")
        elif guess < rnd:
            print("Too Low")


play()
