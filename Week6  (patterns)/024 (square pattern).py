# 24.

# 今天給予兩個正整數N (1 <= N <= 9) 與 D(0 <= D <= 4)
# N代表 n*n的數字矩陣，D代表方向

# 方向分為以下五種方式實作：
# D = 0，矩陣維持原樣
# D = 1，矩陣向左旋轉90度
# D = 2，矩陣向右旋轉90度
# D = 3，矩陣上下翻轉
# D = 4，矩陣左右翻轉

# 請使用迴圈並給予其中一種方向，印出 0 ~ n * n – 1的數字矩陣，數字之間請使用字串格式化 '%3d' 進行排版。

# 例如：
# N = 5，D = 0，則輸出圖形如下


# -------------------------------------------------------------------------------------------------
# N = 7， D = 1，則輸出圖形如下


# ------------------------------------------------------------------------------------------------- 

# 輸入說明：
# 第一行輸入正整數N，N代表n*n的數字矩陣 (1 <= N <= 9)
# 第二行輸入正整數D，D代表數字矩陣的方向 (0 <= D <= 4)

# 輸出說明：
# 根據大小以及選擇的方向印出n*n的數字矩陣，數字之間使用字串格式化 ’%3d’ 進行排版對齊。

# -------------------------------------------------------------------------------------------------
# 範例輸入1：
# 5
# 1

# 範例輸出1：


# -------------------------------------------------------------------------------------------------

# 範例輸入2：
# 3
# 2

# 範例輸出2：


# -------------------------------------------------------------------------------------------------
#  
# 範例輸入3：
# 7
# 0

# 範例輸出3：


# -------------------------------------------------------------------------------------------------

# 範例輸入4：
# 9
# 3

# 範例輸出4：


# -------------------------------------------------------------------------------------------------
#  
# 範例輸入5：
# 8
# 4

# 範例輸出5：

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