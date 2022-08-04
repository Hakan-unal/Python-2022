print(True+False+50)
print(int(True))
print(float(False))


x=30

sonuc=5<x<25
sonuc=(5<x)and(x<25)
sonuc=(5<x)or(x<25)
sonuc=not(5<x)



print(sonuc)


#Uygulama


number=int(input("Please enter number: "))

result1=(50<number)and(number<100)

if(result1):print("number is  range 50-100")
else:print("number is not  range 50-100")

result2=(0<number)and(number%2==1)

if(result1):print("number is  odd and positive")
else:print("number is not  odd and positive")


user="test@test.com"
password="123456"

inputUser=input("please enter inputUser: ")
inputPassword=input("please enter inputPassword: ")

if(inputUser==user and inputPassword==password ):print("Login")
else:print("Invalid")


number1=int(input("Please enter number1: "))
number2=int(input("Please enter number2: "))
number3=int(input("Please enter number3: "))

resultA=(number1<number2)and(number2<number3)
resultB=(number1<number3)and(number3<number2)
resultC=(number3<number2)and(number2<number1)
resultD=(number3<number1)and(number1<number2)
resultE=(number2<number1)and(number1<number3)
resultF=(number2<number3)and(number3<number1)


if(resultA):print("number1<number2<number3")
elif(resultB):print("number1<number3<number2")
elif(resultC):print("number3<number2<number1")
elif(resultD):print("number3<number1<number2")
elif(resultE):print("number2<number1<number3")
elif(resultF):print("number2<number3<number1")


userName=input("please enter username: ")
userWeight=float(input("please enter user weight: "))
userHeight=float(input("please enter user height: "))


user={
    "name":userName,
    "weight":userWeight,
    "height":userHeight
}



userIndex=user.get("weight")/((user.get("height")/100)**2)

ındex1=(0<userIndex)and(userIndex<18.4)
ındex2=(18.5<userIndex)and(userIndex<24.9)
ındex3=(25<userIndex)and(userIndex<29.9)
ındex4=(30<userIndex)and(userIndex<34.9)

if(ındex1):print(f"Zayıf {userIndex}")
elif(ındex2):print(f"Normal {userIndex}")
elif(ındex3):print(f"Fazla Kilolu {userIndex}")
elif(ındex4):print(f"Şişman {userIndex}")
else:print("Invalid")



listA,listB=[1,2,3],[1,2,3]
listC=[1,2,3]


print(listA is listC)
print(listA is listB)
print(listA == listC)
print(listA == listB)

print(1 in listB)
print(5 is listB)



