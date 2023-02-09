import random
import sys
def choose_word(list_of_words):
    return random.choice(list_of_words).upper()


def show_dashes(word):
    blank_list = []
    for i in range(len(word)):
        blank_list.append("_ ")
    return blank_list


def find_char_index(char, word):
    indexes = []
    indexes = [index for index in range(len(word)) if word.startswith(char, index)]
    return indexes


def replace_blank(indexes, character, blank_list):
    for n in indexes:
        blank_list[n] = character.upper()
    return blank_list
def check_dash(word):
    if '_ ' in word:
        return False
    else:
        return True

def check_used_letters(character, let_list):
    if character.upper() not in let_list:
        let_list.append(character)
        return True, let_list
    else:
        return False, let_list


word_list = ["thanksgiving", "apple", "banana", "subaru"]
used_letters = []
lives = 6
random_word = choose_word(word_list)
dash_list = show_dashes(random_word)
print(dash_list)
print(random_word)
try_again=True

while try_again:
    while lives > 0:
        is_used = True
        print(f'Used Letters: {used_letters}')
        char = input("Enter a letter: ").upper()
        if len(char) > 1:
            print
            "Error! Only 1 characters allowed!"
            sys.exit(0)
        is_used, used_letters = check_used_letters(char, used_letters)
        if not is_used:

            is_used = True
            print('You already picked that letter Try again')

        indices = find_char_index(char, random_word)
        if len(indices) > 0:
            dash_list = replace_blank(indices, char, dash_list)
            print(dash_list)
        else:
            lives = lives - 1
            print(f'Wrong! Letter is not in the word you only have {lives} left')
        complete=check_dash(dash_list)
        if complete:
            break
    if complete and lives>0:
        print('Congratulations you won!')
    else:
        print('Sorry You lost')
    play_again=input('Do you an to play again? (y or N) ')
    if play_again.upper() == 'Y':
        try_again=True
        Lives=6
    else:
        try_again=False
        print('Thanks for playing!')
