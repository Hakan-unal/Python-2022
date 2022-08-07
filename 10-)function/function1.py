def calculator(a,b):
    result=""
    if(a>b):result="a>b"
    if(b>a):result="b>a"
    if(a==b):result="a=b"
    return result
number1=int(input("Please enter a number: "))
number2=int(input("Please enter b number: "))
print(calculator(number1,number2))




def stringCalc(string):
    obj={}
    for char in string:
        obj[char]=string.count(char)

    return obj

print(stringCalc("Hello Hello Hello hello"))


def calculate (arr,command,position,value):
    if(command=="add"):
        if(position=="beginning"):
            arr.insert(0,value)
        else: arr.insert(len(arr),value)

    elif(command=="remove"):
        if(position=="beginning"):
            arr.pop(0)
            arr.remove(value)
        else: 
            arr.pop(len(arr)-1)
            arr.remove(value)

    return arr

result=calculate([1,2,3,4,5],"remove","end",4)
print(result)



def colorCalculator(*args):
    arr=[]
    for i in args:
        if(i.count("blue")!=0):
            arr.append((i,True))

    return arr


print(colorCalculator("blue","orange","yellow","dark"))
print("test".count("h"))