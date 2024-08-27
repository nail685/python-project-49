import prompt

NUMBER_OF_ROUNDS = 3


def start_game(game):
    """ Logic games. Greeting, check answer, output """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.QUEST}')
    for _ in range(NUMBER_OF_ROUNDS):
        question, right_answer = game.get_question_and_correct_answer()
        right_answer = str(right_answer)
        answer = prompt.string(f'Question: {question}\n'
                               f'Your answer: ')
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer is '{right_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
