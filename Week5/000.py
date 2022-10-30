graph = int(input())

if (graph > 0 and graph < 4):
    lines = int(input())
    star = lines // 2 + 1
    if (lines > 2 and lines < 22 and (lines % 2 != 0)):
        if(graph == 1):
            for i in range(1, star + 1):
                print("*" * i)
            for i in range(star - 1, 0, -1):
                print("*" * i)

        elif(graph == 2):
            for i in range(1, star + 1):
                print("." * (star - i) + "*" * i)
            for i in range(star - 1, 0, -1):
                print("." * (star - i) + "*" * i)

        elif(graph ==3):
            for i in range(1, star + 1):
                print("." * (star - i) + "*"*(i*2 - 1))
            for i in range(star - 1, 0, -1):
                print("." * (star - i) + "*"*(i*2 - 1))