#!/usr/bin/env python3
import random

QUEST = 'What is the result of the expression?'


def result_expression(num1, num2, math_sign):
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
    var_math_sign = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    math_sign = random.choice(var_math_sign)
    question = f'{num1} {math_sign} {num2}'
    right_answer = result_expression(num1, num2, math_sign)
    return question, right_answer
