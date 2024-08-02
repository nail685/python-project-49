#!/usr/bin/env python3
import prompt
import random


def game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    i = 0
    score = 0
    while i < 3:
        num = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num} {num2}')
        answer = int(prompt.string('Your answer: '))
        right_answer = 0
        while num != 0 and num2 != 0:
            if num > num2:
                num = num % num2
            else:
                num2 = num2 % num
            right_answer = num + num2
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
