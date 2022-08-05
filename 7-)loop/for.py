
# #for



# numbers=[1,2,3,4,51,6,7,90]
# names=["ali","veli","49 50"]
# name="ali veli"
# tupleArr=[(1,2),(4,5),(7,8)]
# obj={"n1":"123","n2":"1234","n3":"12345",}

# def test(value,val):
#     print(f"{value,val}")


# for number in numbers:
#     test(number,"")

# for nam in names:
#     test(nam,"")

# for char in name:
#     test(char,"")

# for arr in tupleArr:
#     test(arr,"")

# for arr,value in tupleArr:
#     test(arr,value)

# for x in obj:
#     print(x)

# for x in obj:
#     print(obj[x])

# for x in obj.values():
#     print(x)

# for key,value in obj.items():
#     print(key)
#     print(value)


# for i in range(2):
#     test(i)





#uygulama 1


# numbers=[1,5,15,35,57,72]
# products=["IPHONE 8","IPHONE X","IPHONE XR","SAMSUNG S10"]

# for value in numbers:
#     print(value)

# for value in numbers:
#     if(value%5==0):print(value)

# result=0
# for value in numbers:
#     result += value

# print(result)


# for value in numbers:
#     if(value%2==0):print(value**2)

# for value in products:
#     print(value[1])

# result=0
# for value in products:
#     if(value.lower().find("iphone")!=-1):result+=1

# print(result)


    
# obj={
#     "key":"value"
# }

# print(obj["key"])
# print(obj.get("key"))




#uygulama 2



products=[
    {"name":"iphone 8","price":"4000"},
    {"name":"iphone 8 plus","price":"5000"},
    {"name":"iphone x","price":"6000"},
    {"name":"iphone xr","price":"7000"},
    {"name":"iphone 11","price":"8000"},
    {"name":"iphone s10","price":"9000"},
    {"name":"iphone s8","price":"6000"},
    {"name":"iphone 11 plus","price":"8000"},
]




for obj in products:
    print(obj)

result=0


for obj in products:
    result+=int(obj.get("price"))

print(result)

for obj in products:
    if(int(obj.get("price"))<=6000):print(obj)



query=input("please enter query: ")


for obj in products:
    if(obj.get("name").find(query)!=-1):print(obj)