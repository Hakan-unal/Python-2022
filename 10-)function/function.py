# def test1():
#     print("test")


# def test2(i):
#     print(i**2)


# def test3(i):
#     return i**2


# def test4(name,message="Test"):
#     print(f"{name}, {message}")

# def test5(a,fn):
#     return fn(a)

# def test6(firstName,lastName):
#     return f"{firstName} {lastName}"

# def test7(*args):

#     result=0
#     for i in args:
#         result+=i
#     return result


def test8(**kwargs):
    print(kwargs)

# test1()
# test2(3)
# print(test3(4))
# test4("name")
# print(test5(3,test3))
# print(test6(lastName="Hello",firstName="World"))
# print(test7(10,20,30,40,15))
test8(name="Hello",lastname="World")
test8(name="World",lastname="Hello")

# uygulama

import random
def display(string,count):
    for i in range(count):print(string)

display("Hello World",2)


def calculatorCevre(uzunKenar,kısaKenar):
    alan=uzunKenar*kısaKenar
    cevre=(uzunKenar+kısaKenar)*2
    return f"alan: {alan}, çevre: {cevre}"



print(calculatorCevre(4,6))


def toss():
    result="Yazı"
    if(random.randint(0,1)==1):result="Tura"
    return result

print(toss())


def asalCalculator(num1,num2):
    arr=[]
    for i in range(num1,num2+1):
        isAsal=True
        for index in range(2,i):
            if(i%index==0):
                isAsal=False
                break
        if(isAsal):arr.append(i)
    return arr
    

            
print(asalCalculator(2,100))




def tamBolenCalculator(number):
    arr=[]
    for i in range(1,number+1):
        if(number%i==0):arr.append(i)
    return arr

print(tamBolenCalculator(1000))
