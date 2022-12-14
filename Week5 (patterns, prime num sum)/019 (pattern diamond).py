# 19 -

# 現在題目給魚的大小，請你畫出這條魚，魚的頭朝向左邊，尾巴在右邊

# 魚由身體 (菱形) 跟 尾巴 (三角形) 兩個部分組成
# 身體的高度為N，(3 <= N <= 100)，且N為奇數
# 尾巴的高度為(N-2)

# 如果N為偶數，請輸出ERROR，並結束程式，不必輸出圖形

# 身體部分使用*號，尾巴部分使用+號

# 魚的身體由菱形組成，是一個對角線長度皆為 N 的菱形

# 魚的尾巴由三角形組成，三角形的最長邊(底邊)在右，頂端朝左
# 是一個底為(N-2)，高也為(N-2)的三角形

# 為了讓尾巴在身體的右方，需要在尾巴跟身體之間加入一些空白字元

# 請注意，整個圖形的第1行與第N行不含尾巴

# 例如:
# N = 9
# 輸出圖形: (輸出以圖片為準:https://ppt.cc/fVKEEx)
#         *
#       *****            +
#     *********        +++
#   *************    +++++
# *****************+++++++
#   *************    +++++
#     *********        +++
#       *****            +
#         *


# ---------------------------------------------------

# 輸入說明 :
# 第一行，輸入整數 N (3 <= N <= 100) ， 代表魚的大小

# 輸出說明 :
# 輸出大小為N的魚 (魚的圖形請參考範例測資)
# 如果N為偶數，請輸出ERROR，並結束程式 (不用輸出圖形)

# ---------------------------------------------------

# 範例輸入 1: (輸出以圖片為準: https://ppt.cc/f3Zywx)
# 3

# 範例輸出 1:
#   *
# *****+
#   *

# ---------------------------------------------------

# 範例輸入 2: (輸出以圖片為準: https://ppt.cc/fDyiPx)
# 5

# 範例輸出 2:
#     *
#   *****    +
# *********+++
#   *****    +
#     *

# ---------------------------------------------------

# 範例輸入 3: (輸出以圖片為準: https://ppt.cc/fVKEEx)
# 9

# 範例輸出 3:
#         *
#       *****            +
#     *********        +++
#   *************    +++++
# *****************+++++++
#   *************    +++++
#     *********        +++
#       *****            +
#         *

# ---------------------------------------------------

# 範例輸入 4:
# 4

# 範例輸出 4:
# ERROR



def entahApa(baris, ukuran):
    marginSize = ukuran - 1 - (2 * baris)
    print(marginSize * " ", end = '')
    print(2 * baris * "*", end = '')
    print("*", end='')
    print(2 * baris * "*", end = '')
    print(2 * marginSize * " ", end = '')
    print(2 * (baris-1) * "+", end='')
    if (baris > 0):
        print("+", end="")

def logika(ukuran):
    for i in range(0, ukuran//2, 1):
        entahApa(i, ukuran)
        print()
    for j in range(ukuran//2, -1, -1):
        entahApa(j, ukuran)
        print()


def main():
    ukuran = input()

    try:
        ukuran = int(ukuran)
    except:
        print("Inputs are not ints!")

    if (ukuran%2 == 0):
        print("ERROR")
        return

    logika(ukuran)

if __name__ == '__main__':
    main()