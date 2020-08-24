'''
Created on 24-Aug-2020

@author: Sanjay Ghosh
'''
import random;

MAX_TURNS = 10
WORDS = ['rainbow', 'computer', 'science', 'programming', 
             'mathematics', 'player', 'condition', 'reverse', 
             'water', 'board', 'geeks'] 
  

def choose():    
  return random.choice(WORDS) 
  
    


def jumble(word): 
    random_word = random.sample(word, len(word))   
    jumbled = ''.join(random_word) 
    return jumbled 

def game():
  turns = 0;
  choice = choose();
  print("Jumbled word:" + jumble(choice))
  while(turns < MAX_TURNS):
    turns = turns + 1;
    user_in = str(input("Enter your guess:"));    
    if choice == user_in:
      print("Correct! You Won!")
      break;
    else:
      print("Wrong! You have " + str(MAX_TURNS - turns) +" turns left")    
  if turns >= MAX_TURNS:
    print("You Lost! Sorry!");

game();