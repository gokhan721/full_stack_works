import random


def generate_digits():
    digits = list(range(10))
    random.shuffle(digits)
    return [str(x) for x in digits[:3]]


def get_guess():
    return list(input("Enter your guess: "))


def clues(digits, guess):

    if digits == guess:
        return ["Correct Answer"]

    clues = []

    for ind,num in enumerate(guess):
        if num == digits[ind]:
            clues.append("match")
        elif num in digits:
            clues.append("close")

    if len(clues) == 0:
        return ["nope"]

    return clues


generated_digits = generate_digits()
print(generated_digits)
clue_report = []

while clue_report != ["Correct Answer"]:

    guess = get_guess()
    print(guess)

    clue_report = clues(generated_digits, guess)

    for clue in clue_report:
        print(clue)
