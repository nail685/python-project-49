import random
from brain_games.games.const import MATH_SIGNS

QUEST = 'What is the result of the expression?'


def get_result_expression(num1, num2, math_sign):
    """Return result mathematical expression."""
    match math_sign:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError('Math sign not found')


def get_question_and_correct_answer():
    """
    Creates two random numbers.
    Returns the game question and the correct answer.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    math_sign = random.choice(MATH_SIGNS)
    question = f'{num1} {math_sign} {num2}'
    right_answer = get_result_expression(num1, num2, math_sign)
    return question, right_answer
