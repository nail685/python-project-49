import prompt

NUMBER_OF_ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.QUEST}')
    c = 0
    for _ in range(NUMBER_OF_ROUNDS):
        question, right_answer, count = game.get_question_and_correct_answer(c)
        answer = prompt.string(f'Question: {question}\n'
                               f'Your answer: ')
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer is '{right_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
        c += 1
    print(f'Congratulations, {name}!')
