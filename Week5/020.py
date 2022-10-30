def nomorPrima(num):
    if num < 2:
        return False
    for j in range(2, num):
        if (num % j) == 0:
            return False
    return True

def logika(maximum):
    sum = 0
    for i in range(2, maximum+1, 1):
        if nomorPrima(i):
            sum += i
    return sum

def main():
    maximum = input()

    try:
        maximum = int(maximum)
    except:
        print("Inputs are not ints!")

    if (maximum < 2 or maximum > 10000):
        return

    print(logika(maximum))

if __name__ == '__main__':
    main()