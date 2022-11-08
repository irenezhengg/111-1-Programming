# 分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。

# 結果須輸出到小數點第二位
# print("%.2f" %ans)

# ---------------------------------------------------

# 輸入說明

# 第一行，輸入數字num1
# 第二行，輸入數字num2

# ---------------------------------------------------

# 輸出說明

# 第一行輸出Sum:num1+num2
# 第二行輸出Difference:num1-num2
# 第三行輸出Product:num1*num2
# 第四行輸出Quotient:num1/num2

# 加減乘除的結果，輸出到小數點後第二位
# print("%.2f" %ans)

# ---------------------------------------------------

# Example Input 1:
# 25
# 2

# Example Output 1:
# Sum:27.00
# Difference:23.00
# Product:50.00
# Quotient:12.50

# --------------------------------

# Example Input 2:
# -1
# 6

# Example Output 2:
# Sum:5.00
# Difference:-7.00
# Product:-6.00
# Quotient:-0.17

# --------------------------------

# Example Input 3:
# 0
# 9

# Example Output 3:
# Sum:9.00
# Difference:-9.00
# Product:0.00
# Quotient:0.00

num1 = int(input())
num2 = int(input())

sum = num1 + num2
diff = abs(num1 - num2)
quot = num1 / num2
prod = num1 * num2

print("Sum:" + "%.2f"%sum)
print("Difference:" + "%.2f"%diff)
print("Product:" + "%.2f"%prod)
print("Quotient:" + "%.2f"%quot)