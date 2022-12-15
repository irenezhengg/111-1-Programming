def dapatkanSkorHuruf(string):
    nilai = 0
    nomor2 = 0
    nomorSebelumnya = False
    for huruf in string:
        if huruf.islower():
                nomorSebelumnya = False
                nilai += 1
        if huruf.isupper():
            nomorSebelumnya = False
            nilai += 3
        if huruf.isnumeric():
            if nomorSebelumnya:
                nomor2 = 0
            else:
                nomor2 += 1
                nomorSebelumnya = True
            nilai += 2
        if huruf == '{' or huruf == '~' or huruf == '!' or huruf == '@' or huruf == '#' or huruf == '$' or huruf == '%' or huruf == '^' or huruf == '&' or huruf == '*' or huruf == '<' or huruf == '>' or huruf == '_' or huruf == '+' or huruf == '=' or huruf == '}':
            nomorSebelumnya = False
            nilai +=5
        
        if nomor2 == 5:
            nomor2 = 0
            nilai += 15

    return nilai

def terbaikDanTerburuk(daftar_kata_sandi):
    atas = daftar_kata_sandi[0]
    bawah = daftar_kata_sandi[0]

    for kataSandi in daftar_kata_sandi:
        if kataSandi[0] > atas[0]:
            atas = kataSandi
        
        if kataSandi[0] < bawah[0]:
            bawah = kataSandi
    
    return atas, bawah

def logika(kataSandi):
    nilai_kata_sandi = []
    for kata_sandi in kataSandi:
        nilai = dapatkanSkorHuruf(kata_sandi)
        nilai_kata_sandi.append([nilai, kata_sandi])

    return terbaikDanTerburuk(nilai_kata_sandi)

def utama():
    kataKataSandi = []
    for i in range(0, 5, 1):
        kataSandi = input()
        if kataSandi == '-1':
            break
        
        if len(kataSandi) < 3 or len(kataSandi) > 15:
            continue
        kataKataSandi.append(kataSandi)

    atas, bawah = logika(kataKataSandi)

    print(atas[1] + ' %d' %atas[0])
    print(bawah[1] + ' %d' %bawah[0])

if __name__ == '__main__':
    utama()