import random

#My initial code
def joguempo():
    while True:
        
        adversary = random.choice(["rock", "paper", "scissors"])
        user = input("select your option: pedra, paper or scissors. (press X for endgame)")
        
        if(user == adversary):
            print("Adversario escolheu:"+adversary)
            print("Emparte")
            
        elif(user == "paper" and adversary == "rock"):
            print("Adversario escolheu:"+adversary)
            print("Voce ganhou")
            
        elif(user == "scissors" and adversary == "paper"):
            print("Adversario escolheu:"+adversary)
            print("Voce Ganhou")
            
        elif(user == "rock" and adversary == "scissors"):
            print("Adversario escolheu:"+adversary)
            print("Voce ganhou")
        
        elif(user == "x" or user == "X"):
            break
        else:
            print("Adversario escolheu:"+adversary)
            print("Voce Perdeu")


#implementation of optimized code
def play_jogempo():

    victory_rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    options = ["paper", "rock", "scissors"]

    while True:

        user = input(f"Select you play ({', '.join(options)}) or press X for endgame: ").lower().strip()
        adversary = random.choice(options)

        if(user == "x"):
            print("-=- Game Over -=-")
            break

        if(user not in options):
            print("select a valid option")
            continue

        print("Adversary plays: " + adversary)

        if(user == adversary):
            print("empate")
        elif(victory_rules[user] == adversary):
            print("Voce ganhou")
        else:
            print("Voce perdeu")

        print("-=-" * 12)
        print(victory_rules)
        print("-=-" * 12)
        print(victory_rules[user])


play_jogempo()