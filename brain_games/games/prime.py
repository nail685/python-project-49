#!/usr/bin/env python3
import prompt
import random


def prime(n):
    sieve = [True] * n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return primes


def game(name):
    i = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:
        num = random.randint(2, 200)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        right_answer = ''
        n = 200
        primes = prime(n)
        if num in primes:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if num in primes and answer == 'yes':
            print('Correct!')
        elif num not in primes and answer == 'no':
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{right_answer}'. \nLet's try again, {name}!")
            break
        i += 1
    if i == 3:
        print(f'Congratulations, {name}!')
