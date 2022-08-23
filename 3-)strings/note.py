str1="hello world"
num=4
print(len(str1))

print(f"{str1}")
print("{val1}, {val2}".format(val1=str1,val2=num))

#aşağıda hata gelir çünkü yukarıdaki kullanımlardan farklı bunu kullanma ya da int değerleri string değerlere çevir
print(str1+""+num)