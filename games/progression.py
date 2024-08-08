#!/usr/bin/env python3
import prompt
import random


def game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    i = 0
    score = 0
    while i < 3:
        num = random.randint(1, 100)
        d = random.randint(5, 10)
        prog = list(range(num, num + d + 1))
        z = random.randint(1, d - 1) - 1
        prog2 = prog.copy()
        prog2[z] = '..'
        print("Question:", *(prog2), sep=' ')
        answer = int(prompt.string('Your answer: '))
        right_answer = prog[z]
        if right_answer == answer:
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
