from db import *

def addProduct(name,price):
    productLen=len(products)
    product={
        "name":name,
        "price":price,
        "id":(products[productLen-1].get("id")+1)
    }
    products.append(product)

def getProduct(id):
    result=list(filter(lambda data:data.get("id")==id,products))
    return  result

def getProducts():
    global products
    return  products

def removeProduct(id):
    global products
    result=list(filter(lambda data:data.get("id")!=id,products))
    products=result