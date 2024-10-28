# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:36:05 2021

@author: thatguy 
"""    
from termcolor import colored  
from colorama import Fore, Style
from random import choice  
 
words = ['arMan','Ali']    
word = choice(words).casefold()
vague_word = '*' * len(word)

count_wrong_guess = 0  
count_round = 0 

guess_right_memory = {}
guess_wrong_memory = {}

def word_crafter(main_word, letter):
    '''
    This function crafts the vague worlds we need: 
    for Example: ***a**
    

    Parameters
    ----------
    main_word : str
        The original word.
    letter : str
        A letter to craft a vague word.

    Returns
    -------
    vague_word : str
        The vague world crafted using main_word and letter.

    '''
    global vague_word
    vague_word = vague_word.lower()
    vague_word_temp = '*' * len(vague_word)
    repeat_count = main_word.count(letter)
    letter_index = 0
    
    for i in range(repeat_count):
        letter_index = main_word.find(letter, letter_index)
        vague_word = vague_word[:letter_index] + letter.upper() + vague_word[letter_index + 1 :]
        vague_word_temp = vague_word_temp[:letter_index] + letter + vague_word_temp[letter_index + 1 :]
        letter_index += 1
    guess_right_memory[letter] = vague_word_temp
    return vague_word
    

while True:
    # if count_wrong_guess == len(word):
    #     print('You lose!')
    #     break
    try:
        guess = input(f'Round {count_round} - Guess a Letter: ').casefold().strip()
        if len(guess) == 0 or len(guess) > 1:
            raise ValueError
        if not guess.isalpha():
            raise TypeError
    except ValueError:
        print('Your Guess Should Be EXACTLY ONE Letter!')
        continue
    except TypeError:
        print('Your Guess Should Be a LETTER!')
        continue
    if guess in guess_right_memory.keys():
        print(f'''See, You Already Guessed This Letter and It was RIGHT:\n{guess_right_memory.get(guess).upper()}
              ''')
        continue
    if guess in guess_wrong_memory:
        print(f'Already Guessed This Letter at Round {guess_wrong_memory.get(guess)} And It Was WRONG!')
        continue
    if guess in word:
        crafted = word_crafter(word, guess)
        count_round += 1
        if word == crafted.casefold():
            print('Congrats! You Win!')
            print(f'The Correct Word Was: {crafted.title()}')
            break
        print(crafted)

    else:
        
        count_wrong_guess += 1
        guess_wrong_memory[guess] = count_round
        count_round += 1
        if count_wrong_guess == len(word):
            print('You Lose!')
            break
        print(f'''\'{guess.upper()}' is a wrong guess\n{len(word) - count_wrong_guess} more wrong guesses and you LOSE!'''.title())
        

    
    
    


