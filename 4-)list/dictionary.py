# #tuple


# list=[1,2,3]
# tuple=(1,2,3)

# print(type(list))
# print(type(tuple))



# obj={
#     "name":"name1",
#     "surname":"surname1",
#     "age":15
# }

# obj1={
#     "name":"name1",
#     "surname":"surname1",
#     "age":15,
#     1:{"name":"name2","surname":"surname2","age":12},

# }


# obj2={
#     1:{"name":"a","surname":"b"},
#     2:{"name":"aa","surname":"bb"},
#     3:{"name":"aaa","surname":"bbb"},
# }

# print(obj["name"])

# obj["date"]="22.22.2222"

# print(obj1[1])
# print(obj2[1])
# print(obj2)



#uygulama


tempObj={}

for i in range(3):
    productID=int(input(f"{i+1}. ürün id'si: "))
    productName=input(f"{i+1}. ürün name'i: ")
    productPrice=input(f"{i+1}. ürün price'ı: ")

    tempObj[productID]={
        "name":productName,
        "price":productPrice
        }
  

print(tempObj)



queryID=int(input(f"Sorgulamak istediğiniz ürün id: "))


print(tempObj[queryID])





