# 27.
# 參考以下演算法:
# 1. 輸入n
# 2. 印出n
# 3. 如果n = 1 則停止
# 4. 如果n為奇數，將 n 設為 3n+1
# 5. 否則 n須被除以2
# 6. 回到第二步驟

# 這個問題稱為3n+1 problem，使用以上的演算法，可以得到一個數列，這個數列的長度被稱為n的cycle-length。


# 例如 N = 10 時，代入演算法得出的數列順序為 [10, 5, 16, 8, 4, 2, 1]
# cycle length 為 7。


# 題目要寫一個程式:
# 輸入兩個數字 n, m 兩個整數，(1 <= n <= 10000, n <= m <= 10000)
# 求出介於n, m之間 (包含n, m)的每一個數字使用演算法後所產生出的數列中，最大的 cycle length 為多少。


# 例如當輸入為
# 1
# 10

# 輸出則為:
# 20

# (1~10之間，9 的數列為 [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]，cycle length 為 20)

# ---------------------------------------------------------------------

# 輸入說明:
# 第一行輸入n，n 的範圍 (1 <= n <= 10000)
# 第二行輸入m，m 的範圍 (n <= m <= 10000)

# 輸出說明:
# 對於輸入的n, m，輸出介於n , m之間(包含n, m)的每一個數字使用演算法後所產生出的數列中的最大cycle length。

# 當兩個數字皆輸入完畢，有超出範圍的情況，則輸出"ERROR"字串(不需輸出 cycle length)。
# ---------------------------------------------------------------------
# 範例輸入1:
# 1
# 100

# 範例輸出1:
# 119
# ---------------------------------------------------------------------

# 範例輸入2:
# 10
# 15

# 範例輸出2:
# 18
# ---------------------------------------------------------------------

# 範例輸入3:
# 3333
# 4567

# 範例輸出3:
# 238
# ---------------------------------------------------------------------

# 範例輸入4:
# 20000
# 4
# 範例輸出4:
# ERROR
# ---------------------------------------------------------------------

# 範例輸入5:
# 0
# 10001

# 範例輸出5:
# ERROR
# -------------------------------------------------------------------

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