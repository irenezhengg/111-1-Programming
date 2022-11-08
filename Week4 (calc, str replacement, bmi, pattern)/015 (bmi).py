# 15 - BMI

# 請設計計算BMI的程式，判斷A, B 兩個人，誰的BMI比較大

# BMI值計算公式: BMI = 體重(公斤) / 身高^2(公尺^2)，例如：一個52公斤的人，身高是155公分，則BMI為 : 52(公斤)/1.55^2 ( 公尺^2 )= 21.6。
# 正常範圍BMI 為 18.5～24 (含18.5與24)。
# 當BMI太大，輸出 Hi {name}, Your BMI: {xxx} too HIGH.
# 當BMI太小，輸出 Hi {name}, Your BMI: {xxx} too LOW.
# 在正常範圍，輸出 Hi {name}, Your BMI: {xxx}.

# 若A比B重，輸出 {A}'s BMI is larger than {B}.
# 若B比A重，輸出 {B}'s BMI is larger than {A}.
# ★ 不會有雙方BMI相同的狀況

# BMI輸出，四捨五入到小數點後第二位 (可用%.2f)。

# ---------------------------------------------------

# 輸入說明 :
# 第一行，輸入一字串，代表A的名字
# 第二行，輸入浮點數 w，代表A的體重
# 第三行，輸入浮點數 h，代表A的身高 (單位為公尺)
# 第四行，輸入一字串，代表B的名字
# 第五行，輸入浮點數 w，代表B的體重
# 第六行，輸入浮點數 h，代表B的身高 (單位為公尺)

# 輸出說明 :
# 第一行，依據A的BMI，輸出A的BMI屬於過重、過輕，還是正常
# 第二行，依據B的BMI，輸出B的BMI屬於過重、過輕，還是正常
# 第三行，輸出A跟B誰的BMI比較大
# 輸出格式請參考題目

# —--------------------------------------------------

# 範例輸入 1說明:
# Andrew (A的名字為 Andrew)
# 123.45 (A的體重為123.45 公斤)
# 1.71 (A的身高為1.71 公尺)
# Kevin (B的名字為 Kevin)
# 81.77 (B的體重為81.77 公斤)
# 1.55 (B的身高為1.55 公尺)

# 範例輸出 1說明:
# Hi Andrew, Your BMI: 42.22 too HIGH. (A的BMI為42.218，輸出成42.22，BMI過重)
# Hi Kevin, Your BMI: 34.04 too HIGH. (B的BMI為34.035，輸出成34.04，BMI過重)
# Andrew's BMI is larger than Kevin. (A的BMI比B大)

# —--------------------------------------------------

# 範例輸入4說明:
# Anthony (A的名字為 Anthony )
# 45 (A的體重為45 公斤)
# 1.68 (A的身高為1.68 公尺)
# Mary (B的名字為 Mary )
# 100 (B的體重為100 公斤)
# 1.69 (B的身高為1.69 公尺)

# 範例輸出 4說明:
# Hi Anthony, Your BMI: 15.94 too LOW. (A的BMI為15.943，輸出成15.94，BMI過輕)
# Hi Mary, Your BMI: 35.01 too HIGH. (B的BMI為35.012，輸出成35.01，BMI過重)
# Mary's BMI is larger than Anthony. (B的BMI比A大)

# —--------------------------------------------------


# 範例輸入1:
# Andrew
# 123.45
# 1.71
# Kevin
# 81.77
# 1.55

# 範例輸出 1:
# Hi Andrew, Your BMI: 42.22 too HIGH.
# Hi Kevin, Your BMI: 34.04 too HIGH.
# Andrew's BMI is larger than Kevin.

# —--------------------------------------------------

# 範例輸入2:
# John
# 77.66
# 1.23
# Henry
# 40.7
# 1.6

# 範例輸出 2:
# Hi John, Your BMI: 51.33 too HIGH.
# Hi Henry, Your BMI: 15.90 too LOW.
# John's BMI is larger than Henry.

# —--------------------------------------------------

# 範例輸入3:
# Larry
# 60
# 1.72
# Bob
# 70
# 1.80

# 範例輸出 3:
# Hi Larry, Your BMI: 20.28.
# Hi Bob, Your BMI: 21.60.
# Bob's BMI is larger than Larry.

# —--------------------------------------------------

# 範例輸入4:
# Anthony
# 45
# 1.68
# Mary
# 100
# 1.69

# 範例輸出 4:
# Hi Anthony, Your BMI: 15.94 too LOW.
# Hi Mary, Your BMI: 35.01 too HIGH.
# Mary's BMI is larger than Anthony.

# —--------------------------------------------------

# 範例輸入5:
# Jeff
# 30
# 1.32
# Randy
# 50
# 1.85

# 範例輸出 5:
# Hi Jeff, Your BMI: 17.22 too LOW.
# Hi Randy, Your BMI: 14.61 too LOW.
# Jeff's BMI is larger than Randy.

def calc_BMI1(name1, H1, W1):
    BMI1 = W1 / (H1**2)
    if BMI1 > 24 :
        print("Hi",name1+", Your BMI:","%.2f"%BMI1,"too HIGH.")
    elif BMI1 <18.5:
        print("Hi",name1+", Your BMI:","%.2f"%BMI1,"too LOW.")
    else:
        print("Hi",name1+", Your BMI:","%.2f"%BMI1+".")

def calc_BMI2(name2, H2, W2):
    BMI2 = W2 / (H2**2)
    if BMI2 > 24 :
        print("Hi",name2+", Your BMI:","%.2f"%BMI2,"too HIGH.")
    elif BMI2 <18.5:
        print("Hi",name2+", Your BMI:","%.2f"%BMI2,"too LOW.")
    else:
        print("Hi",name2+", Your BMI:","%.2f"%BMI2+".")

def compare(name1, H1, W1, name2, H2, W2):
    BMI1 = W1 / (H1**2)
    BMI2 = W2 / (H2**2)
    if BMI1 > BMI2:
        print('{}\'s BMI is larger than {}.'. format(name1, name2))
    else:
        print('{}\'s BMI is larger than {}.'. format(name2, name1))
        
name1 = input()
W1 = float(input())
H1 = float(input())

name2 = input()
W2 = float(input())
H2 = float(input())

calc_BMI1(name1, H1, W1)
calc_BMI2(name2, H2, W2)
compare(name1, H1, W1, name2, H2, W2)