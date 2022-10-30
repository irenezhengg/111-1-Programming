MATRIX_NORMAL = 0
MATRIX_PUTAR_KIRI = 1
MATRIX_PUTAR_KANAN = 2
MATRIX_PUTAR_ATAS_BAWAH = 3
MATRIX_PUTAR_KIRI_KANAN = 4

def max(ukuran):
    return ukuran * ukuran - 1

def cekSpasi(i, step, end):
    if step > 0:
        return i+step < end
    return i+step > end

def baris(begin, end, step):
    for i in range(begin, end, step):
        print("%3d" %i, end='')
    print()

def normal(ukuran):
    maximum = max(ukuran)
    for i in range(0, maximum+1, ukuran):
        baris(i, i+ukuran, 1)

def kiri(ukuran):
    maximum = max(ukuran)
    for i in range(ukuran-1, -1, -1):
        baris(i, maximum+1, ukuran)
        maximum -= 1

def kanan(ukuran):
    maximum = max(ukuran)
    begin = maximum-ukuran+1
    for i in range(begin, maximum+1, 1):
        baris(i, i-begin-1, -ukuran)

def atasBawah(ukuran):
    maximum = max(ukuran)
    begin = maximum - ukuran + 1
    for i in range(begin, -1, -ukuran):
        baris(i, i+ukuran, 1)

def kiriKanan(ukuran):
    maximum = max(ukuran)
    begin = ukuran-1
    for i in range(begin, maximum+1, ukuran):
        baris(i, i-begin-1, -1)

BENTUK_BENTUK = {
    MATRIX_NORMAL : normal,
    MATRIX_PUTAR_KIRI : kiri,
    MATRIX_PUTAR_KANAN : kanan,
    MATRIX_PUTAR_ATAS_BAWAH : atasBawah,
    MATRIX_PUTAR_KIRI_KANAN : kiriKanan
}

def logika(ukuran, bentuk):
    if (ukuran < 1 or ukuran > 9):
        return

    if not(bentuk in BENTUK_BENTUK.keys()):
        return
    
    shapeFunc = BENTUK_BENTUK[bentuk]
    shapeFunc(ukuran)

def main():
    try:
        a = int(input())
        b = int(input())
    except:
        print("Inputs are not ints")
    
    logika(a, b)

if __name__ == "__main__":
    main()