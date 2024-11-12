import prompt
from brain_games.cli import welcome_user


def launch_game(game_module):
    print(game_module.DESCRIPTION)
    name = welcome_user()
    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game_module.get_question_and_answer()
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
