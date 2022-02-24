# Coding Challenge 3, hangman.py
# Name:NirajLamichhane
# Student No: 2059514

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
print("Welcome to Hangman Ultimate Edition ")
print("I am thinking of a word that can have any  letters.")
import random #Import random class.

temp = []
alpha ="'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'"
get = list(alpha)
chance= 8

correct = True


def random_words():                    # using function random
    file = open("words.txt", "r")
    read = file.read()
    lists = list(read.split(" "))      # converting the data  into list format.
    word = random.choice(lists)
    return word.lower()


s = random_words()
print(s)
def is_word_guessed(guess):     # function used
    temp.append(guess)
    if guess in get:
        get.remove(guess)
        alpha = "".join(get)
    else:
        print("Oops! You've already guessed that letter")


def guessed_word(correct,alpha,chance):
    while correct:
        print("your remaining choice", alpha, "and chances", chance)
        guess = input("enter your guess:").lower()
        is_word_guessed(guess)
        if guess not in s:
            chance -= 1
            print("Oops! That letter is not in my word")
            if chance == 0:
                reak
        else:
            print("Good Guess")
        correct = False
        for x in s:
            if x not in temp:
                correct = True
        for x in s:
            if x in temp:
                print(x, end="")
            else:
                print("_", end="")
        print("")
    if not correct:
        print("Congrulation you found the word", s)
    else:
        print("soory,you ran out of guesses the word was", s)
result = guessed_word(correct,alpha,chance)
