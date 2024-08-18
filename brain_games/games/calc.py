#!/usr/bin/env python3
import random

QUEST = 'What is the result of the expression?'


def get_question_and_correct_answer(c):
    chars = ['+', '-', '*']
    num = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f'{num} {chars[c]} {num2}'
    if c == 0:
        right_answer = num + num2
        return question, str(right_answer), c
    elif c == 1:
        right_answer = num - num2
        return question, str(right_answer), c
    else:
        right_answer = num * num2
        return question, str(right_answer), c
