def masukan(dec: int):
    if dec == 0 or dec == 1:
        return dec

    if dec%2 == 0:
        return dec // 2

    return (dec + 1) // 2

def binariDesimal(binari: str):
    pangkat = 0
    nomor = 0
    for i in range(len(binari)-1, -1, -1):
        if binari[i] != '0' and binari[i] != '1':
            print('Input error')
            exit()
        
        nomor += int(binari[i]) * pow(2, pangkat)
        pangkat += 1

    return nomor

def desimalBinari(nomor: int):
    binari = ''
    while(nomor > 0):
        digit = nomor % 2
        binari += str(digit)
        nomor = nomor // 2
    while(len(binari) != 12):
        binari += '0'
    binari = binari[::-1]
    return binari

def printHasil(outputs: list):
    for output in outputs:
        print(desimalBinari(output))

def logika(inputList: list):
    daftarOutput = []
    for nomor in inputList:
        total = 0
        max = binariDesimal(nomor)
        for i in range(0, max+1, 1):
            totalLoop = 0
            fb = i
            while True:
                if fb == 0 or fb == 1:
                    break
                fb = masukan(fb)
                totalLoop += 1
            total += totalLoop
        daftarOutput.append(total)
    return daftarOutput

def main():
    inputs = []
    while True:
        userInput = input()
        if userInput == '-1':
            break
        inputs.append(userInput)

    outputs = logika(inputs)
    printHasil(outputs)


if __name__ == '__main__':
    main()