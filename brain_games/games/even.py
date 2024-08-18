#!/usr/bin/env python3
import random

QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer(c):
    num = random.randint(1, 100)
    question = f'{num}'
    if num % 2 == 0:
        right_answer = 'yes'
    elif num % 2 != 0:
        right_answer = 'no'
    return question, right_answer, c
