ukuran = 0

def pound(row):
    global ukuran
    for i in range(0, ukuran-row, 1):
        print("#", end='')

def stars(row):
    for i in range(0, row, 1):
        print("*", end='')

def space():
    print(" ", end='')

def num(row):
    for i in range(1, row+1, 1):
        print(i, end='')

def numInverse(row):
    global ukuran
    for i in range(ukuran, ukuran-row, -1):
        print(i, end='')


def logic():
    global ukuran
    for i in range(1, ukuran+1, 1):
        pound(i)
        stars(i)
        space()
        num(i)
        print()
    
    for j in range(ukuran, 0, -1):
        pound(j)
        numInverse(j)
        space()
        stars(j)
        print()

def main():
    try:
        n = int(input())
    except:
        print("Input is not an int.")

    if (n < 1 or n > 9):
        print("ERROR")
        return
    global ukuran
    ukuran = n

    logic()

if __name__ == '__main__':
    main()