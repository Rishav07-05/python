# Q1. Found the word from practice txt file 

# f = open("practice.txt")

# data = f.read()

# if("Twinkle" in data):
#     print("Found")
# else:
#     print("Not Found")
   
# f.close()


# Q2. Check the highscore 

# import random 

# def game():
#     print("You are playing the game")
#     score = random.randint(1,69)
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"your score: {score}")
#     if(score > hiscore or hiscore == ""):
#         with open("hiscore.txt" , "w") as f:
#             f.write(str(score))
#     return score 

# game()


# Q3. Program to write table from 2 to 20


# def generateTable(n):
#     table =  ""
#     for i in range(1,11):
#         table+= f"{n} X {i} = {n*i}\n"
#     with open(f"table/table_{n}.txt" , "w") as f:
#         f.write(table)

# for i in range(1,21):
#     generateTable(i)



# Q4. Replace the word "Rishav" with "Batman"

# word = "Rishav"

# with open("replace.txt" , "r") as f:
#     data = f.read()

# newData = data.replace(word , "Batman")

# with open("replace.txt" , "w") as f:
#     data = f.write(newData)