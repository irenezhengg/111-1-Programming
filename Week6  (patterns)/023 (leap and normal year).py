# 23. 閏年判斷
# 閏年(Leap year)是指該年有366日，比一般年份(365日)多出了一天。閏年是為了彌補人為制定的曆法天數365日，與回歸年大約365天又6小時的差距而設立的，我們可以得知陽曆每四年有一個閏年，全年共三百六十六天。並且包含以下規則:
# 公元年分非4的倍數，為平年。
# 公元年分為4的倍數但非100的倍數，為閏年。
# 公元年分為100的倍數但非400的倍數，為平年。
# 公元年分為400的倍數為閏年。

# 現在給予N個年份( 1 <= N <= 10)
# 印出這些年份為閏年或平年，年份的範圍為公元1年到公元10000年
# 例如N = 5時：
# 輸入為：
# 5
# 1987
# 1988
# 1990
# 1991
# 1992

# 輸出為：
# 1987 is normal year.
# 1988 is leap year.
# 1990 is normal year.
# 1991 is normal year.
# 1992 is leap year.
# -------------------------------------------------------------------------------------------------

# 輸入說明:
# 第一行輸入N個年份 (1 <= N <= 10)。
# 接下來N行，每行皆輸入年份Y (1 <= Y <= 10000)。

# 輸出說明:
# 依照輸入的N值，輸入N個年份，並且根據輸入的年份，判斷閏年或是平年。

# -------------------------------------------------------------------------------------------------


# 範例輸入 1:
# 2
# 1900
# 2000

# 範例輸出 1:
# 1900 is normal year.
# 2000 is leap year.

# -------------------------------------------------------------------------------------------------

# 範例輸入 2:
# 3
# 1888
# 1901
# 2000

# 範例輸出 2:
# 1888 is leap year.
# 1901 is normal year.
# 2000 is leap year.

# -------------------------------------------------------------------------------------------------

# 範例輸入 3:
# 9
# 1500
# 1600
# 1700
# 1800
# 1900
# 2000
# 2100
# 2020
# 2021

#  
# 範例輸出 3:
# 1500 is normal year.
# 1600 is leap year.
# 1700 is normal year.
# 1800 is normal year.
# 1900 is normal year.
# 2000 is leap year.
# 2100 is normal year.
# 2020 is leap year.
# 2021 is normal year.


def logika(listTahun):
    for tahun in listTahun:
        print(tahun, end='')
        print(" is ", end='')
        if ((tahun%400 == 0 and tahun%100 == 0) or (tahun%100 != 0 and tahun%4 == 0)):
            print("leap", end='')
        else:
            print("normal", end='')
        print(" tahun.")


def main():
    try:
        a = int(input())
    except:
        print("Input is not an int.")

    if (a < 1 or a > 10):
        print("Error")
        return

    listTahun=[]

    try:
        for i in range(0, a, 1):
            tahun = int(input())
            if (tahun < 1 or tahun > 10000):
                print("Error")
                return
            listTahun.append(tahun)
    except:
        print("Input is not an int.")
    
    logika(listTahun)

if __name__ == '__main__':
    main()