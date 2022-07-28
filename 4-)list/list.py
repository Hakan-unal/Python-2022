# message="hello world"

# array=message.split()
# numbers=[1,3,5,8,9,11,12]
# names=["name1","name2","name3","name4","name5","name6"]
# liste=["name1","surname1",12]
# complexArray=[[1,2,"name"],["name","surname",23]]

# # print(array)
# # print(array[0])
# # print(array[1])
# # print(array[0][0])
# # print(array[1][0])
# # print([[1,2,"name"],["name","surname",23]])
# # print(complexArray[0])
# # print(complexArray[0][2])
# # print(complexArray[0][2][1])


# print(names[:2])
# print(names[2:4])
# print(names[3:])
# print(names[-1])
# print(names[-4:-1])
# print(len(names))


# if"name1" in names:
#     print("True")
# else :
#     print("False")

# if"name212" in names:
#     print("True")
# else :
#     print("False")


# for data in names:
#     print(data)


# del names[3]

# print(names)




#Uygulama





list=["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
listLen=len(list)

print(listLen)
print(list[0],list[listLen-1])

list[0]="Samsung S9"

if "Samsung S6" in list:
    print("Elemanı")
else:
    print("Elemanı değil")

print(list)
print(list[-3])
print(list[:2])

list[listLen-1]="Samsung S10"
list[listLen-2]="Samsung S9"

print(list)
list.append("Samsung X")
list.append("Samsung XR")

print(list)

listLen=len(list)

del list[listLen-1]
del list[-1]

print(list)


print(list[::-1])


userA=["Yiğit","Bilgi",2010,(70,60,70)]
userB=["Sena","Turan",1999,(80,80,70)]
userC=["Ahmet","Turan",1998,(80,70,90)]

print(userA[3][2])

for data in list:
    print(data)
