users=[
    {
        "name":"name1",
        "hesapNo":"1111",
        "money":1000,
        "ekMoney":500
    },
     {
        "name":"name2",
        "hesapNo":"2222",
        "money":2000,
        "ekMoney":1000
    }
]



def widthraw(hesapNo,value):
    user=checkHesap(hesapNo)
    if(user!=False):
        if(user.get("money")>=value):
            user["money"]-=value
            print("ana hesap çekebilirsiniz")
        else:
            total=user.get("money")+user.get("ekMoney")
            if(total>=value):
                userChoice=input("Ek hesap kullanılsın mı ? (e/h)")
                if(userChoice=="e"):
                    user["ekMoney"]-=value-user["money"]
                    user["money"]=0
                    print("ana hesap + ek hesap çekebilirsiniz")
                else:
                    print("işlem iptal")
            else:
                print("bakiye yetersiz")
    else:print("Geçersiz hesap no")
            
def checkHesap(hesapNo):
    for user in users:
        if(user.get("hesapNo")==hesapNo):
            return user
    return False




for i in range(3):
    input1=input("please enter hesapNo: ")
    input2=int(input("please enter value: "))
    widthraw(input1,input2)
