ERROR = "ERROR"

def sum(input):
    if (input == 1):
        return 1
        
    return ((input**input) + sum(input-1))

def Seq(result):
    ukuran = str(result)
    returnStr = ""
    for i in range(len(ukuran)-1, -1, -1):
        returnStr += ukuran[i]
        
        if (i != 0):
            returnStr += ","

    return returnStr

def logika(input):
    result = sum(input)
    ukuran = Seq(result)
    print(result)
    print(ukuran)

def utama():
    try:
        n = int(input())
        
        if (n < 0 or n > 10):
            print(ERROR)
            return
        
        for i in range(0, n, 1):
            k = int(input())

            if (k < 1 or k > 15):
                print(ERROR)
                continue

            logika(k)
    
    except:
        print("Inputus are not ints")

if __name__ == '__main__':
    utama()