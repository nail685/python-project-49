#!/usr/bin/env python3
import random

QUEST = 'What number is missing in the progression?'


def get_question_and_correct_answer(c):
    num = random.randint(1, 100)
    d = random.randint(5, 15)
    prog = list(range(num, num + d))
    z = random.randint(1, d - 1)
    prog2 = prog.copy()
    prog2[z] = '..'
    question = ' '.join(str(num) if num != '..' else num for num in prog2)
    right_answer = prog[z]
    return question, str(right_answer), c
