#!/usr/bin/env python3
import prompt
import random


def game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 0
    score = 0
    while i < 3:
        num = random.randint(1, 100)
        print(f'Answer "yes" if the number is even, otherwise answer "no".'
              f'\nQuestion: {num}')
        answer = prompt.string('Your answer: ')
        if num % 2 == 0 and answer == 'yes':
            score += 1
            print('Correct!')
        elif num % 2 != 0 and answer == 'no':
            score += 1
            print('Correct!')
        else:
            right_answer = 'no' if num % 2 != 0 else 'yes'
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
