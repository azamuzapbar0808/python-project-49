import random


def get_question_and_answer():
    print("What is the result of the expression?")
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        correct_answer = a + b
    elif operation == '-':
        correct_answer = a - b
    else:
        correct_answer = a * b

    question = f"{a} {operation} {b}"
    return question, correct_answer
