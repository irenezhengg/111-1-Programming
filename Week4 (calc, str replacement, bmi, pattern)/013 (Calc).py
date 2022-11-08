# 013:

# 輸入m, n, a, b 四個整數，請計算m ~ n 之間等差為a的數列總和、等差為b的數列的乘積，

# 計算方式如下:
# 1. m ~ n 之間 等差為a的和:
# m + (m+a) + (m+a*2) + (m+a*3) + ...

# 2. m ~ n 之間 等差為b的積:
# m * (m+b) * (m+b*2) * (m+b*3) * ...

# ---------------------------------------------------

# 輸入說明 :
# 第一行，輸入整數 m
# 第二行，輸入整數 n
# 第三行，輸入整數 a
# 第四行，輸入整數 b

# 輸出說明 :
# 第一行輸出 m ~ n 之間 等差為a的數列的總和
# 第二行輸出 m ~ n 之間 等差為b的數列的乘積

# ---------------------------------------------------

# 範例輸入 1說明:
# 2
# 10
# 2
# 3

# 範例輸出 1說明:
# 30 (2~10之間等差為2的數列為: [2, 4, 6, 8, 10]，總和為30)
# 80 (2~10之間等差為3的數列為: [2, 5, 8]，乘積為80)

# ---------------------------------------------------

# 範例輸入 4說明:
# -20
# 7
# 4
# 6

# 範例輸出 4說明:
# -56 (-20~7之間等差為4的數列為: [-20, -16, -12, -8, -4, 0, 4]，總和為-56)
# 17920 (-20~7之間等差為4的數列為: [-20, -14, -8, -2, 4]，乘積為17920)

# ---------------------------------------------------


# 範例輸入1:
# 2
# 10
# 2
# 3

# 範例輸出 1:
# 30
# 80

# —--------------------------------------------------

# 範例輸入2:
# 1
# 1
# 3
# 4

# 範例輸出 2:
# 1
# 1

# —--------------------------------------------------

# 範例輸入3:
# -100
# 100
# 2
# 3

# 範例輸出 3:
# 0
# 1933377063266786171556383835915513372677928926645598788472757611806350392456590325815705600000000000000000

# —--------------------------------------------------

# 範例輸入4:
# -20
# 7
# 4
# 6

# 範例輸出 4:
# -56
# 17920

def main():
    m = int(input())
    n = int(input())
    a = int(input())
    b = int(input())
    c, d = calculate(m,n,a,b)
    print(c)
    print(d)

def calculate(m,n,a,b):
    sum = 0
    for i in range (m, n+1, a):
        sum += i
    multi = 1
    for i in range (m, n+1, b):
        multi *= i
    return sum,multi 

main()