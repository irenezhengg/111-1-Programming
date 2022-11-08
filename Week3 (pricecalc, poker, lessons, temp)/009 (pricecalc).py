# 009.
# 蘋果、奇異果、鳳梨，三種水果價格及折扣表如下，且老闆為了回饋社會，決定再加碼，購買總顆數(三種水果加起來) 達30顆，總金額再打8.7折。
# 今一顧客欲購買，蘋果:ｘ顆、 奇異果:ｙ顆、鳳梨:ｚ顆（x、y、z 為使用者輸入），
# 請計算本次購買需花費多少錢？
# (若計算出的最終結果有小數，則直接無條件捨去小數點後的數字；所有計算過程都使用小數，只有在輸出結果時使用整數輸出)

# -------------------------------------------------------------------
# ------------| 定價 | 1~10顆 | 11~15顆 | 16~20顆 | 21顆以上 (含21顆) |
# -------------------------------------------------------------------
# | 蘋果-----| 30---| 原價----| 9.5折-----| 9折-------| 8折----|
# -------------------------------------------------------------------
# | 奇異果--| 70---| 原價----| 9折-------| 8.5折-----| 7.5折-|
# -------------------------------------------------------------------
# | 鳳梨-----| 40---| 原價----| 8.5折-----| 8折-------| 8折---|
# -------------------------------------------------------------------

# -------------------------------------------------------------------

# 輸入說明:
# 第一行，輸入購買 x 顆蘋果
# 第二行，輸入購買 y 顆奇異果
# 第三行，輸入購買 z 顆鳳梨

# 輸出說明:
# 請輸出最後花費的總金錢

# -------------------------------------------------------------------

# 範例輸入 1說明:
# 10 (購買 10 顆蘋果)
# 10 (購買 10 顆奇異果)
# 10 (購買 10 顆鳳梨)

# 範例輸出 1說明:
# 1218
# (10顆蘋果共300元，10個奇異果共700元，10個鳳梨共400元，共1400元
# 總共買了30顆水果，打8.7折，1400 * 0.87 = 1218)

# -------------------------------------------------------------------

# Example Input 1：
# 10
# 10
# 10

# Example Output 1：
# 1218

# -------------------------------------------------------------------

# Example Input 2：
# 10
# 16
# 20

# Example Output 2：
# 1646

# -------------------------------------------------------------------

# Example Input 3：
# 0
# 30
# 0

# Example Output 3：
# 1370

# -------------------------------------------------------------------

# Example Input 4：
# 1
# 5
# 60

# Example Output 4：
# 2001

# -------------------------------------------------------------------

# Example Input 5：
# 21
# 21
# 21

# Example Output 5：
# 1982

# -------------------------------------------------------------------

# Example Input 6：
# 1
# 2
# 3

# Example Output 6：
# 290

# -------------------------------------------------------------------

# Example Input 7：
# 15
# 15
# 15

# Example Output 7：
# 1637

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    discount1 = [1.0, 0.95, 0.9, 0.8]
    discount2 = [1.0, 0.9 , 0.85, 0.75]
    discount3 = [1.0, 0.85, 0.8, 0.8]
    priceA = price(n1,discount1)
    priceB = price(n2,discount2)
    priceC = price(n3,discount3)
    total = (n1*30*priceA) + (n2*70*priceB) + (n3*40*priceC)
    result(total,n1,n2,n3)
    print('%d'%result(total,n1,n2,n3))

def price(x,y):
    price = 0
    if (x >= 21):
        price = y[3]
    elif (x >= 16):
        price = y[2]
    elif (x >= 11):
        price = y[1]
    elif (x >= 1):
        price = y[0]
    return price

def result(total,n1,n2,n3):
    amount = n1 + n2 + n3
    result = 0
    if (amount >= 30):
        result += total * 0.87
    else:
        result += total * 1
    return result
    
main()