a,b,c=2,5,10

inputA=int(input("enter first number: "))
inputB=int(input("enter second number: "))

result1=inputA*inputB
result2=a+b+c
result3=result1-result2


print(result1)
print(result2)
print(result3)

print(c//b)
print(result2%3)



numbers=(1,5,7,10,3)


d,*e,f=numbers

print(f**3)
g=0

for data in e:
    g+=data

print(g)