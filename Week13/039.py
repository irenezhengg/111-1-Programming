def getStopSekarang(mulai: int, jalurSekarang: list) -> int:
    jalanSekarang = jalurSekarang[len(jalurSekarang)-1]

    if mulai == jalanSekarang[0]:
            return jalanSekarang[1]
    
    if mulai == jalanSekarang[1]:
        return jalanSekarang[0]

    previousRoad = jalurSekarang[len(jalurSekarang)-2]

    if previousRoad[0] == jalanSekarang[0]:
        return jalanSekarang[1]
    
    if previousRoad[0] == jalanSekarang[1]:
        return jalanSekarang[0]

    if previousRoad[1] == jalanSekarang[0]:
        return jalanSekarang[1]

    if previousRoad[1] == jalanSekarang[1]:
        return jalanSekarang[0]

    print('ERROR GETTING CURRENT STOP, EXIT')
    exit()
    

def cariRute(mulai: int, jalan2: list) -> list:
    jalur2 = []
    for jalan in jalan2:
        if mulai in jalan:
            jalur2.append([jalan])

    if len(jalur2) == 0:
        print('NO')
        exit()

    i = 0


    while True:
        if i >= len(jalur2):
            break

        jalurSekarang = jalur2[i].copy()
        stopSekarang = getStopSekarang(mulai, jalurSekarang)

        for jalan in jalan2:
            if stopSekarang in jalan and not(jalan in jalurSekarang):
                newPath = jalurSekarang.copy()
                newPath.append(jalan)
                jalur2.append(newPath)

        i += 1
    return jalur2
        

def cariJalurvalid(jalur2: list, berhenti: list) -> list:
    returnList = []
    for jalur in jalur2:
        checkFlags = 0

        for stop in berhenti:
            for jalan in jalur:
                if stop in jalan:
                    checkFlags += 1
                    break

        if checkFlags >= len(berhenti):
            returnList.append(jalur)

    if len(returnList) == 0:
        print('NO')
        exit()

    return returnList

def cariJalurPendek(jalur2: list) -> list:
    minima = 0

    for jalur in jalur2:
        if minima == 0:
            minima = len(jalur)
            returnPath = jalur
            continue

        if len(jalur) < minima: #note, do not know if smaller or smaller and equal
            minima = len(jalur)
            returnPath = jalur

    return returnPath

def jalanSederhana(jalur: list, mulai: int) -> list:

    returnPath = [mulai]

    if jalur[0][0] == mulai:
        koneksi = jalur[0][1]
    
    elif jalur[0][1] == mulai:
        koneksi = jalur[0][0]

    returnPath.append(koneksi)

    for i in range(1, len(jalur), 1):
        if jalur[i][0] == koneksi:
            koneksi = jalur[i][1]

        elif jalur[i][1] == koneksi:
            koneksi = jalur[i][0]

        returnPath.append(koneksi)

    return returnPath

def logika(mulai: int, berhenti: list, jalan2: list) -> list:

    jalur2 = cariRute(mulai, jalan2)
    jalur2 = cariJalurvalid(jalur2, berhenti)
    jalur = cariJalurPendek(jalur2)
    
    return jalanSederhana(jalur, mulai)



def printHasil(result: list):
    print((len(result) - 1))

    for i in range(0, len(result), 1):
        print(result[i], end='')

        if (i + 1) != len(result):
            print(' ', end='')

def main():
    input2 = input().split(' ')
    listJalan = []

    try:
        jalan2 = int(input2[0])
        awal = int(input2[1])
        berhenti = [int(input2[i]) for i in range(2, len(input2), 1)]

    except:
        print('ERROR Line 1: inputs are not int!')

    try:
        for i in range(0, jalan2, 1):
            input2 = input().split()
            roadBegin = int(input2[0])
            roadEnd = int(input2[1])
            listJalan.append([roadBegin, roadEnd])

    except:
        print('ERROR with the road in line ' + str(i+2))

    result = logika(awal, berhenti, listJalan)

    printHasil(result)

    

if __name__ == '__main__':
    main()