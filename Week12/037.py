from math import sqrt

def kotakBukan(number: int) -> bool:
    kotak = sqrt(number)
    return kotak.is_integer()

def cariPasanganBarang(barang2: int, jumlahPalet: int) -> list:
    daftarBarang = range(1, barang2+1, 1)
    daftarPalet = [[daftarBarang[0]]]
    for i in range(1, len(daftarBarang), 1):
        diMasukan = False
        barang = daftarBarang[i]
        for palet in daftarPalet:
            kotak = palet[0] + barang
            if (kotakBukan(kotak)):
                palet.append(barang)
                palet.sort(reverse=True)
                diMasukan = True
                break
        
        if diMasukan:
            continue
        
        daftarPalet.append([barang])

        if len(daftarPalet) > jumlahPalet:
            print('False')
            exit()
        
    return daftarPalet

def susunPalet(palet2: list) -> list:
    hasil = []
    insersi = 0
    ukuran = 1
    while True:
        for palet in palet2:
            if len(palet) == ukuran:
                palet.sort()
                hasil.append(palet)
                insersi += 1

        ukuran += 1

        if insersi == len(palet2):
            break

    return hasil


def logika(barang2: int, palet2: int) -> list :
    return susunPalet(cariPasanganBarang(barang2, palet2))

def printPalet(palet2: list) -> None:
    print('True')
    
    for palet in palet2:
        for barang in palet:
            print(barang, end=' ')
        print()

def main() -> None:
    try:
        batasBarang = int(input())
        paletKayu = int(input())

    except:
        print('Input is not int!')

    hasil = logika(batasBarang, paletKayu)
    printPalet(hasil)

if __name__ == '__main__':
    main()