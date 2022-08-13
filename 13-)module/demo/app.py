from methods import *



while True:
    print("1-) Add Product")
    print("2-) Get Product")
    print("3-) Get Products")
    print("4-) Remove Product")

    choice= input("Choice operations: 1/2/3/4: ")
    match (choice):
        case "1":
            name=input("Please enter product name:")
            price=input("Please enter product price:")
            addProduct(name,price)
        case "2":
            id=int(input("Please enter product id:"))
            print(getProduct(id))
        case "3":
            print(getProducts())
        case "4":
            id=int(input("Please enter product id:"))
            removeProduct(id)
        case default:print("Invalid Choice")






