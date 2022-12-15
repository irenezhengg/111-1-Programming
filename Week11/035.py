def barangBilanganBulat(barang2: list):
    returnList = []
    try:
        for barang in barang2:
            returnList.append(int(barang[0]))

    except:
        print('Input Error')
        exit()

    return returnList

def barangKarakter(barang2: list):
    returnList = []
    for barang in barang2:
        returnList.append(barang[1])

    return returnList

def checkDuplikat(barang2: list):
    if len([barang for barang in barang2 if barang2.count(barang) > 1]) > 0:
        return True
    return False

def melebihibatasbeban(barang2: list, muatan: int):
    daftarBarang = barangBilanganBulat(barang2)
    for barang in daftarBarang:
        if barang > muatan:
            return True
    return False

def temukanSetPengiriman(daftarBarang: list, muatan: int):
    daftarAngka = barangBilanganBulat(daftarBarang)
    daftarHuruf = barangKarakter(daftarBarang)
    returnList = []
    IndeksDaftarPengecualian = []
    pelacak = 0
    for i in range(0, len(daftarAngka), 1):
        if i in IndeksDaftarPengecualian:
            continue

        total = daftarAngka[i]
        tmpList = [daftarHuruf[i]]
        IndeksDaftarPengecualian.append(i)

        for j in range(i, len(daftarAngka), 1):
            if total == muatan:
                total = 0
                returnList.append(tmpList)
                pelacak += 1
                break

            if j in IndeksDaftarPengecualian:
                continue

            if (total + daftarAngka[j]) <= muatan:
                total += daftarAngka[j]
                tmpList.append(daftarHuruf[j])
                IndeksDaftarPengecualian.append(j)
                pelacak += 1
        
        if total == muatan:
            total = 0
            returnList.append(tmpList)
            pelacak += 1

    if(pelacak != len(daftarBarang)):
        print('Cannot be delivered')
        exit()

    return returnList

def sortirPengiriman(deliveryList: list):
    copy_deliveryList = deliveryList
    length = 1
    lengthList = []
    result = []
    total = 0
    while copy_deliveryList:
        iterator = 0
        rangeLength = len(copy_deliveryList)
        while iterator != rangeLength:
            if length == 1 and isinstance(copy_deliveryList[iterator], str):
                print(combination)
                combination = copy_deliveryList.pop(iterator)
                lengthList.append(combination)
                total += 1
                iterator -= 1
                rangeLength -= 1

            elif len(copy_deliveryList[iterator]) == length:
                combination = copy_deliveryList.pop(iterator)
                combination.sort()
                lengthList.append(combination)
                total += 1
                iterator -= 1
                rangeLength -= 1

            iterator += 1
            
        lengthList.sort()
        result.append(lengthList)
        lengthList = []
        length += 1
    return result, total

def logika(daftarBarang: list, muatan: int):
    return sortirPengiriman(temukanSetPengiriman(daftarBarang, muatan))

def printDeliveryList(deliveryList: list, trips: int):
    print(trips)
    for sublist in deliveryList:
        if len(sublist) == 0:
            continue
        for subsublist in sublist:
            if len(subsublist) == 0:
                continue
            
            for i in range(0, len(subsublist), 1):
                print(subsublist[i], end='')
                if i != (len(subsublist) - 1):
                    print(' ', end='')
            print()

def main():
    barang2 = input().split(' ')
    try:
        bebanMuatan = int(input())
    
    except:
        print('Input Error')

    if (bebanMuatan < 1 or bebanMuatan > 10):
        print('Input Error')
        return

    if(checkDuplikat(barang2)):
        print('Duplicated ID')
        return
    
    if (melebihibatasbeban(barang2, bebanMuatan)):
        print('Load limit exceeded')
        return

    deliveryList, totalTrips = logika(barang2, bebanMuatan)
    printDeliveryList(deliveryList, totalTrips)

if __name__ == '__main__':
    main()

