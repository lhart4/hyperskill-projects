# Write your code here
import random


def update_hint(hint, solution, guess):
    if guess in solution:
        i = -1
        hint_list = list(hint)
        for _ in range(solution.count(guess)):
            j = solution[i+1:].find(guess)
            hint_list[i + 1 + j] = guess
            i = j
        return ''.join(hint_list)
    else:
        return hint


print('H A N G M A N')
play_or_exit = input('Type "play" to play the game, "exit" to quit:')

possibles = {'python': '------', 'java': '----', 'kotlin': '------',
             'javascript': '----------'}

solution = random.choice(list(possibles.keys()))
hint = possibles[solution]
hint_list = []
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
counter = 0

if play_or_exit == 'play':
    while counter != 8:
        print()
        print(hint)
        guess = input('Input a letter: ')
        guess_list = list(guess)
        hint = update_hint(hint, solution, guess)
        if len(guess_list) >= 2:
            print('You should input a single letter')
        elif guess in english and guess.islower:
            if hint == solution:
                print()
                print(solution)
                print('You guessed the word!')
                print('You survived!')
                break
            if guess in hint_list:
                print('You already typed this letter')
                continue
            if guess not in solution:
                print('No such letter in the word')
                counter += 1
        else:
            print('It is not an ASCII lowercase letter')
        hint_list.append(guess)
    if counter == 8:
        print('You are hanged!')