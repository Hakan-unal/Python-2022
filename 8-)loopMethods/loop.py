#uygulama 1

# for i1 in range(1,11):
#     print("*****")
#     for i2 in range(1,11):
#         print(f"{i1}*{i2}=  {i1*i2}")


# number=int(input("please enter number: "))
# result=True
# for i in range (2,number):
#     if(number%i==0):
#         result=False
#         break

# print(f"is Asal {result}")



#Uygulama 2

import random

# number=random.random()
# randomNumber=round(number*100)
randomNumber=random.randint(1,100)
hak=6

while (hak>0):
        
    hak-=1

    userChoice=int(input("Please enter number: "))
    if(userChoice==randomNumber):
        print("Congralations")
        break
    elif(userChoice<randomNumber):print("Higher")
    elif(userChoice>randomNumber):print("Lower")
    if(hak==0):print("Lose")


