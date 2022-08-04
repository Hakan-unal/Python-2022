# a,b,c=2,5,10

# inputA=int(input("enter first number: "))
# inputB=int(input("enter second number: "))

# result1=inputA*inputB
# result2=a+b+c
# result3=result1-result2


# print(result1)
# print(result2)
# print(result3)

# print(c//b)
# print(result2%3)



# numbers=(1,5,7,10,3)


# d,*e,f=numbers

# print(f**3)
# g=0

# for data in e:
#     g+=data

# print(g)




#Uygulama


a=int(input("please enter a: "))
b=int(input("please enter b: "))
c=int(input("please enter c: "))


if(a>b):print("a bigger than b")
elif(a<b):print("b bigger than a")
elif(a==b):print("a equal to b")


if(c%2==0):print("c number is even")
elif(c%2==1):print("c number is odd")

if(c>0):print("c number is positive")
elif(c<0):print("c number is negative")


visit1=int(input("please enter visit1: "))
visit2=int(input("please enter visit2: "))
final=int(input("please enter final: "))

calculate=((visit1+visit2)/2*60/100)+(final*40/100)

sonuc=""

if(calculate<50):sonuc="Kaldı"
if(calculate>=50):sonuc="Geçti"


print(f"your result: {sonuc,calculate}")


user="test@test.com"
password="123456"

inputUser=input("please enter inputUser: ")
inputPassword=input("please enter inputPassword: ")

if(inputUser==user and inputPassword==password ):print("Login")
else:print("Invalid")


