from random import randint
from PIL import Image
x = ["Rock", "Scissors", "Paper"]
i = 1
j = 1
n = 1
while i < 6:
    computer = x[randint(0, 2)]
    print("Rock, Paper, Scissors? \U0001F9D0")
    me = input()
    if me == computer:
        print("You both selected the same object \U0001f636")
    elif me == "Rock":
        if computer == "Paper":
            print("Your opponent gets a point \U0001F622")
            n += 1
        else:
            print("You get a point \U0001F973")
            j += 1
    elif me == "Paper":
        if computer == "Scissors":
            print("Your opponent gets a point \U0001F622")
            n += 1
        else:
            print("You get a point \U0001F973")
            j += 1
    elif me == "Scissors":
        if computer == "Rock":
            print("Your opponent gets a point \U0001F622")
            n += 1
        else:
            print("You get a point \U0001F973")
            j += 1
    else:
        print("We can't figure out which object you selected \U0001F636")
    i += 1
if j > n:
    print("The winner is You.")
    img = Image.open("youwin.jpg")
    img.show()
elif n > j:
    print("You lost.")
    img = Image.open("youwin.jpg")
    img.show()
elif n == j:
    print("There is not any winner!!!")
