import random
import time

compeuter = random.randint(0, 2)
print("This is a game of rock paper scissors")
time.sleep(1)
userInput = str(input("Do you want to play? Enter Y for yes N for no: "))

if userInput == "Y":
  print("GAME ON!")
  matt = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
  if matt == 0:  
    print("you chose rock")
    print("""
    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)
  elif matt == 1:
    print("you chose paper")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """)
  else:
    print("you chose scissors")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
  if compeuter == 0:
    print("A.I chose rock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)
  elif compeuter == 1:
    print("A.I chose paper")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """)
  else:
    print("A.I chose scissors")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)
  if matt == compeuter:
    print("DRAW!")
  elif matt == 0 and compeuter > 1:
    print("You win! Rock evaporates scissors!")
  elif matt == 1 and compeuter > 1:
    print("A.I. wins! scissors cuts paper")
  elif matt > 1 and compeuter == 0:
    print("A.I. wins! rock crushes scissors")
  elif matt == 1 and compeuter == 0:
    print("you win! paper eats rock")
  elif matt == 0 and compeuter == 1:
    print("A.I. wins! paper sqeezez rock into peices")
  else:
    print("You win! scissors cuts paper")
   
else:
  print("you suck!")

