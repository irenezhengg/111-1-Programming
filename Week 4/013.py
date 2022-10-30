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