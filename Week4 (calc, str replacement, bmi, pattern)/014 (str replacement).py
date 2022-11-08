# 14 -

# 輸入N個字串，請執行以下操作
# 1. 印出這N個字串中所有的小寫字母
# (注意:若沒有字串中沒有小寫字母則輸出'No lowercase letters')
# 2. 輸出這N個字串中所有大寫字元的數量
# 3. 輸出這N個字串共有多少個字元 (含標點符號與空格)
# 4. 以空格分割這N個字串，將其中長度最長的單字輸出

# ---------------------------------------------------

# 輸入說明 :
# 第一行，輸入整數 N，代表接下來有N行輸入
# 第二 ~ N+1 行，輸入的字串，根據這N行執行操作1~4

# 輸出說明 :
# 第一行，輸出N個字串中所有的小寫字母
# 第二行，輸出N個字串中所有大寫字元的數量
# 第三行，輸出N個字串中所有字元的數量 (含標點符號、特殊字元與空格)
# 第四行，輸出以空格分割這N個字串後，其中長度最長的字串；若有多個長度最長的字串，輸出最早出現的字串

# ---------------------------------------------------

# 範例輸入 1說明:
# 2 (接下來輸入2行)
# I have a pen I have an apple
# Pen pineapple apple pen

# 範例輸出 1說明:
# haveapenhaveanappleenpineappleapplepen (輸入的2個字串所有小寫字元)
# 3 (輸入的2個字串總共有2個大寫字元 (2個I))
# 51 (輸入的2個字串共有51個字元)
# pineapple (以空格切分輸入的2個字串後，得到的所有字串為['I', 'have', 'a', 'pen', 'I', 'have', 'an', 'apple', 'Pen', 'pineapple', 'apple', 'pen']，其中最長的字串為'pineapple')

# ---------------------------------------------------

# 範例輸入 3說明:
# 2 (接下來輸入2行)
# THE END OF THE WORLD
# FINALE OF THE SHOW

# 範例輸出 3說明:
# No lowercase letters (輸入的2個字串沒有任何小寫字元)
# 31 (輸入的2個字串共有31個大寫字元)
# 38 (輸入的2個字串共有38個字元)
# FINALE (以空格切分輸入的2個字串後，得到的所有字串為['THE', 'END', 'OF', 'THE', 'WORLD', 'FINALE', 'OF', 'THE', 'SHOW']，其中最長的字串為'FINALE')

# ---------------------------------------------------

# 範例輸入 1:
# 2
# I have a pen I have an apple
# Pen pineapple apple pen

# 範例輸出 1:
# haveapenhaveanappleenpineappleapplepen
# 3
# 51
# pineapple

# —--------------------------------------------------

# 範例輸入 2:
# 5
# There's a growing trend among teenagers
# A dead duck does not fly backward
# I would be delighted
# A song can make or ruin a person’s day
# The pigs were insulted

# 範例輸出 2:
# heresagrowingtrendamongteenagersdeadduckdoesnotflybackwardwouldbedelightedsongcanmakeorruinapersonsdayhepigswereinsulted
# 5
# 152
# teenagers

# —--------------------------------------------------

# 範例輸入 3:
# 2
# THE END OF THE WORLD
# FINALE OF THE SHOW

# 範例輸出 3:
# No lowercase letters
# 31
# 38
# FINALE

# —--------------------------------------------------

# 範例輸入4:
# 2
# *&^$(*#&%*#&$^&%*@^&
# *&%#(*&#%(*&%Cry*$&%(&$%

# 範例輸出 4:
# ry
# 1
# 44
# *&%#(*&#%(*&%Cry*$&%(&$%

def main():
    number = int(input())
    sentence = [input() for _ in range(number)]
    sentence_joined = ''.join(sentence)
    sentence_joined2 = ' '.join(sentence)
    sentence_lower = lower(sentence_joined)
    sentence_upper = upper(sentence_joined)

    if (len(sentence_lower) == 0):
        print ("No lowercase letters")
    else:
        for i in sentence_lower:   
            print(i,end="")
        print("")

    if (len(sentence_upper) == 0):
        print ("No uppercase letters")
    else:  
            print(len(sentence_upper))

    print(len(sentence_joined))

    longest = max(sentence_joined2.split(), key=len)
    print(longest)

def lower(x):
    new_sentence =[]
    for i in x:
        if (i.islower()):
            new_sentence += i
    return new_sentence

def upper(x):
    new_sentence =[]
    for i in x:
        if (i.isupper()):
            new_sentence += i
    return new_sentence

main()
    