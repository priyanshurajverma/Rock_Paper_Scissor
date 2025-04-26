import random

choice=input("Enter your chhoices r-rock p-paper s-scissor").lower()


a=['r','p','s']
computer=random.choice(a)


if(choice==computer):
    print("tie")
elif(choice=='r' and computer=='p'):
    print("You lose")
elif(choice=='p' and computer=='s'):
    print("You lose")
elif(choice=='s' and computer=='r'):
    print("You lose")
elif(choice=='p' and computer=='r'):
    print("You win")
elif(choice=='s' and computer=='p'):
    print("You win")
elif(choice=='r' and computer=='s'):
    print("You win")
else:
    print("Wrong Option")