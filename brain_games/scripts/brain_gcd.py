import random
import prompt
import math


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0

    while correct_answers < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        correct_answer = math.gcd(a, b)

        print(f'Question: {a} {b}')
        answer = prompt.string('Your answer: ')

        if answer.isdigit() and int(answer) == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f" Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
