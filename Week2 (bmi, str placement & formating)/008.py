# 008.
# 輸入為一個人的全名加上一組生日，
# 將以上資訊依下列格式輸出，
# {FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.

# ---------------------------------------------------

# 輸入說明：
# 第一行，輸入一個人的全名，
# 順序為FirstName LastName

# 第二行，輸入他的生日，
# 生日年、月、日會以/隔開，格式為yyyy/mm/dd

# 輸出說明：
# 套用以下格式輸出
# {FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.

# ---------------------------------------------------

# Example Input 1:
# kobe Bryant
# 1978/08/23

# Example Output 1:
# kobe is born at year 1978 month 08 day 23 in Bryant family.

# ---------------------------------------------------

# Example Input 2:
# kevin love
# 1988/09/07

# Example Output 2:
# kevin is born at year 1988 month 09 day 07 in love family.

# ---------------------------------------------------

# Example Input 3:
# Stephen Curry
# 1988/03/14

# Example Output 3:
# Stephen is born at year 1988 month 03 day 14 in Curry family.

name = input()
bd = input()
name = name.split(" ")
bd = bd.split("/")

data = {'FirstName' : name[0], 'LastName' : name[1], 'yyyy' : bd[0], 'mm' : bd[1], 'dd' : bd[2]}

str = "{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.".format(**data)
print(str)