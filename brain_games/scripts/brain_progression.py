import random
import prompt


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = list(range(start, start + step * length, step))
    return progression


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    correct_answers = 0

    while correct_answers < 3:
        progression = generate_progression()
        missing_index = random.randint(0, len(progression) - 1)
        correct_answer = progression[missing_index]
        progression[missing_index] = '..'
        print('Question:', ' '.join(map(str, progression)))
        answer = prompt.string('Your answer: ')
        if answer.isdigit() and int(answer) == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was: '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
