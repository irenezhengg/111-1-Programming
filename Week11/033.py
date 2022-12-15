MSG = 'ERROR'

def getPembilangPenyebut(operator: str):
    try:
        tmp = operator.split('/')
        pembilangOperator = int(tmp[0])
        penyebutOperator = int(tmp[1])

        if penyebutOperator == 0:
            return 0, 0

    except:
        print(MSG)

    return pembilangOperator, penyebutOperator

def tambah(operator1: str, operator2: str):
    operator1Pembilang, operator1Penyebut = getPembilangPenyebut(operator1)
    operator2Pembilang, operator2Penyebut = getPembilangPenyebut(operator2)

    if operator1Pembilang == 0 or operator1Penyebut == 0 or operator2Pembilang == 0 or operator2Penyebut == 0:
        return MSG

    if operator1Penyebut == operator2Penyebut:
        resultNumerator = operator1Pembilang + operator2Pembilang
        returnValue = str(resultNumerator) + '/' + str(operator1Penyebut)
        return returnValue

    operator1Pembilang *= operator2Penyebut
    operator2Pembilang *= operator1Penyebut
    returnValue = str(operator1Pembilang + operator2Pembilang) + '/' + str(operator1Penyebut * operator2Penyebut)
    return returnValue

def kurang(operator1: str, operator2: str):
    operator1Pembilang, operator1Penyebut = getPembilangPenyebut(operator1)
    operator2Pembilang, operator2Penyebut = getPembilangPenyebut(operator2)

    if operator1Pembilang == 0 or operator1Penyebut == 0 or operator2Pembilang == 0 or operator2Penyebut == 0:
        return MSG

    if operator1Penyebut == operator2Penyebut:
        resultNumerator = operator1Pembilang - operator2Pembilang
        returnValue = str(resultNumerator) + '/' + str(operator1Penyebut)
        return returnValue

    operator1Pembilang *= operator2Penyebut
    operator2Pembilang *= operator1Penyebut
    returnValue = str(operator1Pembilang - operator2Pembilang) + '/' + str(operator1Penyebut * operator2Penyebut)
    return returnValue

def kali(operator1: str, operator2: str):
    operator1Pembilang, operator1Penyebut = getPembilangPenyebut(operator1)
    operator2Pembilang, operator2Penyebut = getPembilangPenyebut(operator2)
    
    if operator1Pembilang == 0 or operator1Penyebut == 0 or operator2Pembilang == 0 or operator2Penyebut == 0:
        return MSG

    returnValue = str(operator1Pembilang * operator2Pembilang) + '/' + str(operator1Penyebut * operator2Penyebut)

    return returnValue

def bagi(operator1: str, operator2: str):
    operator1Pembilang, operator1Penyebut = getPembilangPenyebut(operator1)
    operator2Pembilang, operator2Penyebut = getPembilangPenyebut(operator2)

    if operator1Pembilang == 0 or operator1Penyebut == 0 or operator2Pembilang == 0 or operator2Penyebut == 0:
        return MSG

    returnValue = str(operator1Pembilang * operator2Penyebut) + '/' + str(operator1Penyebut * operator2Pembilang)

    return returnValue

OPERASI = {
    '+' : tambah,
    '-' : kurang,
    '*' : kali,
    '/' : bagi
}

def ntahApa(n, m):
    if n > 0:
        d =  min (n, m)
        while   n % d != 0 or m % d != 0:
            d =  d - 1

    if n < 0:
        d =  min (n, m)
        while   n % d != 0 or m % d != 0:
            d =  d + 1

    return  d

def mengurangi (num, den):
   if num == 0:
      return  (0, 1)
   G =  ntahApa(num, den)
   return  (num // G, den // G)


def sederPecahan(pecahan: str):
    if pecahan == MSG:
        return MSG

    remaining = 0
    returnValue = ''
    negatif = False

    pembilang, penyebut = getPembilangPenyebut(pecahan)

    if pembilang < 0:
        pembilang *= -1
        negatif = not(negatif)

    if penyebut < 0:
        penyebut *= -1
        negatif = not(negatif)

    pembilang, penyebut = mengurangi(pembilang, penyebut)

    if pembilang == 0:
        return str(0)

    remaining = pembilang // penyebut
    pembilang %= penyebut

    if remaining != 0:
        if negatif:
            returnValue += '-'
        returnValue += str(remaining)
        if pembilang != 0:
            returnValue += '('

    if pembilang != 0:
        if remaining == 0 and negatif:
            returnValue += '-'
        returnValue += str(pembilang) + '/' + str(penyebut)

    if remaining != 0 and pembilang != 0:
        returnValue += ')'

    return returnValue

def fraksiSemua(pecahan: str):
    try:
        tmp = pecahan.split('(')
        if len(tmp) == 1:
            return pecahan

        utuh = int(tmp[0])
        tmp = tmp[1].split('/')
        pembilang = int(tmp[0])
        tmp = tmp[1].split(')')
        penyebut = int(tmp[0])

    except:
        print('Error fractioning before operation.')

    negatif = False

    if utuh < 0:
        utuh *= -1
        negatif = not(negatif)

    pembilang += (utuh * penyebut)
    
    if negatif:
        pembilang *= -1

    return str(pembilang) + '/' + str(penyebut)
    


def logika(operator: list, operan: list):
    results = []
    if len(operator) != len(operan):
        return

    for i in range(0, len(operator), 1):
        if not(operan[i] in OPERASI.keys()):
            return
        
        if len(operator[i]) != 2:
            return

        func = OPERASI[operan[i]]
        result = func(fraksiSemua(operator[i][0]), fraksiSemua(operator[i][1]))
        result = sederPecahan(result)
        results.append(result)
    
    return results


def main():
    operator = []
    operan = []

    while True:
        operatorInput = []
        operatorInput.append(input())
        operatorInput.append(input())
        operator.append(operatorInput)
        operand = input()
        operan.append(operand)
        cont = input()

        if cont == 'y':
            continue
        break

    results = logika(operator, operan)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()