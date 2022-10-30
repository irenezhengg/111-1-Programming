def entahApa(baris, ukuran):
    marginSize = ukuran - 1 - (2 * baris)
    print(marginSize * " ", end = '')
    print(2 * baris * "*", end = '')
    print("*", end='')
    print(2 * baris * "*", end = '')
    print(2 * marginSize * " ", end = '')
    print(2 * (baris-1) * "+", end='')
    if (baris > 0):
        print("+", end="")

def logika(ukuran):
    for i in range(0, ukuran//2, 1):
        entahApa(i, ukuran)
        print()
    for j in range(ukuran//2, -1, -1):
        entahApa(j, ukuran)
        print()


def main():
    ukuran = input()

    try:
        ukuran = int(ukuran)
    except:
        print("Inputs are not ints!")

    if (ukuran%2 == 0):
        print("ERROR")
        return

    logika(ukuran)

if __name__ == '__main__':
    main()