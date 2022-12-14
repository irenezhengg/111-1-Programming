# A25.
# 請繪製兩個不同的圖形:
# 1. 井字號、星號、英文字母的複合圖形
# 2. 數字、星號的複合圖形

# 給予兩個正整數 N、M
# N 代表要繪製的圖形種類，N的範圍為 (1 <= N <= 2)
# M 代表要繪製的圖形高度，M的範圍有兩種情況
# 當 N = 1 時，代表繪製井字號、英文字母、星號的複合圖形，M的範圍為(2 <= M <= 29)
# 當 N = 2 時，代表繪製數字、星號的複合圖形，M的範圍為(1 <= M <= 9)
# 當 N 不為 1 或 2 時，輸出ERROR字串並結束程式


# 當N = 1時，輸出格式為：
# 第一層為 M - 1 個井字號、1 個星號、 M - 1個井字號
# 第二層為 M - 2 個井字號、1 個英文字母與 2 個星號、M - 2個井字號
# 第三層為 M - 3 個井字號、2 個英文字母與 3 個星號、M - 3個井字號
# 井字號、英文字母、星號的數量，依照規則以層數以此類推，直到 M 行結束。

# 除了第一層外，每層的英文字母以A、B、C作為循環。規則如下:
# 第二層的英文字母為A
# 第三層的英文字母為B
# 第四層的英文字母為C
# 第五層的英文字母回到A，以此類推循環，直到M行結束。
# 例如當N = 1, M = 5時 :
# 1
# 5

# 輸出圖形為：
# ####*####
# ###*A*###
# ##*B*B*##
# #*C*C*C*#
# *A*A*A*A*

# 當 N = 2 時，輸出格式為：
# 第一行為 數字 1 及 M * 2 個星號 及 數字 1 。
# 第二行為 數字 1 到 2 及 (M - 1)*2 個星號 及 數字 2 到 1。
# 第三行為 數字 1 到 3 及 (M - 2)*2 個星號 及 數字 3 到 1。
# 數字的範圍和星號的數量，依照規則以層數以此類推，直到M行結束。

#  
# 例如當N = 2, M = 5 時:
# 2
# 5

# 輸出圖形為：
# 1**********1
# 12********21
# 123******321
# 1234****4321
# 12345**54321

# 請注意：
# 若M不在上述的範圍內，直接輸出ERROR並結束程式。


# 輸入說明：
# 第一行輸入一整數N
# 當N = 1時，代表要繪製井字號、英文字母、星號的複合圖形
# 當N = 2時，代表要繪製數字、星號的複合圖形

# 第二行輸入對應代表圖形的高度M
# 若N = 1時，M的範圍為1 <= M <= 9
# 若N = 2時，M的範圍為2 <= M <= 29

# 輸出說明:
# 若N = 1時，輸出依照題目規則，有M行高的井字號、英文字母、星號的複合圖形。

# 若M數值範圍不在2 <= M <= 29，輸出ERROR並結束程式，不必輸出圖形

# 若N = 2時，輸出依照題目規則，有M行高的數字、星號複合圖形。
# 若M的數值範圍不在1 <= M <= 9，則輸出ERROR並結束程式，不必輸出圖形。

# 當N不為1或2時，則輸出ERROR並且結束程式，不需等待輸入M

# -------------------------------------------------------------------------------------------------
# 範例輸入1:
# 1
# 3

# 範例輸出1:
# ##*##
# #*A*#
# *B*B*

# -------------------------------------------------------------------------------------------------
# 範例輸入2:
# 1
# 7

# 範例輸出2:
# ######*######
# #####*A*#####
# ####*B*B*####
# ###*C*C*C*###
# ##*A*A*A*A*##
# #*B*B*B*B*B*#
# *C*C*C*C*C*C*

# -------------------------------------------------------------------------------------------------
# 範例輸入3:
# 1
# 30

# 範例輸出3:
# ERROR

# -------------------------------------------------------------------------------------------------
# 範例輸入4:
# 2
# 3

# 範例輸入4:
# 1******1
# 12****21
# 123**321

# -------------------------------------------------------------------------------------------------
# 範例輸入5:
# 2
# 7

# 範例輸入5:
# 1**************1
# 12************21
# 123**********321
# 1234********4321
# 12345******54321
# 123456****654321
# 1234567**7654321

# -------------------------------------------------------------------------------------------------
# 範例輸入6:
# 2
# 10

# 範例輸入6:
# ERROR

# -------------------------------------------------------------------------------------------------

# 範例輸入7:
# 3

# 範例輸入7:
# ERROR

# -------------------------------------------------------------------------------------------------

ERROR = "ERROR"
LETTER_CHOICE = {
    0 : "C",
    1 : "A",
    2 : "B"
}

def printAlpha(ukuran):
    if (ukuran < 2 or ukuran > 29):
        print(ERROR)
        return

    panjang = ukuran * 2 - 1
    lapisan = ukuran - 1

    for i in range(0, ukuran, 1):
        print((lapisan - i ) * "#", end='')
        print("*", end = '')

        letterCode = i%3

        for j in range(0, i, 1):
            print(LETTER_CHOICE[letterCode], end='')
            print("*", end='')
        
        print((lapisan - i ) * "#", end='')
        print()


def Stars(ukuran):
    if (ukuran < 2 or ukuran > 9):
        print(ERROR)
        return

    panjang = ukuran * 2 + 2

    for i in range(1, ukuran+1):
        starsNumber = panjang - 2 * i
        for j in range(1, i+1, 1):
            print(j, end='')
        print(starsNumber * "*", end = '')
        for j in range(i, 0, -1):
            print(j, end='')
        print()
        
PILIHAN_BENTUK = {
    1 : printAlpha,
    2 : Stars
}

def logika(type, ukuran):
    function = PILIHAN_BENTUK[type]
    function(ukuran)


def main():
    try:
        x = int(input())
        
        if not(x in PILIHAN_BENTUK.keys()):
            print(ERROR)
            return

        y = int(input())
        
    
    except:
        print("Inputs are not ints")

    logika(x, y)

if __name__ == '__main__':
    main()