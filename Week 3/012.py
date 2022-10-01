WINDY = 1
NO_WINDY = 0
VALUE_ERROR = -1

def reason(celcius, humid, air):
    if(celcius < 0 or celcius > 100):
        return REPORT_ERROR
    
    if(humid < 0 or humid > 100):
        return REPORT_ERROR
    
    if(air == WINDY):
        air = True
    elif(air == NO_WINDY):
        air = False
    else:
        return REPORT_ERROR

    if (celcius>=50):
        return 18

    if (celcius<25):
        return "Today is cool"

    if ((celcius >= 30 and not(air)) or humid >= 85):
        return 24
    
    if ((celcius>= 25 and celcius <= 29) and (((humid >= 60 and humid <= 84) and air) or (humid < 60 and not(air)))):
        return 27

    return "Today is cool"

def main():
    temp = input()
    humid = input()
    wind = input()

    try:
        temp = int(temp)
        humid = int(humid)
        wind = int(wind)
    except:
        print("Input errors: please try inputting ints for all of them.")
        return

    Stats = reason(temp, humid, wind)
    if (Stats == VALUE_ERROR):
        print("Internal Error, please try again.")
        return

    print(Stats)

if __name__ == '__main__':
    main()