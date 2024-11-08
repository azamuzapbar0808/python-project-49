import random


def get_question_and_answer():
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer
