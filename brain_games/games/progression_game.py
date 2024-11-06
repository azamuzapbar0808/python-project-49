import random


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = list(range(start, start + step * length, step))
    missing_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
