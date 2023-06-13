import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice=int(input("What do you chooose? Type 0 for Rock, 1 for Paper or 2 fpr Sissors."))
if(choice==0):
  print(rock)
if(choice==1):
  print(paper)
if(choice==2):
  print(scissors)
print("computer choice is :")
comp_choice=random.randint(0,2)
t=0

if(comp_choice==0):
    print(rock)
if(comp_choice==1):
    print(paper)
if(comp_choice==2):
    print(scissors)
t==0 
if(choice==comp_choice):
    print("its a draw")
    t=1
if(choice==2 and comp_choice==0):
    print("You Lose")
    t=1
    
if(choice==1 and comp_choice==2):
    print("You Lose")
    t=1
    
if(choice==0 and comp_choice==1):
    print("You Lose")
    t=1
    
if(t==0):
  print("you win")


                 
