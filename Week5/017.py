# rows = int(input())

# exampleOne
# for i in range(1, rows+1):
#     for j in range(1,i+1):
#         print(j, end='')
    
#     for j in range(i-1,0,-1):
#         print(j, end='')

#     print("")


# exampleTwo
# for i in range(1,rows+1):
    
#     for j in range(1, rows+1-i):
#         print('_', end='')

#     for j in range(1,i+1):
#         print(j, end='')
    
#     for j in range(i-1,0,-1):
#         print(j, end='')
    
#     for j in range(1, rows+1-i):
#         print('_', end='')
    
#     print()

# exampleThree
# for i in range(rows,0, -1):
#     for j in range(rows-i):
#         print('_', end='') 

#     for j in range(1,i+1):
#         print(j, end='')

#     for j in range(i-1,0,-1):
#         print(j, end='')
    
#     for j in range(rows-i):
#         print('_', end='')

#     print()

def main():
    shape = int(input())
    rows = int(input())
    picture(shape,rows)

def picture(x,y):
    if (x==1):
        for i in range(1, y+1):
            for j in range(1,i+1):
                print(j, end='')
    
            for j in range(i-1,0,-1):
                print(j, end='')
            print("")

    elif (x==2):
        for i in range(1,y+1):
            for j in range(1, y+1-i):
                print('_', end='')
            for j in range(1,i+1):
                print(j, end='')
            for j in range(i-1,0,-1):
                print(j, end='')
            for j in range(1, y+1-i):
                print('_', end='')
            print()

    elif (x==3):        
        for i in range(y,0, -1):
            for j in range(y-i):
                print('_', end='') 
            for j in range(1,i+1):
                print(j, end='')
            for j in range(i-1,0,-1):
                print(j, end='')
            for j in range(y-i):
                print('_', end='')
            print()

main()
    