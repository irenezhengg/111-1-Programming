def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    discount1 = [1.0, 0.95, 0.9, 0.8]
    discount2 = [1.0, 0.9 , 0.85, 0.75]
    discount3 = [1.0, 0.85, 0.8, 0.8]
    priceA = price(n1,discount1)
    priceB = price(n2,discount2)
    priceC = price(n3,discount3)
    total = (n1*30*priceA) + (n2*70*priceB) + (n3*40*priceC)
    result(total,n1,n2,n3)
    print('%d'%result(total,n1,n2,n3))

def price(x,y):
    price = 0
    if (x >= 21):
        price = y[3]
    elif (x >= 16):
        price = y[2]
    elif (x >= 11):
        price = y[1]
    elif (x >= 1):
        price = y[0]
    return price

def result(total,n1,n2,n3):
    amount = n1 + n2 + n3
    result = 0
    if (amount >= 30):
        result += total * 0.87
    else:
        result += total * 1
    return result
main()