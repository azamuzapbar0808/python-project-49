import random
import math


def get_question_and_answer():
    print('Find the greatest common divisor of given numbers.')
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    correct_answer = math.gcd(a, b)
    return question, correct_answer
