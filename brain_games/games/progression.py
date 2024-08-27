import random

QUEST = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    """
    Creates a progression and hides the random number.
    Return question game and right_answer.
    """
    num = random.randint(1, 100)
    len_progression = random.randint(5, 11)
    progression = list(range(num, num + len_progression))
    hidden_num = random.randint(1, len_progression - 1)
    right_answer = progression[hidden_num]
    # print_progression = progression.copy()
    progression[hidden_num] = '..'
    question = ' '.join(str(num) for num in progression)
    # right_answer = progression[hidden_num]
    return question, right_answer
