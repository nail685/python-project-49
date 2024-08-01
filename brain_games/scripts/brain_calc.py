#!/usr/bin/env python3
import prompt
import random


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    score = 0
    num = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sum_num = num + num2
    print(f'What is the result of the expression?".'
          f'\nQuestion: {num} + {num2}')
    answer = prompt.string('Your answer: ')
    if sum_num == int(answer):
        score += 1
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was"
              f" '{sum_num}'. \nLet's try again, {name}!")
    num = random.randint(1, 100)
    num2 = random.randint(1, 100)
    diff_num = num - num2
    print(f'Question: {num} - {num2}')
    answer = prompt.string('Your answer: ')
    if diff_num == int(answer):
        score += 1
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was"
              f" '{diff_num}'. \nLet's try again, {name}!")
    num = random.randint(1, 100)
    num2 = random.randint(1, 100)
    multiplication = num * num2
    print(f'Question: {num} * {num2}')
    answer = prompt.string('Your answer: ')
    if multiplication == int(answer):
        score += 1
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was"
              f" '{multiplication}'. \nLet's try again, {name}!")
    if score == 3:
        print(f'Congratulations, {name}!')


def main():
    calc()


if __name__ == '__main__':
    main()
