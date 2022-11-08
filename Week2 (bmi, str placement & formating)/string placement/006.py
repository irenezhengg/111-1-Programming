# 006.
# 1. 輸入兩個英文句子 A, B，兩個字串 x, y
# 2. 將兩個英文句子A, B 串聯成 句子C
# 3. 將句子C其中的字串x 取代成 字串y，另其變成句子D
# 4. 輸出句子C, 句子D長度的加總
# 5. 把句子D 前三個字以及最後三個字組合成 句子E
# 6. 重複輸出三次句子E

# ---------------------------------------------------

# 輸入說明：
# 第一行，輸入英文句子 A
# 第二行，輸入英文句子 B
# 第三行，輸入字串 x
# 第四行，輸入字串 y

# 輸出說明：
# 第一行，輸出句子C, 句子D長度的加總
# 第二行，重複輸出三次句子E

# ---------------------------------------------------

# 範例輸入 1 說明:
# This is a book (句子A)
# That is a cat (句子 B)
# is (字串 x)
# was (字串 y)

# 句子C為This is a bookThat is a cat
# 句子D為Thwas was a bookThat was a cat
# 句子E為Thwcat

# 範例輸出 1 說明:
# 57 (句子C長度為27，句子D長度為30，總和為57)
# ThwcatThwcatThwcat (句子E為Thwcat，重複三次為ThwcatThwcatThwcat)

# ---------------------------------------------------

# Example Input 1:
# This is a book
# That is a cat
# is
# was


# Example Output 1:
# 57
# ThwcatThwcatThwcat

# ---------------------------------------------------

# Example Input 2:
# I have a pen
# I have an apple
# pineapple
# watermelon


# Example Output 2:
# 54
# I hpleI hpleI hple

# ---------------------------------------------------

# Example Input 3:
# My name is Jeff
# My name is Jeff
# _
# !!


# Example Output 3:
# 60
# My effMy effMy eff

A = input()
B = input()
x = input()
y = input()

C = A + B

D = C.replace(x, y)

print(len(C + D))
E = D[:3] + D[-3::]
print(E * 3)