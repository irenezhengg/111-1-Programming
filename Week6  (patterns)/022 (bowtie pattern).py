# 22.

# 今天小明想要畫出一個圖形，圖形是沙漏與蝴蝶結的複合形狀
# 現在給予一個正整數N，N為圖形高度，範圍為 (4 <= N <= 30)

# 當N為偶數或是超出範圍的情況則須輸出Error並結束程式(不須輸出圖形)
# 當N為奇數的情況則正常輸出圖形

# 圖形由星號和底線組成，且星號為蝴蝶結的形狀、底線為沙漏的形狀
# 每一行使用星號做開頭與結尾，中間由底線填滿
# 每一行星號有(2n-1) * 2個、底線有N * 2 - (2n-1) * 2個

# 圖形可分成上半段和下半段
# 上半段為第1行到第 (N // 2 + 1) 行
# 下半段為第 (N // 2 + 2) 行到第 N 行

# 上半段的星號數量由上而下遞增，底線數量由上而下遞減
# 下半段的星號數量由上而下遞減，底線數量由上而下遞增

# 例如N = 9
# 上半段則為第1行到第5行的複合圖形，下半段則為第6行到第9行
# 則輸出圖形為：
# *________________*
# ***____________***
# *****________*****
# *******____*******
# ******************
# *******____*******
# *****________*****
# ***____________***
# *________________*

# -------------------------------------------------------------------------------------------------
#  

# 輸入說明：
# 第一行輸入正整數N (4 <= N <= 30)，代表圖形的大小

# 輸出說明：
# 輸出沙漏與蝴蝶結的複合圖形，大小為N
# 當N為偶數或是超出範圍時，輸出Error並結束程式(不須輸出圖形)
# -------------------------------------------------------------------------------------------------

# 範例輸入1：
# 5

# 範例輸出1：
# *________*
# ***____***
# **********
# ***____***
# *________*

# -------------------------------------------------------------------------------------------------

# 範例輸入2：
# 7

# 範例輸出2：
# *____________*
# ***________***
# *****____*****
# **************
# *****____*****
# ***________***
# *____________*

# -------------------------------------------------------------------------------------------------
#  

# 範例輸入3：
# 11

# 範例輸出3：
# *____________________*
# ***________________***
# *****____________*****
# *******________*******
# *********____*********
# **********************
# *********____*********
# *******________*******
# *****____________*****
# ***________________***
# *____________________*

# -------------------------------------------------------------------------------------------------

# 範例輸入4：
# 4

# 範例輸出4：
# Error

# -------------------------------------------------------------------------------------------------

# 範例輸入5：
# 32

# 範例輸出5：
# Error

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