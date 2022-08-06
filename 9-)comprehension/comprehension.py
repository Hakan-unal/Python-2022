# arr1=[1,2,3,4]
# arr2=list(range(2,500,50))
# arr3=[i**2 for i in range(1,50,3)]

# print(arr1)
# print(arr2)
# print(arr3)



# count=int(input("please enter product count: "))
# products=[]

# for i in range(count):
#     name=input(f"please enter {i+1}. product name: ")
#     price=int(input(f"please enter {i+1}. product price: "))
#     obj={
#         "name":name,
#         "price":price
#     }
#     products.append(obj)

# print(products)

# query=input("Please enter search product name: ")

# for product in products:
#     if(product.get("name")==query):
#         print(f"Product: {product}")
#         break


# tempArr=[i for i in range(1,5) if(i%2==0)]

# print(tempArr)




#uygulama


import datetime

time=datetime.datetime.now()
names=["Ahmet","ali","Çınar","DeNiz"]
string="Hello 12345 World"
years=[1983,1999,2008,1956,1986]
degress=[20,5,15,-2,0,-6]
tempArr=[i for i in range(1,101) if i%12==0]
tempArr1=[name.lower()[::-1] for name in names ]
tempArr2=[char for char in string if((char=="1")or (char=="2") or(char=="3") or(char=="4") or(char=="5")) ]
tempArr2=[char for char in string if((char.isdigit())) ]

tempArr3=[time.year-year for year in years]
tempArr4=[value if value>=0  else "buzlanma tehlikesi" for value in degress]

print(tempArr)
print(tempArr1)
print(tempArr2)
print(tempArr3)
print(tempArr4)






