import datetime
time=datetime.datetime.now()

# name=input("please enter your name: ")
# age=int(input("please enter your age: "))
# education=input("please enter your education: ")

# result1=""

# if((age>18)and (education=="lise")or(education=="üniversite")):result="Ehliyet alabilir"
# else:result1="Ehliyet alamaz"

# print(result1)


# scor1=int(input("please enter scor1: "))
# scor2=int(input("please enter scor2: "))
# scor3=int(input("please enter scor3: "))

# result2=(scor1+scor2+scor3)/3

# if((0<result2)and(result2<24)):print("0")
# elif((25<result2)and(result2<44)):print("1")
# elif((45<result2)and(result2<54)):print("2")
# elif((55<result2)and(result2<69)):print("3")
# elif((70<result2)and(result2<84)):print("4")
# elif((85<result2)and(result2<100)):print("5")
# else: print("Invalid score not")



carAge=int(input("Car year: "))
result3=time.year-carAge

if(result3==1):print("1. bakım")
if(result3==2):print("2. bakım")
if(result3==3):print("3. bakım")
else:print("bakımsız")

print(time.year)