def calc_BMI1(name1, H1, W1):
    BMI1 = W1 / (H1**2)
    if BMI1 > 24 :
        print("Hi",name1+", Your BMI:","%.2f"%BMI1,"too HIGH.")
    elif BMI1 <18.5:
        print("Hi",name1+", Your BMI:","%.2f"%BMI1,"too LOW.")
    else:
        print("Hi",name1+", Your BMI:","%.2f"%BMI1+".")

def calc_BMI2(name2, H2, W2):
    BMI2 = W2 / (H2**2)
    if BMI2 > 24 :
        print("Hi",name2+", Your BMI:","%.2f"%BMI2,"too HIGH.")
    elif BMI2 <18.5:
        print("Hi",name2+", Your BMI:","%.2f"%BMI2,"too LOW.")
    else:
        print("Hi",name2+", Your BMI:","%.2f"%BMI2+".")

def compare(name1, H1, W1, name2, H2, W2):
    BMI1 = W1 / (H1**2)
    BMI2 = W2 / (H2**2)
    if BMI1 > BMI2:
        print('{}\'s BMI is larger than {}.'. format(name1, name2))
    else:
        print('{}\'s BMI is larger than {}.'. format(name2, name1))
        
name1 = input()
W1 = float(input())
H1 = float(input())

name2 = input()
W2 = float(input())
H2 = float(input())

calc_BMI1(name1, H1, W1)
calc_BMI2(name2, H2, W2)
compare(name1, H1, W1, name2, H2, W2)