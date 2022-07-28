# carA={
#     "marka":"opel",
#     "model":"Corsa",
#     "year":2020,
#     "country":"Türkiye",
#     "speed":120
# }



# print(carA)
# print(carA.get("marka"))


# for key in carA:           # sadece key
#     print(key,carA[key])

# for value in carA.values():  # sadece value
#     print(value)

# for key,value in carA.items():  # sadece key value
#     print(key,value)

# carA.setdefault("test","test")


# print(carA)


# result="models" in carA
# print(result)

# result=len(carA)
# print(result)


# carA.pop("test")
# print(carA)

# carA.popitem()
# print(carA)

# del carA["marka"]




# tempObj1=carA
# tempObj2=carA.copy()

# tempObj1["value1"]="value"
# tempObj2["value2"]="value"



# tempObj2.update({
#         "model":"Bmw"
# })
# print(result)

# print(carA)
# print(tempObj1)
# print(tempObj2)







#UYGULAMA





players=[
    {"id":1,"name":"messi","date":"22.22.2222","nationality":"Türkiye","team":"Barça","history":"barça, argentina,portugal"},
    {"id":2,"name":"ronaldo","date":"11.11.1111","nationality":"potgual","team":"real","history":"real, argentina,portugal"}
    ]


query= int(input("please enter search query: "))

for data in players:
    if data.get("id")==query:
        print(data)

print(players)



