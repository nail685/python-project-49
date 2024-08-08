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


def game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    score = 0
    while i < 3:
        num = random.randint(2, 200)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        right_answer = ''
        n = 200
        primes = prime(n)
        if num in primes and answer == 'yes':
            score += 1
            print('Correct!')
        elif num not in primes and answer == 'no':
            score += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{right_answer}'. \nLet's try again, {name}!")
            break
        i += 1
    if score == 3:
        print(f'Congratulations, {name}!')


def main():
    game()


if __name__ == '__main__':
    main()
