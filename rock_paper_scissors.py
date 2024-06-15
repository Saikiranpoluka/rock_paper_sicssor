import random
user=int(input("enter your choice:type 0 for rock,1 for paper,2 for scissors."))
if user >=3 or user <0:
    print("you entered invalid number,you lose.")
computer=random.randint(0,2)
print("computer chose:")
print(computer)
if computer == user:
    print("it's a draw")
elif computer ==0 and user ==2:
    print("you lose")
elif user ==0 and computer ==2:
    print("you win")
elif computer > user:
    print("you lose")
elif user > computer:
    print("you win")