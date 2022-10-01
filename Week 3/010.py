import math
def main():
    score_dict = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":0.5, "Q":0.5, "K":0.5}
    A1 = score_dict[input()]
    A2 = score_dict[input()]
    A3 = score_dict[input()]
    B1 = score_dict[input()]
    B2 = score_dict[input()]
    B3 = score_dict[input()]
    score_A = A1 + A2 + A3
    score_B = B1 + B2 + B3
    overscore(score_A)
    overscore(score_B)
    judge(overscore(score_A),overscore(score_B))
    
def overscore(x):
    if (x > 10.5):
        return 0
    else :
        return x

def judge(y1,y2):
    print (y1)
    print (y2)
    if (y1 > y2):
        print("A Win")
    elif (y2 > y1):
        print("B Win")
    elif ( y1 == y2):
        print("Tie")
main()