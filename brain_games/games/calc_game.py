import random


def generate_round():
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
