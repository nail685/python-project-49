import random

QUEST = 'Find the greatest common divisor of given numbers.'


def get_greatest_divisor(num1, num2):
    """Search and return greatest divisor """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def get_question_and_correct_answer():
    """
    Creates two random numbers.
    Returns the game question and the correct answer.
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f'{num1} {num2}'
    right_answer = get_greatest_divisor(num1, num2)
    return question, right_answer
