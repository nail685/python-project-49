#!/usr/bin/env python3
import random

QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(n):
    sieve = [True] * n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return primes


def get_question_and_correct_answer(c):
    num = random.randint(2, 200)
    question = f'{num}'
    n = 200
    primes = prime(n)
    if num in primes:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer, c
