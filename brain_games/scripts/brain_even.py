import random
import prompt


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if answer not in ['yes', 'no']:
            print(f"'{answer}' is not a valid answer. Let's try again, {name}!")
            return

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
