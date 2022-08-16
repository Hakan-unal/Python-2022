

# class Person:
#     def __init__(self,name,surname):
#         self.uniq="Name"
#         self.name=name
#         self.surname=surname
#     def f1(self):
#         return self.name



# person1=Person("Test","Test1")
# person2=Person("Test","Test2")



# print(person1.uniq)
# print(person1.name)
# print(person1.surname)

# print(person2.f1())



# #uygulama

# class Comment:
#     def __init__(self,username,text,likes=0,dislikes=0):
#         self.username=username
#         self.text=text
#         self.likes=likes
#         self.dislikes=dislikes
    

# obj= Comment("username1","text1",)
# obj1= Comment("username2","text2")
# obj2= Comment("username3","text3","likes3","dislikes3")
# obj3= Comment("username4","text4","likes4","dislikes4")
# obj4= Comment("username5","text5","likes5","dislikes5")

# objects=[obj,obj1,obj2,obj3,obj4]

# for object in objects:
#     print(object.username)
#     print(object.dislikes)



class BankAccount:
    activeAccounts=0
    arr=[1,2,3,4]

    @classmethod
    def display_activeAccounts(cls):
        return cls.activeAccounts
    def append_arr(cls,val):
        return cls.arr.append(val)
    def __init__(self,owner,balance=0.0):
        self.owner=owner
        self.balance=balance
        BankAccount.activeAccounts+=1
    
    def getBalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
        return self.getBalance()
    def withdraw(self,amount):
        self.balance-=amount
        return self.getBalance()
    def logout(self):
        BankAccount.activeAccounts-=1

print(BankAccount.activeAccounts)

user=BankAccount("user")
user1=BankAccount("user1")

print(user.deposit(1000))
print(user.withdraw(100))

print(user.owner)
print(user.arr)
print(user.activeAccounts)
user.append_arr(5)
user.append_arr(5)

print(user.arr)
print(user.display_activeAccounts())


print(BankAccount.activeAccounts)
user.logout()
print(BankAccount.activeAccounts)
