
   ###PYTHON GAME FOR ROCK, PAPER AND SCISSORS
import random

def play():  
     user = input("Whats your choice? 'r' for rock, 'p' for paper and 's' for scissors\n")
     computer = random.choice(['r','p','s'])  #for the computer to make random choice

     if user == computer:
        return 'tie'
    
    # r>s , s>p , p>r
     if is_win(user,computer):
        return 'You won!!'
    

     return 'You lost!!'


def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
      return True  

print(play())  