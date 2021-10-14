from random import randint

print("rock ... \npaper ... \nscissors")
player = str(input("please insert one of them : rock or paper or scissors ===>\n"))
number = randint(0, 2)
botmove = ""
if number == 0:
    botmove = "rock"
elif number == 1:
    botmove = "paper"
elif number == 2:
    botmove = "scissors"

print(f"bot move is : {botmove}")

if player == botmove:
    print("your choice and its choice are same ! ")
elif player == "rock":
    if botmove == "paper":
        print("bot wins ... !")
    if botmove == "scissors":
        print("you win ...")
elif player == "paper":
    if botmove == "rock":
        print("you win ...")
    if botmove == "scissors":
        print("bot wins ... !")
elif player == "scissors":
    if botmove == "rock":
        print("bot wins ... !")
    if botmove == "paper":
        print("you win ...")
else:
    print("somethings went wrong")

print("     Have A Good Time :)     \n")
bye = input("please insert one word to exit the game")