# Basic game rules 
# 1 => Snake
# -1 => Water
# 0 => Gun

import random


computer =  random.choice([1, 0, -1])
yourInputStr = input("Enter your choice: ")
yourDict =  {"Snake" : 1,"Water" : -1,"Gun" : 0}
yourInputNum = yourDict[yourInputStr]

if(computer == yourInputNum):
    print("It's a draw")

else:
    if(computer == 1 and yourInputNum == -1):
        print("You Lose")
    elif(computer == -1 and yourInputNum == 1):
        print("You Win")
    elif(computer == 0 and yourInputNum == -1):
        print("You Win")
    elif(computer == 0 and yourInputNum == 1):
        print("You Lose")
    elif(computer == 1 and yourInputNum == 0):
        print("You Win")
    elif(computer == -1 and yourInputNum == 0):
        print("You Lose")
    else:
        print("Something Went Wrong")