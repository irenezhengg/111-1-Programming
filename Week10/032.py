def logika(equation):
    tambah = 0
    kurang = 0
    kali = 0
    bagi = 0
    kurung = []
    isBreak = False
    for karakter in equation:
        if karakter == '{' or karakter == '[' or karakter == '(' or karakter == '<' or karakter == '⊂' or karakter == '【':
            kurung.append(karakter)
            continue
        if karakter == '}':
            if kurung[len(kurung)-1] != '{':
                isBreak = True
                break
            del kurung[len(kurung)-1]
            continue
        if karakter == ']':
            if kurung[len(kurung)-1] != '[':
                isBreak = True
                break
            del kurung[len(kurung)-1]
            continue
        if karakter == ')':
            if kurung[len(kurung)-1] != '(':
                isBreak = True
                break
            del kurung[len(kurung)-1]
            continue
        if karakter == '>':
            if kurung[len(kurung)-1] != '<':
                isBreak = True
                break
            del kurung[len(kurung)-1]
            continue
        if karakter == '⊃':
            if kurung[len(kurung)-1] != '⊂':
                isBreak = True
                break
            del kurung[len(kurung)-1]
            continue
        if karakter == '】':
            if kurung[len(kurung)-1] != '【':
                isBreak = True
                break
            del kurung[len(kurung)-1]
            continue
        if karakter == '+':
            tambah += 1
            continue
        if karakter == '-':
            kurang += 1
            continue
        if karakter == '*':
            kali += 1
            continue
        if karakter == '/':
            bagi += 1
            continue

    dekat = False
    if len(kurung) == 0 and not(isBreak):
        dekat = True

    return dekat, tambah, kurang, kali, bagi

def utama():
    try:
        masuk = int(input())
    
    except:
        print('First input is not a number')

    for i in range (0, masuk, 1):
        eq = input()
        parent, tambah, kurang, kali, bagi = logika(eq)
        if parent:
            print('Pass')
            print('%d %d %d %d' %(tambah, kurang, kali, bagi))
            continue
        print('Fail')


if __name__ == '__main__':
    utama()