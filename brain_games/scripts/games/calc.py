#!/usr/bin/env python3
import prompt
import random


def game(name):
    chars = ['+', '-', '*']
    for char in chars:
        score = 0
        num = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(f'What is the result of the expression?".'
              f'\nQuestion: {num} {char} {num2}')
        answer = prompt.string('Your answer: ')
        rezalt = 0
        if char == '+':
            rezalt = num + num2
        elif char == '-':
            rezalt = num - num2
        else:
            rezalt = num * num2
        if rezalt == int(answer):
            score += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{rezalt}'. \nLet's try again, {name}!")
            return exit
    print(f'Congratulations, {name}!')
