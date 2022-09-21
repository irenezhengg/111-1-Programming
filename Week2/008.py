name = input()
bd = input()
name = name.split(" ")
bd = bd.split("/")

data = {'FirstName' : name[0], 'LastName' : name[1], 'yyyy' : bd[0], 'mm' : bd[1], 'dd' : bd[2]}

str = "{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.".format(**data)
print(str)