# 007.
# 輸入為一個英文句子以及一個單字，
# 請print出句子的長度，並且把句子以輸入的單字進行分割後輸出。

# ---------------------------------------------------

# 輸入說明：
# 第一行，一個英文句子
# 第二行，一個在第一行的英文句子中有出現的單字

# 輸出說明：
# 第一行輸出句子的長度
# 第二行輸出以單字進行分割後的句子
# ★請注意第二行輸出的句子的輸出格式是否正確

# ---------------------------------------------------

# Example Input 1:
# Those who turn back never reach the summit.
# who

# Example Output 1:
# 43
# ['Those ', ' turn back never reach the summit.']

# ---------------------------------------------------

# Example Input 2:
# Bravery never goes out of fashion.
# never

# Example Output 2:
# 34
# ['Bravery ', ' goes out of fashion.']

# ---------------------------------------------------

# Example Input 3:
# A man is not old as long as he is seeking something.
# is

# Example Output 3:
# 52
# ['A man ', ' not old as long as he ', ' seeking something.']

# ---------------------------------------------------

# Example Input 4:
# Do the right thing Do Things Right
# Do

# Example Output 4:
# 34
# ['', ' the right thing ', ' Things Right']

pp = input()
word = input()

print(len(pp))

op = pp.split(word)
print(op)