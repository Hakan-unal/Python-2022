# i=0
# while (i<10):
#     print("test")
#     i+=1


# username=""

# while not username:
#     username=input("please enter username: ")


# print(username)



# #uygulama 1

# numbers=[4,6,9,10,35,57,89,125,244]

# numbersLength=len(numbers)
# i=0
# while (i<numbersLength):
#     print(numbers[i])
#     i +=1


# startPoint=int(input("please enter startPoint: "))
# endPoint=int(input("please enter endPoint: "))


# index=0
# while (index<numbersLength):
#     if((startPoint<numbers[index])and(numbers[index]<endPoint)and(numbers[index]%2==1)):
#         print(numbers[index])
#     index +=1

# index1=0
# arr=[]
# while (index1<5):
#     number=int(input("please enter number: "))
#     arr.append(number)
#     index1 +=1

# print(arr)
# arr.sort()
# print(arr)



#uygulama 2



productCount=int(input("please enter product conunt: "))
index=0
arr=[]
while(index<productCount):
    name=input("please enter product name: ")
    price=int(input("please enter product price: "))
    obj={
        "name":name, 
        "price":price
    }
    arr.append(obj)
    index+=1

i=0
while(i< len(arr)):
    print(arr[i])
    i+=1



