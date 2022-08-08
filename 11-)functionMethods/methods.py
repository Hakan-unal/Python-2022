#lambda


# def test1(a,b):
#     return a*b

# def test4(b):
#     return lambda a:a*b
# result= (lambda a,b:a*b)(3,5)

# test2=lambda a,b:a*b

# test3=test4(3)


# print(test1(2,4))
# print(result)
# print(test1(4,6))
# print(test3(4))


#map


# numbers=[1,2,5,7,9]
# exponentials=[]

# for number in numbers:
#     exponentials.append(number**2)


# def kareAl(number):
#     return number**2

# result=list(map(kareAl,numbers))
# result1=list(map(lambda number:number**2,numbers))
# result2=list(map(str,numbers))

# print(exponentials)
# print(result)
# print(result1)
# print(result2)



#filter

# numbers=[1,2,3,4,4,5,56,2342,32,12,22,33,11]

# result=list(filter(lambda number:number%2==0,numbers))
# result1=list(filter(lambda number:number%2==1,numbers))
# result2=list(filter(lambda number:number%2==0,filter(lambda number:number%4==0,numbers)))
# result3=list(map(lambda number:number%2==1,numbers))

# print(result)
# print(result1)
# print(result2)
# print(result3)




# any, all



# numbers=[1,2,3,4,5,None]
# strings=["1sad","qweasd","ass","asds","asdad"]
# booleans=[True,True,False,None]
# dicts=[{},{}]

# result=all(numbers)
# result1=all(strings)
# result2=all(booleans)
# result3=all(dicts)
# result4=any(numbers)
# result5=any(strings)
# result6=any(booleans)
# result7=any(dicts)

# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)



#sorted


# numbers=[1,3,5,46,78,9,90,77,87]
# users=[
#     {"name":"name3","tweets":["tweet 1"],"count":1000},
#     {"name":"name1","tweets":["tweet 1","tweet 2"],"test":"ets","count":2000},
#     {"name":"name2","tweets":[],"test":"test","test1":"test2","count":3000},
# ]

# result=sorted(numbers,reverse=False)
# result1=sorted((1,4,3,2,4,34,123,22,32),reverse=False)
# result2=sorted(users,key=len,reverse=True)
# result3=sorted(users,key=lambda user:user.get("name"))
# result4=sorted(users,key=lambda user:user.get("count"),reverse=True)

# numbers.sort()

# print(numbers)
# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)





#min,max

# numbers=[1,3,34,45,67,789,90,456,234,33,33,13,15]
# chars=["as","bdas","asd","bss","ccc"]
# products=[
#     {"name":"name1","price":1000},
#     {"name":"name2","price":2000},
#     {"name":"name3","price":3000},

# ]
# result=min(numbers)
# result1=max(numbers)
# result2=min(chars)
# result3=max(chars)
# result4=max(products,key=lambda product:product.get("price")).get("name")
# result5=min(products,key=lambda product:product.get("price")).get("name")

# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)



#sum,round

numbers=[1,23,34,23,54,43,1,2,3,4]
products=[
    {"name":"name1","price":1000},
    {"name":"name2","price":2000},
    {"name":"name3","price":3000},
]

result=sum(numbers)
result1=sum(numbers,25)
result2=sum(map(lambda product:product.get("price"),products))


print(result)
print(result1)
print(result2)
print(round(10.2))
print(round(10.5))
print(round(10.7))
print(round(10.73123123123,3))
print(round(10.73163123123,3))
