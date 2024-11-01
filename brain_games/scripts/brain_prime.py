import random
import prompt


def is_prime(answer):
    if answer <= 1:
        return False
    for i in range(2, answer):
        if answer % i == 0:
            return False
    return True


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        a = random.randint(1, 100)
        print(f'Question: {a}')
        answer = prompt.string('Your answer: ').strip().lower()
        correct_answer = "yes" if is_prime(a) else "no"

        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
