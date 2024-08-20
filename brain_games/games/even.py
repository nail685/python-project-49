#!/usr/bin/env python3
import random

QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """
    Returns an even number or not
    """
    return num % 2 == 0


def get_question_and_correct_answer():
    """
    Creates a random number.
    Returns the game question and the correct answer.
    """
    num = random.randint(1, 100)
    question = f'{num}'
    if is_even(num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
