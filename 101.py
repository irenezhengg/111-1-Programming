from random import randint

def exit(inputUser):
    if inputUser == 'exit':
            return 0, True
    inputUser = [eval(i) for i in list(str(input))]
    return inputUser, False

def game(listTebak):
    tebakan = 0
    while True:
        inputUser = input("Please guess a number: ")
        inputUser, chkExit = exit(inputUser)
        if chkExit:
            return tebakan, False
        
        while True:
            if len(listTebak) < len(inputUser):
                inputUser = input("the number is too long!")
                inputUser, chkExit = exit(inputUser)
                if chkExit:
                    return tebakan, False
                continue
            if len(listTebak) > len(inputUser):
                inputUser = input("the number is too short!")
                inputUser, chkExit = exit(inputUser)
                if chkExit:
                    return tebakan, False
                continue
            break
        
        A = 0
        B = 0
        tebakan += 1
        
        if len(listTebak) != len(inputUser):
            return -1, False

        for i in range (0, len(listTebak)):
            if listTebak[i] == inputUser[i]:
                A += 1
                continue
            for j in range(0, len(inputUser)):
                if listTebak[i] == inputUser[j]:
                    B += 1
                    break

        print("%d A, %d B" %(A, B))
        if(A == len(listTebak)):
            return tebakan, True

def main():
    print("Welcome to the A and B Game and a 4-digit number is generated")
    print("You get a B for every number that is in the wrong place. You get an A for every correct answer.\nWhen you get four As, the game is over!")
    print("To exit, type exit at any prompt.")
    nomorAcak = randint(1, 10000)
    nomorListTebak = [eval(i) for i in list(str(nomorAcak))]

    tebakan, exitTrigger = game(nomorListTebak)

    if tebakan == -1:
        return 1

    if exitTrigger:
        print("Congratulations you did it in %d tries!" %tebakan)
        return 0
    
    print("You tried for %d times and the number is %d." %(tebakan, nomorAcak))
    print("\tBetter Luck Next time!")
    

if __name__ == '__main__':
    main()