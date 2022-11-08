# A、B、C三本書價格如下，一顧客欲購買A:ｘ本、B:ｙ本、C:ｚ本（ｘ、ｙ、ｚ為使用者輸入），請計算需花費多少錢？

# 定價
# A 380
# B 1200
# C 180

# ---------------------
# Example input:
# 8
# 9
# 5

# Example output:
# 14740
# ---------------------
# Example input:
# 0
# 0
# 0

# Example output:
# 0
# ---------------------
# Example input:
# 1
# 0
# 4

# Example output:
# 1100
# ---------------------

num1 = int(input())
num2 = int(input())
num3 = int(input())

a = int(380)
b = int(1200)
c = int(180)

sum = num1*a + num2*b + num3*c

print(str(sum))