#!/usr/bin/env python3
import random

QUEST = 'Find the greatest common divisor of given numbers.'


def get_question_and_correct_answer(count):
    num = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f'{num} {num2}'
    while num != 0 and num2 != 0:
        if num > num2:
            num = num % num2
        else:
            num2 = num2 % num
    right_answer = str(num + num2)
    return question, right_answer, count
