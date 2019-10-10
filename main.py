"""
Hanged man game for dummies
"""

from random import choice

MAX_ERRORS = 10


def get_word():
    words = ['mesa', 'silla', 'armario', 'estanteria', 'ventilador']
    return choice(words)


def draw_word(sel_word, sel_letters):
    result = []
    for char in sel_word:
        if char in sel_letters:
            result.append(char)
        else:
            result.append('_')
    return ''.join(result)


def start():
    found = False
    current_errors = []
    selected_letters = []
    selected_word = get_word()
    print(selected_word)

    while not found and len(current_errors) < MAX_ERRORS:
        # show word as we go and ask for another letter
        drawed_word = draw_word(selected_word, selected_letters)
        print(drawed_word)
        if '_' not in drawed_word:
            found = True
            break

        letter = input('Type a letter: ')
        if letter in selected_letters:
            print('Letter {} already proposed'.format(letter))
            continue

        selected_letters.append(letter)
        if letter not in selected_word:
            current_errors.append(letter)
            print('ups: wrong letter! Remain {} errors'.format(
                MAX_ERRORS - len(current_errors))
            )

    if found:
        print('YAY, word found!!!')
    else:
        print('Ohhhhh, sorry, you\'re hanged!!!')


if __name__ == '__main__':
    start()
