#!/usr/bin/env python3
import prompt
import random


def game(name):
    print('What is the result of the expression?')
    chars = ['+', '-', '*']
    score = 0
    for char in chars:
        num = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(f'Question: {num} {char} {num2}')
        answer = prompt.string('Your answer: ')
        rezalt = 0
        if char == '+':
            rezalt = num + num2
        elif char == '-':
            rezalt = num - num2
        else:
            rezalt = num * num2
        if rezalt == int(answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was"
                  f" '{rezalt}'. \nLet's try again, {name}!")
            return exit
        score += 1
    if score == 3:
        print(f'Congratulations, {name}!')
