PESAN_ERROR = 'ERROR'

def logika(inputs = []):
    genap = []
    ganjil = []
    returnList = []
    for input in inputs:
        if (input%2 == 0):
            genap.append(input)
            continue
        ganjil.append(input)

    genap.sort(reverse=True)
    ganjil.sort(reverse=False)

    returnList.extend(ganjil)
    returnList.extend(genap)

    return returnList

def printDaftar(myList):
    for element in myList:
        print(element, end='')
        print(' ', end='')

    print()

def utama():
    try:
        ukuranList = int(input())

    except:
        print('Input is not an int')

    if (ukuranList < 1 or ukuranList > 10):
        print(PESAN_ERROR)
        return

    inputList = []

    try:
        for i in range(0, ukuranList, 1):
            inputNumber = int(input())

            if (inputNumber < 1 or inputNumber > 1000):
                print(PESAN_ERROR)
                return

            inputList.append(inputNumber)

    except:
        print('Input is not an int')

    output = logika(inputList)

    printDaftar(output)

if __name__ == '__main__':
    utama()