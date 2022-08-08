# try:
#     number=int(input("please enter number: "))
# except:
#     print("error")


# x = int(input('x '))
# y = int(input('y '))

# print(x / y)

# SyntaxError => yazım yanlışı

# hlkhlk;;
# def yazdir((:
#     pass
# print('merhab'a)

# NameError => tanımlanmamış bir değişken kullanımı
# print(ad)

# TypeError => hatalı parametre kullanımı
# len(5)
# 4 + 'a'

# IndexError => yanlış indeks numarası
# liste = ['merhaba']
# liste[1]

# ValueError => hatalı tip kullanımı
# int('10a')

# KeyError => key hatası
# d = {}
# d['ad']

# AttributeError => olmayan bir özelliğe ulaşmak istediğimizde
# "merhaba".upper()
# "merhaba".Upper()




# while True:
#     try:
#         x=int(input("x:"))
#         y=int(input("y:"))
#         print(x/y)
#     except ZeroDivisionError as err:
#         print("Y can not 0")
#         print(err)
#     except ValueError:
#         print("x and y only numeric")
#     except Exception as err:
#         print("unexpected error")
#         print(err)
#     else:
#         break
#     finally:
#         print("Test")



#uygulama


# arr=["1","2","5a","10b","abc","10","50"]


# for x in arr:
#     try:
#         result=int(x)
#         print(result)
#     except ValueError:
#         continue


# while True:
#     number=input("(q:quit)input:")
#     if(number=="q"):
#         quit()
    
#     try:
#         result=float(number)
#         print(result)
#         break
#     except ValueError:
#         print("geçersiz sayı")
#         continue


# try:
#     obj={"name":"samsung s10"}
#     obj.get("surname") 
#     obj["surname"]
# except KeyError:
#     print("key error")



