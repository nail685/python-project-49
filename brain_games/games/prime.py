#!/usr/bin/env python3
import random

QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """
    Returns an prime number or not
    """
    i = 2
    while i < num / 2:
        if num % i == 0:
            return False
        i += 1
    return True


def get_question_and_correct_answer():
    """Creates a random number.
    Returns the game question and the correct answer.
    """
    num = random.randint(2, 200)
    question = f'{num}'
    if is_prime(num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
