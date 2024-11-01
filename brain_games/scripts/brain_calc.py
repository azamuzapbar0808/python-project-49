import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    correct_answers = 0

    while correct_answers < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])

        if operation == '+':
            correct_answer = a + b
        elif operation == '-':
            correct_answer = a - b
        else:
            correct_answer = a * b

        print(f'Question: {a} {operation} {b}')
        answer = prompt.string('Your answer: ')

        if answer.isdigit() and int(answer) == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
