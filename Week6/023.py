def logika(listTahun):
    for tahun in listTahun:
        print(tahun, end='')
        print(" is ", end='')
        if ((tahun%400 == 0 and tahun%100 == 0) or (tahun%100 != 0 and tahun%4 == 0)):
            print("leap", end='')
        else:
            print("normal", end='')
        print(" tahun.")


def main():
    try:
        a = int(input())
    except:
        print("Input is not an int.")

    if (a < 1 or a > 10):
        print("Error")
        return

    listTahun=[]

    try:
        for i in range(0, a, 1):
            tahun = int(input())
            if (tahun < 1 or tahun > 10000):
                print("Error")
                return
            listTahun.append(tahun)
    except:
        print("Input is not an int.")
    
    logika(listTahun)

if __name__ == '__main__':
    main()