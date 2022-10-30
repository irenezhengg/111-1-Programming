from itertools import cycle


def algoritma(input):
    global siklus
    siklus += 1

    if (input <= 1):
        return

    if (input % 2 == 1):
        algoritma((3 * input + 1))
        return
    
    algoritma((input//2))

def logika(minimum, input):
    global siklus
    siklus = 0
    maximum = 0
    for i in range(minimum, input+1, 1):
        algoritma(i)

        if siklus > maximum:
            maximum = siklus

        siklus = 0

    return maximum

def utama():
    try:
        x = int(input())
        y = int(input())

        if ((x < 1 or x > 10000) or (y < x or y > 10000)):
            print("ERROR")
            return
        
    except:
        print("Inputs are not all ints")

    siklus = logika(x, y)
    print(siklus)

if __name__ == '__main__':
    utama()