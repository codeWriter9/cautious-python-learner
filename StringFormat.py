'''
Created on 25-May-2019

@author: Sanjay Ghosh
'''
from random import randrange;

def randomize(actual, guess):
    while True:
        if actual > guess:
            print("You guessed too low");
            guess = int(input(" Enter a number between 1 and 100:"));
        elif actual < guess:
            print("You guessed too high");
            guess = int(input(" Enter a number between 1 and 100:"));
        elif guess == actual :
            print("Correct.");
            print(" Number : " + str(actual));
            print(" Guess  : " + str(guess));
            break;
    

actual = randrange(1, 100, 1);
guess = int(input(" Enter a number between 1 and 100:"));
randomize(actual, guess);