def masukan(desimal: int):
    if desimal == 0 or desimal == 1:
        return desimal

    if desimal%2 == 0:
        return desimal // 2

    return (desimal + 1) // 2

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

def logika(inputList: list):
    daftarKeluaran = []
    for nomor in inputList:
        hasil = []
        fb = binariDesimal(nomor)
        while True:
            fb = masukan(fb)
            hasil.append(fb)
            if fb == 0 or fb == 1:
                break
        daftarKeluaran.append(hasil)
    return daftarKeluaran

def desimalBinari(nomor: int):
    binari = ''
    while(nomor > 0):
        angka = nomor % 2
        binari += str(angka)
        nomor = nomor // 2
    while(len(binari) != 4):
        binari += '0'
    binari = binari[::-1]
    return binari

def printHasil(outputs: list):
    for hasil in outputs:
        if (len(hasil) == 1):
            print('0000')
            print('No Feedback')
            continue

        print(desimalBinari(len(hasil)))
        for i in range(0, len(hasil), 1):
            print(hasil[i], end='')
            if (i != (len(hasil) - 1)):
                print(' ', end='')
        print()


def main():
    inputs = []
    while True:
        inputPengguna = input()
        if inputPengguna == '-1':
            break
        inputs.append(inputPengguna)

    outputs = logika(inputs)
    printHasil(outputs)


if __name__ == '__main__':
    main()