def logika(ukuran):
    for i in range(1, ukuran, 2):
        print(i*"*", end='')
        print(2 * (ukuran-i) * "_", end='')
        print(i*"*", end='')
        print()
    
    for j in range(ukuran, 0, -2):
        print(j*"*", end='')
        print(2 * (ukuran-j) * "_", end='')
        print(j*"*", end='')
        print()


def main():
    try:
        n = int(input())
    except:
        print("Input is not an int.")

    if (n < 4 or n > 30 or n%2 == 0):
        print("Error")
        return

    logika(n)

if __name__ == '__main__':
    main()