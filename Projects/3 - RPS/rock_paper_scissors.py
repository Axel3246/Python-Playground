import random


def winner(user, cpu):
    
    if((user == 'R' and cpu == 'S') or (user == 'P' and cpu == 'R') or (user == 'S' and cpu == 'P')):
        print("You Win!")
    elif((cpu == 'R' and user == 'S') or (cpu == 'P' and user == 'R') or (cpu == 'S' and user == 'P')):
        print("You Lose!")
        
def play():
    rps = ['R', 'P', 'S']
    user = input("Rock (R), Paper (P) or Scissors (S)? ")
    cpu = random.choice(rps)

    if(user == cpu):
        print("It's a Tie!")
    else:
        winner(user, cpu)

play()