a = int(input("Enter our age: "))

# if else ladder

if(a>=18):
    print("You are above the age of consent :-) ")
    print("That's good for you")

elif(a<0):
    print("Age couldn't be in negative format")

elif(a==0):
    print("You are entering your age as zero")

else:
    print("You are below the age of consent :-( ")