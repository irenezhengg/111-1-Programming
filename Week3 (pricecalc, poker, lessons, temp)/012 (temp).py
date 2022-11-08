# 012.
# 今天好熱好熱，好想開冷氣
# 給你今天的溫度 (0 ~ 100)、濕度 (0 ~ 100)，有沒有起風 (0、1，0代表沒風，1代表有風)
# 請根據以下條件，幫忙決定一下今天要不要開冷氣，如果要開冷氣，請決定要設定幾度
# 1. 如果 溫度高於 50 (含50)，不論濕度、有無起風，一律開冷氣且設定18度
# 2. 如果 溫度低於 25 (不含25)，不論濕度、有無起風，一律不開冷氣
# 3. 如果 溫度高於 30 (含30) 而且沒有風，或濕度大於85(含85)，則開冷氣且設定為24度
# 4. 如果 溫度介於 25到29之間 (含25跟29) 且濕度介於60到84(含60跟84)且有起風，或溫度介於 25到29之間 (含25跟29) 且濕度小於60(不含60)且無起風，則開冷氣且設定為27度
# 5. 除此之外的狀況皆不開冷氣
# ★若條件重複，以條件標號數字較小者優先判斷
# -------------------------------------------------------------------

# 輸入說明:
# 第一行，輸入溫度 (0 ~ 100，為一整數)
# 第二行，輸入濕度 (0 ~ 100，為一整數)
# 第三行，輸入有無起風 (0、1，0代表沒風，1代表有風)

# 輸出說明:
# 根據條件決定要不要開冷氣
# 如果要開冷氣，請輸出要設定的溫度
# 如果不開冷氣，請輸出 Today is cool

# -------------------------------------------------------------------

# 範例輸入 1說明:
# 50 (溫度為 50)
# 20 (濕度為 20)
# 0 (沒有起風)

# 範例輸出 1說明:
# 18 (溫度高於50，符合條件1，開冷氣且設定為18度)

# 範例輸入 4說明:
# 25 (溫度為 25)
# 60 (濕度為 60)
# 1 (有起風)

# 範例輸出4說明:
# 27 (溫度介於25~29，濕度介於60~84，有起風，符合條件4，開冷氣且設定27度)

# -------------------------------------------------------------------


# Example Input 1：
# 50
# 20
# 0

# Example Output 1：
# 18

# -------------------------------------------------------------------

# Example Input 2：
# 20
# 100
# 1

# Example Output 2：
# Today is cool
# -------------------------------------------------------------------

# Example Input 3：
# 25
# 85
# 1

# Example Output 3：
# 24

# -------------------------------------------------------------------

# Example Input 4：
# 25
# 60
# 1

# Example Output 4：
# 27
# -------------------------------------------------------------------

# Example Input 5：
# 29
# 50
# 0

# Example Output 5：
# 27

# -------------------------------------------------------------------

# Example Input 6：
# 25
# 0
# 1

# Example Output 6：
# Today is cool


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