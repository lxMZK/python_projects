import random


def play():
    random.seed()

    numTries = validateInput('Input number of tries:')
    high = validateInput('Input upper bound: ')

    rnd = random.randint(1, high)

    for i in range(numTries):
        guess = validateInput(f"Attempt {i + 1} Guess the number: ")
        if guess == rnd:
            print("You win!")
            break
        elif guess > rnd:
            print("Too High")
        elif guess < rnd:
            print("Too Low")


def validateInput(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please input an integer.")
            continue


play()
