# numbers=[12,32,122,1,2,3,4,5,5,6,6,6,6,6]
# strigns=["name1","name2","name3","name4"]
# mix=[1,2,3,"name1","name2"],


# print(min(numbers))
# print(max(numbers))
# print(min(strigns))
# print(max(strigns))

# numbers.append(12)
# numbers.insert(2,12)

# numbers.pop()

# numbers.remove(5)

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)

# print(numbers.count(64))

# numbers.clear()
# print(numbers)




#uygulama




names=["name1","name2","name3","name4","name5","name6",]
ages=[2004,2005,1998,1999,2000,2001,2002]



names.append("Cenk")
print(names)

names.insert(0,"Sena")
print(names)

names.remove("name3")
print(names)

#print(names.index("name3"))
print(names.count("name3"))
print( "names" in names)

names.reverse()
print(names)

names.sort()
print(names)


ages.sort()

print(ages)




message="IPHONE X, IPHONE XR"

tempArr=message.split(",")

print(tempArr)

print(min(ages))
print(max(ages))

print(ages.count(1998))

ages.clear()
print(ages)


companies=[]

input1=input("1. firma: ")
companies.append(input1)
input2=input("2. firma: ")
companies.append(input2)
input3=input("3. firma: ")
companies.append(input3)

print(companies)
