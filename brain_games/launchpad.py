import prompt


def launch_game(game_module):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    game_descriptions = {
        'brain_games.games.calc_game':
            "What is the result of the expression?",
        'brain_games.games.even_game': 'Answer "yes" if the number is even, '
                                       'otherwise answer "no".',
        'brain_games.games.gcd_game':
            'Find the greatest common divisor of given numbers.',
        'brain_games.games.progression_game':
            'What number is missing in the progression?',
        'brain_games.games.prime_game':
            'Answer "yes" if given number is prime. Otherwise answer "no".'
    }

    description = game_descriptions.get(game_module.__name__)
    print(description)

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
