ERROR = "ERROR"
LETTER_CHOICE = {
    0 : "C",
    1 : "A",
    2 : "B"
}

def printAlpha(ukuran):
    if (ukuran < 2 or ukuran > 29):
        print(ERROR)
        return

    panjang = ukuran * 2 - 1
    lapisan = ukuran - 1

    for i in range(0, ukuran, 1):
        print((lapisan - i ) * "#", end='')
        print("*", end = '')

        letterCode = i%3

        for j in range(0, i, 1):
            print(LETTER_CHOICE[letterCode], end='')
            print("*", end='')
        
        print((lapisan - i ) * "#", end='')
        print()


def Stars(ukuran):
    if (ukuran < 2 or ukuran > 9):
        print(ERROR)
        return

    panjang = ukuran * 2 + 2

    for i in range(1, ukuran+1):
        starsNumber = panjang - 2 * i
        for j in range(1, i+1, 1):
            print(j, end='')
        print(starsNumber * "*", end = '')
        for j in range(i, 0, -1):
            print(j, end='')
        print()
        
PILIHAN_BENTUK = {
    1 : printAlpha,
    2 : Stars
}

def logika(type, ukuran):
    function = PILIHAN_BENTUK[type]
    function(ukuran)


def main():
    try:
        x = int(input())
        
        if not(x in PILIHAN_BENTUK.keys()):
            print(ERROR)
            return

        y = int(input())
        
    
    except:
        print("Inputs are not ints")

    logika(x, y)

if __name__ == '__main__':
    main()